import typing
from typing import Any, List, Set

from fwego.contrib.database.fields.dependencies.exceptions import (
    SelfReferenceFieldDependencyError,
)
from fwego.contrib.database.fields.dependencies.models import FieldDependency
from fwego.contrib.database.fields.dependencies.types import FieldDependencies
from fwego.contrib.database.formula.ast.tree import (
    FwegoBooleanLiteral,
    FwegoDecimalLiteral,
    FwegoFieldReference,
    FwegoFunctionCall,
    FwegoFunctionDefinition,
    FwegoIntegerLiteral,
    FwegoStringLiteral,
)
from fwego.contrib.database.formula.ast.visitors import FwegoFormulaASTVisitor
from fwego.contrib.database.formula.types.exceptions import (
    get_invalid_field_and_table_formula_error,
)
from fwego.contrib.database.formula.types.formula_type import (
    FwegoFormulaValidType,
    UnTyped,
)
from fwego.contrib.database.formula.types.formula_types import (
    FwegoExpression,
    FwegoFormulaBooleanType,
    FwegoFormulaNumberType,
    FwegoFormulaTextType,
    FwegoFormulaType,
)

if typing.TYPE_CHECKING:
    from fwego.contrib.database.fields.field_cache import FieldCache
    from fwego.contrib.database.fields.models import Field, LinkRowField


class FunctionsUsedVisitor(
    FwegoFormulaASTVisitor[Any, Set[FwegoFunctionDefinition]]
):
    def visit_field_reference(self, field_reference: FwegoFieldReference):
        return {field_reference}

    def visit_string_literal(
        self, string_literal: FwegoStringLiteral
    ) -> Set[FwegoFunctionDefinition]:
        return set()

    def visit_boolean_literal(
        self, boolean_literal: FwegoBooleanLiteral
    ) -> Set[FwegoFunctionDefinition]:
        return set()

    def visit_function_call(
        self, function_call: FwegoFunctionCall
    ) -> Set[FwegoFunctionDefinition]:
        all_used_functions = {function_call.function_def}
        for expr in function_call.args:
            all_used_functions.update(expr.accept(self))

        return all_used_functions

    def visit_int_literal(
        self, int_literal: FwegoIntegerLiteral
    ) -> Set[FwegoFunctionDefinition]:
        return set()

    def visit_decimal_literal(
        self, decimal_literal: FwegoDecimalLiteral
    ) -> Set[FwegoFunctionDefinition]:
        return set()


