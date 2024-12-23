from decimal import Decimal

from fwego.contrib.database.formula.ast.tree import (
    FwegoBooleanLiteral,
    FwegoDecimalLiteral,
    FwegoExpression,
    FwegoFieldReference,
    FwegoFunctionCall,
    FwegoIntegerLiteral,
    FwegoStringLiteral,
)
from fwego.contrib.database.formula.registries import formula_function_registry
from fwego.contrib.database.formula.types.formula_type import UnTyped
from fwego.core.formula.parser.exceptions import (
    FwegoFormulaSyntaxError,
    FieldByIdReferencesAreDeprecated,
    FormulaFunctionTypeDoesNotExist,
    InvalidNumberOfArguments,
    MaximumFormulaSizeError,
    UnknownOperator,
)
from fwego.core.formula.parser.generated.FwegoFormula import FwegoFormula
from fwego.core.formula.parser.generated.FwegoFormulaVisitor import (
    FwegoFormulaVisitor,
)
from fwego.core.formula.parser.parser import (
    convert_string_literal_token_to_string,
    get_parse_tree_for_formula,
)


def raw_formula_to_untyped_expression(
    formula: str,
) -> FwegoExpression[UnTyped]:
    """
    Takes a raw user input string, syntax checks it to see if it matches the syntax of
    a Fwego Formula (raises a FwegoFormulaSyntaxError if not) and converts it into
    an untyped FwegoExpression.

    :param formula: A raw user supplied string possibly in the format of a Fwego
        Formula.
    :return: An untyped FwegoExpression which represents the provided raw formula.
    :raises FwegoFormulaSyntaxError: If the supplied formula is not in the syntax
        of the Fwego Formula language.
    """

    try:
        tree = get_parse_tree_for_formula(formula)
        return FwegoFormulaToFwegoASTMapper().visit(tree)
    except RecursionError:
        raise MaximumFormulaSizeError()


class FwegoFormulaToFwegoASTMapper(FwegoFormulaVisitor):
    """
    A Visitor which transforms an Antlr parse tree into a FwegoExpression AST.

    Raises an UnknownBinaryOperator if the formula contains an unknown binary operator.

    Raises an UnknownFunctionDefinition if the formula has a function call to a function
    not in the registry.
    """

    def visitRoot(self, ctx: FwegoFormula.RootContext):
        return ctx.expr().accept(self)

    def visitStringLiteral(self, ctx: FwegoFormula.StringLiteralContext):
        # noinspection PyTypeChecker
        literal = self.process_string(ctx)
        return FwegoStringLiteral(literal, None)

    def visitDecimalLiteral(self, ctx: FwegoFormula.DecimalLiteralContext):
        return FwegoDecimalLiteral(Decimal(ctx.getText()), None)

    def visitBooleanLiteral(self, ctx: FwegoFormula.BooleanLiteralContext):
        return FwegoBooleanLiteral(ctx.TRUE() is not None, None)

    def visitBrackets(self, ctx: FwegoFormula.BracketsContext):
        return ctx.expr().accept(self)

    def process_string(self, ctx):
        literal_without_outer_quotes = ctx.getText()[1:-1]
        if ctx.SINGLEQ_STRING_LITERAL() is not None:
            literal = literal_without_outer_quotes.replace("\\'", "'")
        else:
            literal = literal_without_outer_quotes.replace('\\"', '"')
        return literal

    def visitFunctionCall(self, ctx: FwegoFormula.FunctionCallContext):
        function_name = ctx.func_name().accept(self).lower()
        function_argument_expressions = ctx.expr()

        return self._do_func(function_argument_expressions, function_name)

    def _do_func(self, function_argument_expressions, function_name):
        function_def = self._get_function_def(function_name)
        self._check_function_call_valid(function_argument_expressions, function_def)
        args = [expr.accept(self) for expr in function_argument_expressions]
        return FwegoFunctionCall[UnTyped](function_def, args, None)

    def visitBinaryOp(self, ctx: FwegoFormula.BinaryOpContext):
        if ctx.PLUS():
            op = "add"
        elif ctx.MINUS():
            op = "minus"
        elif ctx.SLASH():
            op = "divide"
        elif ctx.EQUAL():
            op = "equal"
        elif ctx.BANG_EQUAL():
            op = "not_equal"
        elif ctx.STAR():
            op = "multiply"
        elif ctx.GT():
            op = "greater_than"
        elif ctx.LT():
            op = "less_than"
        elif ctx.GTE():
            op = "greater_than_or_equal"
        elif ctx.LTE():
            op = "less_than_or_equal"
        elif ctx.AMP_AMP():
            op = "and"
        elif ctx.PIPE_PIPE():
            op = "or"
        else:
            raise UnknownOperator(ctx.getText())

        return self._do_func(ctx.expr(), op)

    @staticmethod
    def _check_function_call_valid(function_argument_expressions, function_def):
        num_expressions = len(function_argument_expressions)
        if not function_def.num_args.test(num_expressions):
            raise InvalidNumberOfArguments(function_def, num_expressions)

    @staticmethod
    def _get_function_def(function_name):
        try:
            function_def = formula_function_registry.get(function_name)
        except FormulaFunctionTypeDoesNotExist:
            raise FwegoFormulaSyntaxError(f"{function_name} is not a valid function")
        return function_def

    def visitFunc_name(self, ctx: FwegoFormula.Func_nameContext):
        return ctx.getText()

    def visitIdentifier(self, ctx: FwegoFormula.IdentifierContext):
        return ctx.getText()

    def visitIntegerLiteral(self, ctx: FwegoFormula.IntegerLiteralContext):
        return FwegoIntegerLiteral[UnTyped](int(ctx.getText()), None)

    def visitFieldReference(self, ctx: FwegoFormula.FieldReferenceContext):
        reference = ctx.field_reference()
        field_name = convert_string_literal_token_to_string(
            reference.getText(), reference.SINGLEQ_STRING_LITERAL()
        )
        return FwegoFieldReference[UnTyped](field_name, None, None)

    def visitLookupFieldReference(
        self, ctx: FwegoFormula.LookupFieldReferenceContext
    ):
        reference = ctx.field_reference(0)
        field_name = convert_string_literal_token_to_string(
            reference.getText(), reference.SINGLEQ_STRING_LITERAL()
        )
        lookup = ctx.field_reference(1)
        lookup_name = convert_string_literal_token_to_string(
            lookup.getText(), reference.SINGLEQ_STRING_LITERAL()
        )
        return FwegoFieldReference[UnTyped](field_name, lookup_name, None)

    def visitFieldByIdReference(self, ctx: FwegoFormula.FieldByIdReferenceContext):
        raise FieldByIdReferencesAreDeprecated()

    def visitLeftWhitespaceOrComments(
        self, ctx: FwegoFormula.LeftWhitespaceOrCommentsContext
    ):
        return ctx.expr().accept(self)

    def visitRightWhitespaceOrComments(
        self, ctx: FwegoFormula.RightWhitespaceOrCommentsContext
    ):
        return ctx.expr().accept(self)