class FieldDependencyExtractingVisitor(
    FwegoFormulaASTVisitor[UnTyped, FieldDependencies]
):
    """
    Calculates and returns all the field dependencies that the fwego expression has.
    """

    def __init__(self, source_field, table, field_cache):
        self.source_field = source_field
        self.field_cache = field_cache
        self.table = table

    def visit_field_reference(
        self, field_reference: FwegoFieldReference[UnTyped]
    ) -> FieldDependencies:
        from fwego.contrib.database.fields.models import LinkRowField

        source_field = self.source_field
        referenced_field_name = field_reference.referenced_field_name
        field_cache = self.field_cache
        table = self.table

        if source_field.name == referenced_field_name:
            # If our field name is the same as the field(name), we are referencing
            # ourselves incorrectly.
            raise SelfReferenceFieldDependencyError()

        referenced_field = field_cache.lookup_by_name(table, referenced_field_name)
        if referenced_field is None:
            # There is no field with referenced_field_name in the table, setup a broken
            # dependency to that name so if one is created source_field gets fixed
            # automatically.
            return [
                FieldDependency(
                    dependant=source_field,
                    broken_reference_field_name=referenced_field_name,
                )
            ]

        target_field_name = field_reference.target_field
        if isinstance(referenced_field, LinkRowField):
            return self._visit_field_reference_to_link_row_field(
                field_cache, referenced_field, source_field, target_field_name
            )
        elif target_field_name is None:
            # We are just a normal field() reference pointing at a non link row field.
            return [
                FieldDependency(
                    dependant=source_field, dependency=referenced_field, via=None
                )
            ]
        else:
            # We are a lookup but our via_field is not a link row field.
            # Depend on the via field directly so if it is renamed/deleted/changed
            # we get notified and fixed if it is converted to a link row.
            return [
                FieldDependency(dependant=source_field, dependency=referenced_field)
            ]

    def _visit_field_reference_to_link_row_field(
        self,
        field_cache: "FieldCache",
        referenced_field: "LinkRowField",
        source_field: "Field",
        target_field_name: typing.Optional[str],
    ):
        # We are referencing a link row field , which means we are either a lookup
        # or a field() reference of a link row field, which is the same as a
        # lookup of the primary field in the linked table.
        via_field = referenced_field
        if target_field_name is None:
            # We don't have a target field so we are not a lookup and must be
            # a field() reference of a link row field.

            primary_field_in_other_table = via_field.link_row_table_primary_field
            if primary_field_in_other_table is None:
                return []
            else:
                if primary_field_in_other_table.id == source_field.id:
                    raise SelfReferenceFieldDependencyError()
                return [
                    FieldDependency(
                        dependant=source_field,
                        dependency=primary_field_in_other_table,
                        via=via_field,
                    ),
                ]
        else:
            # We are a lookup()
            target_table = via_field.link_row_table
            target_field = field_cache.lookup_by_name(target_table, target_field_name)
            if target_field is None:
                # We can't find the target field, but we have found the via field,
                # setup a broken dep pointing at the unknown field name in the other
                # table via the link row field so source_field gets fixed if a
                # field with that name is created/renamed in the other table.
                return [
                    FieldDependency(
                        dependant=source_field,
                        broken_reference_field_name=target_field_name,
                        via=via_field,
                    ),
                ]
            else:
                if target_field.id == source_field.id:
                    raise SelfReferenceFieldDependencyError()
                # We found all the fields correctly and they are valid so setup the
                # dep to the other table via the link row field at the target field.
                return [
                    FieldDependency(
                        dependant=source_field,
                        dependency=target_field,
                        via=via_field,
                    ),
                ]

    def visit_string_literal(
        self, string_literal: FwegoStringLiteral[UnTyped]
    ) -> FieldDependencies:
        return []

    def visit_function_call(
        self, function_call: FwegoFunctionCall[UnTyped]
    ) -> FieldDependencies:
        field_references: FieldDependencies = []
        for expr in function_call.args:
            field_references.extend(expr.accept(self))
        return field_references

    def visit_int_literal(
        self, int_literal: FwegoIntegerLiteral[UnTyped]
    ) -> FieldDependencies:
        return []

    def visit_decimal_literal(
        self, decimal_literal: FwegoDecimalLiteral[UnTyped]
    ) -> FieldDependencies:
        return []

    def visit_boolean_literal(
        self, boolean_literal: FwegoBooleanLiteral[UnTyped]
    ) -> FieldDependencies:
        return []