class FwegoFieldReferenceVisitor(FwegoFormulaVisitor):
    """
    Visitor which visits a Fwego Formula parse tree and returns a set of field
    references found in the formula. This is used for example when importing
    new tables with formula fields to import the fields in the correct order.
    """

    def visitRoot(self, ctx: FwegoFormula.RootContext):
        return ctx.expr().accept(self)

    def visitStringLiteral(self, ctx: FwegoFormula.StringLiteralContext):
        return set()

    def visitDecimalLiteral(self, ctx: FwegoFormula.DecimalLiteralContext):
        return set()

    def visitBooleanLiteral(self, ctx: FwegoFormula.BooleanLiteralContext):
        return set()

    def visitBrackets(self, ctx: FwegoFormula.BracketsContext):
        return ctx.expr().accept(self)

    def visitLookupFieldReference(
        self, ctx: FwegoFormula.LookupFieldReferenceContext
    ):
        reference = ctx.field_reference(1)
        field_name = convert_string_literal_token_to_string(
            reference.getText(), reference.SINGLEQ_STRING_LITERAL()
        )

        reference = ctx.field_reference(0)
        via_field_name = convert_string_literal_token_to_string(
            reference.getText(), reference.SINGLEQ_STRING_LITERAL()
        )

        if not field_name:
            return set()

        return {(field_name, via_field_name)}

    def visitFunctionCall(self, ctx: FwegoFormula.FunctionCallContext):
        args = set()
        for expr in ctx.expr():
            args.update(expr.accept(self))
        return args

    def visitFunc_name(self, ctx: FwegoFormula.Func_nameContext):
        return set()

    def visitIdentifier(self, ctx: FwegoFormula.IdentifierContext):
        return set()

    def visitIntegerLiteral(self, ctx: FwegoFormula.IntegerLiteralContext):
        return set()

    def visitFieldReference(self, ctx: FwegoFormula.FieldReferenceContext):
        reference = ctx.field_reference()
        field_name = convert_string_literal_token_to_string(
            reference.getText(), reference.SINGLEQ_STRING_LITERAL()
        )
        return {(field_name, None)}

    def visitFieldByIdReference(self, ctx: FwegoFormula.FieldByIdReferenceContext):
        return set()

    def visitLeftWhitespaceOrComments(
        self, ctx: FwegoFormula.LeftWhitespaceOrCommentsContext
    ):
        return ctx.expr().accept(self)

    def visitRightWhitespaceOrComments(
        self, ctx: FwegoFormula.RightWhitespaceOrCommentsContext
    ):
        return ctx.expr().accept(self)

    def visitBinaryOp(self, ctx: FwegoFormula.RightWhitespaceOrCommentsContext):
        args = set()
        for expr in ctx.expr():
            args.update(expr.accept(self))
        return args