class FormulaTypingVisitor(
    FwegoFormulaASTVisitor[UnTyped, FwegoExpression[FwegoFormulaType]]
):
    def __init__(self, field_being_typed, field_cache):
        self.field_cache = field_cache
        self.field_being_typed = field_being_typed

    def visit_field_reference(
        self, field_reference: FwegoFieldReference[UnTyped]
    ) -> FwegoExpression[FwegoFormulaType]:
        from fwego.contrib.database.fields.registries import field_type_registry

        referenced_field_name = field_reference.referenced_field_name
        if referenced_field_name == self.field_being_typed.name:
            raise SelfReferenceFieldDependencyError()

        table = self.field_being_typed.table
        referenced_field = self.field_cache.lookup_by_name(table, referenced_field_name)
        if referenced_field is None:
            return field_reference.with_invalid_type(
                f"references the deleted or unknown field"
                f" {field_reference.referenced_field_name}"
            )
        else:
            field_type = field_type_registry.get_by_model(referenced_field)
            target_field = field_reference.target_field
            if target_field is not None:  # it's a lookup, verify the target field
                from fwego.contrib.database.fields.models import LinkRowField

                if not isinstance(referenced_field, LinkRowField):
                    return field_reference.with_invalid_type(
                        "first lookup function argument must be a link row field"
                    )
                target_table = referenced_field.link_row_table

                target_field = self.field_cache.lookup_by_name(
                    target_table, target_field
                )
                if target_field is None:
                    return field_reference.with_invalid_type(
                        get_invalid_field_and_table_formula_error(
                            field_reference.target_field, target_table.name
                        )
                    )
                else:
                    return self._create_lookup_reference(
                        target_field, referenced_field, field_reference
                    )
            # check the lookup field
            expression = field_type.to_fwego_formula_expression(referenced_field)
            # if other formula fields are referenced, we want to avoid
            # keep nesting wrapper functions, so unwrap the expression here
            if expression.is_wrapper:
                expression = expression.expression_type.unwrap_at_field_level(
                    expression
                )
            return expression

    def _create_lookup_reference(self, target_field, referenced_field, field_reference):
        from fwego.contrib.database.fields.models import LinkRowField
        from fwego.contrib.database.fields.registries import field_type_registry

        if isinstance(target_field, LinkRowField):
            if (
                target_field.link_row_table_id == self.field_being_typed.table_id
                and self.field_being_typed.primary
            ):
                return field_reference.with_invalid_type(
                    "references itself via a link field causing a circular dependency"
                )
            # If we are looking up a link row field we need to do an
            # extra relational jump to that primary field.
            related_primary_field = target_field.link_row_table_primary_field
            if related_primary_field is None:
                return field_reference.with_invalid_type(
                    "references a deleted or unknown table"
                )
            sub_ref = "__" + related_primary_field.db_column
        else:
            sub_ref = ""

        lookup_field_type = field_type_registry.get_by_model(target_field)
        formula_type = lookup_field_type.to_fwego_formula_type(target_field)

        return FwegoFieldReference(
            referenced_field.db_column,
            target_field.db_column + sub_ref,
            formula_type,
        )

    def visit_string_literal(
        self, string_literal: FwegoStringLiteral[UnTyped]
    ) -> FwegoExpression[FwegoFormulaType]:
        return string_literal.with_valid_type(FwegoFormulaTextType())

    def visit_function_call(
        self, function_call: FwegoFunctionCall[UnTyped]
    ) -> FwegoExpression[FwegoFormulaType]:
        typed_args: List[FwegoExpression[FwegoFormulaValidType]] = []
        requires_aggregate_wrapper = []
        for index, expr in enumerate(function_call.args):
            arg_expr = expr.accept(self)
            if arg_expr.requires_aggregate_wrapper:
                requires_aggregate_wrapper.append(str(index + 1))

            function_def = function_call.function_def
            expr_type = arg_expr.expression_type
            if expr_type.nullable and function_def.try_coerce_nullable_args_to_not_null:
                arg_expr = expr_type.try_coerce_to_not_null(arg_expr)

            typed_args.append(arg_expr)

        if requires_aggregate_wrapper and not function_call.function_def.aggregate:
            plural_s = (
                "s numbered" if len(requires_aggregate_wrapper) > 1 else " number"
            )
            return function_call.with_invalid_type(
                f"input{plural_s} {','.join(requires_aggregate_wrapper)} to"
                f" {function_call.function_def} must be directly wrapped by an "
                f"aggregate function like sum, avg, count etc"
            )
        return function_call.type_function_given_typed_args(typed_args)

    def visit_int_literal(
        self, int_literal: FwegoIntegerLiteral[UnTyped]
    ) -> FwegoExpression[FwegoFormulaType]:
        return int_literal.with_valid_type(
            FwegoFormulaNumberType(
                number_decimal_places=0,
            ),
        )

    def visit_decimal_literal(
        self, decimal_literal: FwegoDecimalLiteral[UnTyped]
    ) -> FwegoExpression[FwegoFormulaType]:
        return decimal_literal.with_valid_type(
            FwegoFormulaNumberType(
                number_decimal_places=decimal_literal.num_decimal_places()
            )
        )

    def visit_boolean_literal(
        self, boolean_literal: FwegoBooleanLiteral[UnTyped]
    ) -> FwegoExpression[FwegoFormulaType]:
        return boolean_literal.with_valid_type(FwegoFormulaBooleanType())
