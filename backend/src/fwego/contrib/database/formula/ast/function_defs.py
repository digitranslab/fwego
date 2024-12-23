from abc import ABC
from datetime import timedelta
from decimal import Decimal
from typing import List

from django.contrib.postgres.aggregates import JSONBAgg
from django.db.models import (
    Avg,
    Case,
    Count,
    DecimalField,
    Expression,
    ExpressionWrapper,
    F,
    Func,
    JSONField,
    Max,
    Min,
    OuterRef,
    StdDev,
    Subquery,
    Sum,
    Value,
    Variance,
    When,
    fields,
)
from django.db.models.functions import (
    Abs,
    Cast,
    Ceil,
    Coalesce,
    Concat,
    Exp,
    Extract,
    Floor,
    Greatest,
    JSONObject,
    Least,
    Left,
    Length,
    Ln,
    Log,
    Lower,
    Mod,
    Power,
    Replace,
    Reverse,
    Right,
    Sign,
    Sqrt,
    StrIndex,
    Trim,
    Upper,
)
from django.db.models.functions.datetime import TimezoneMixin

from fwego.contrib.database.fields.models import NUMBER_MAX_DECIMAL_PLACES
from fwego.contrib.database.formula.ast.function import (
    FwegoFunctionDefinition,
    CollapseManyFwegoFunction,
    NumOfArgsBetween,
    NumOfArgsGreaterThan,
    OneArgumentFwegoFunction,
    ThreeArgumentFwegoFunction,
    TwoArgumentFwegoFunction,
    ZeroArgumentFwegoFunction,
    aggregate_expr_with_metadata_filters,
    aggregate_wrapper,
    construct_aggregate_wrapper_queryset,
    construct_not_null_filters_for_inner_join,
)
from fwego.contrib.database.formula.ast.tree import (
    FwegoDecimalLiteral,
    FwegoExpression,
    FwegoExpressionContext,
    FwegoFunctionCall,
    FwegoIntegerLiteral,
)
from fwego.contrib.database.formula.expression_generator.django_expressions import (
    AndExpr,
    FwegoStringAgg,
    EqualsExpr,
    GreaterThanExpr,
    GreaterThanOrEqualExpr,
    IsNullExpr,
    LessThanEqualOrExpr,
    LessThanExpr,
    NotEqualsExpr,
    NotExpr,
    OrExpr,
)
from fwego.contrib.database.formula.expression_generator.exceptions import (
    FwegoToDjangoExpressionGenerationError,
)
from fwego.contrib.database.formula.expression_generator.generator import (
    JoinIdsType,
    WrappedExpressionWithMetadata,
)
from fwego.contrib.database.formula.types.formula_type import (
    FwegoFormulaType,
    FwegoFormulaValidType,
    UnTyped,
)
from fwego.contrib.database.formula.types.formula_types import (
    FwegoFormulaArrayType,
    FwegoFormulaBooleanType,
    FwegoFormulaButtonType,
    FwegoFormulaCharType,
    FwegoFormulaDateType,
    FwegoFormulaDurationType,
    FwegoFormulaLinkType,
    FwegoFormulaMultipleSelectType,
    FwegoFormulaNumberType,
    FwegoFormulaSingleFileType,
    FwegoFormulaSingleSelectType,
    FwegoFormulaTextType,
    FwegoFormulaURLType,
    FwegoJSONBObjectBaseType,
    calculate_number_type,
    literal,
)
from fwego.contrib.database.formula.types.type_checker import (
    FwegoArgumentTypeChecker,
    MustBeManyExprChecker,
)


class FwegoTimezoneMixinOverride(TimezoneMixin):
    def get_tzname(self):
        return None


class FwegoExtract(FwegoTimezoneMixinOverride, Extract):
    pass


def register_formula_functions(registry):
    # Text functions
    registry.register(FwegoUpper())
    registry.register(FwegoLower())
    registry.register(FwegoConcat())
    registry.register(FwegoToText())
    registry.register(FwegoToVarchar())
    registry.register(FwegoT())
    registry.register(FwegoReplace())
    registry.register(FwegoSearch())
    registry.register(FwegoLength())
    registry.register(FwegoReverse())
    registry.register(FwegoContains())
    registry.register(FwegoLeft())
    registry.register(FwegoRight())
    registry.register(FwegoTrim())
    registry.register(FwegoRegexReplace())
    registry.register(FwegoEncodeUri())
    registry.register(FwegoEncodeUriComponent())
    # Number functions
    registry.register(FwegoMultiply())
    registry.register(FwegoDivide())
    registry.register(FwegoToNumber())
    registry.register(FwegoErrorToNan())
    registry.register(FwegoGreatest())
    registry.register(FwegoLeast())
    registry.register(FwegoMod())
    registry.register(FwegoRound())
    registry.register(FwegoInt())
    registry.register(FwegoEven())
    registry.register(FwegoOdd())
    registry.register(FwegoTrunc())
    registry.register(FwegoSplitPart())
    registry.register(FwegoLn())
    registry.register(FwegoExp())
    registry.register(FwegoLog())
    registry.register(FwegoSqrt())
    registry.register(FwegoPower())
    registry.register(FwegoAbs())
    registry.register(FwegoCeil())
    registry.register(FwegoFloor())
    registry.register(FwegoSign())
    registry.register(FwegoIsNaN())
    registry.register(FwegoWhenNan())
    # Boolean functions
    registry.register(FwegoIf())
    registry.register(FwegoEqual())
    registry.register(FwegoIsBlank())
    registry.register(FwegoIsNull())
    registry.register(FwegoNot())
    registry.register(FwegoNotEqual())
    registry.register(FwegoGreaterThan())
    registry.register(FwegoGreaterThanOrEqual())
    registry.register(FwegoLessThan())
    registry.register(FwegoLessThanOrEqual())
    registry.register(FwegoAnd())
    registry.register(FwegoOr())
    # Date functions
    registry.register(FwegoDatetimeFormat())
    registry.register(FwegoDatetimeFormatTz())
    registry.register(FwegoDay())
    registry.register(FwegoMonth())
    registry.register(FwegoYear())
    registry.register(FwegoSecond())
    registry.register(FwegoToDate())
    registry.register(FwegoDateDiff())
    registry.register(FwegoBcToNull())
    registry.register(FwegoNow())
    registry.register(FwegoToday())
    registry.register(FwegoToDateTz())
    # Date interval functions
    registry.register(FwegoDateInterval())
    registry.register(FwegoSecondsToDuration())
    registry.register(FwegoDurationToSeconds())
    # Special functions
    registry.register(FwegoAdd())
    registry.register(FwegoMinus())
    registry.register(FwegoErrorToNull())
    registry.register(FwegoRowId())
    registry.register(FwegoWhenEmpty())
    # Array functions
    registry.register(FwegoArrayAgg())
    registry.register(Fwego2dArrayAgg())
    registry.register(FwegoMultipleSelectOptionsAgg())
    registry.register(FwegoAny())
    registry.register(FwegoEvery())
    registry.register(FwegoMax())
    registry.register(FwegoMin())
    registry.register(FwegoCount())
    registry.register(FwegoFilter())
    registry.register(FwegoAggJoin())
    registry.register(FwegoStdDevPop())
    registry.register(FwegoStdDevSample())
    registry.register(FwegoVarianceSample())
    registry.register(FwegoVariancePop())
    registry.register(FwegoAvg())
    registry.register(FwegoSum())
    # Single Select functions
    registry.register(FwegoGetSingleSelectValue())
    # Multiple Select functions
    registry.register(FwegoHasOption())
    registry.register(FwegoMultipleSelectCount())
    registry.register(FwegoStringAggMultipleSelectValues())
    registry.register(FwegoStringAggArrayOfMultipleSelectValues())
    # Link functions
    registry.register(FwegoLink())
    registry.register(FwegoButton())
    registry.register(FwegoGetLinkUrl())
    registry.register(FwegoGetLinkLabel())
    # JSON functions
    registry.register(FwegoJsonbExtractPathText())
    registry.register(FwegoIndex())
    # FIle functions
    registry.register(FwegoGetFileVisibleName())
    registry.register(FwegoGetFileMimeType())
    registry.register(FwegoGetFileSize())
    registry.register(FwegoGetImageWidth())
    registry.register(FwegoGetImageHeight())
    registry.register(FwegoIsImage())
    registry.register(FwegoArrayAggNoNesting())
    registry.register(FwegoGetFileCount())
    registry.register(FwegoToURL())


class FwegoUpper(OneArgumentFwegoFunction):
    type = "upper"
    arg_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaTextType(nullable=arg.expression_type.nullable)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Upper(arg, output_field=fields.TextField())


class FwegoLower(OneArgumentFwegoFunction):
    type = "lower"
    arg_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaTextType(nullable=arg.expression_type.nullable)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Lower(arg, output_field=fields.TextField())


class FwegoDatetimeFormat(TwoArgumentFwegoFunction):
    type = "datetime_format"
    arg1_type = [FwegoFormulaDateType]
    arg2_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaTextType(nullable=arg1.expression_type.nullable)
        )

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        if isinstance(arg1, Value) and arg1.value is None:
            return Value("")
        return Coalesce(
            Trim(
                Func(
                    arg1,
                    arg2,
                    function="to_char",
                    output_field=fields.TextField(),
                )
            ),
            Value(""),
            output_field=fields.TextField(),
        )


class FwegoDatetimeFormatTz(ThreeArgumentFwegoFunction):
    type = "datetime_format_tz"
    arg1_type = [FwegoFormulaDateType]
    arg2_type = [FwegoFormulaTextType]
    arg3_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
        arg3: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaTextType(nullable=True))

    def to_django_expression(
        self, arg1: Expression, arg2: Expression, arg3: Expression
    ) -> Expression:
        return Trim(
            Coalesce(
                Func(
                    arg1,
                    arg2,
                    arg3,
                    function="try_datetime_format_tz",
                    output_field=fields.TextField(),
                ),
                Value(""),
                output_field=fields.TextField(),
            ),
        )


class FwegoEncodeUri(OneArgumentFwegoFunction):
    type = "encode_uri"
    arg_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaTextType(nullable=arg.expression_type.nullable)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(
            arg,
            function="try_encode_uri",
            output_field=fields.TextField(),
        )


class FwegoEncodeUriComponent(OneArgumentFwegoFunction):
    type = "encode_uri_component"
    arg_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaTextType(nullable=arg.expression_type.nullable)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(
            arg,
            function="try_encode_uri_component",
            output_field=fields.TextField(),
        )


class FwegoToText(OneArgumentFwegoFunction):
    type = "totext"
    arg_type = [FwegoFormulaValidType]
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return arg.expression_type.cast_to_text(func_call, arg).with_valid_type(
            FwegoFormulaTextType()
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Coalesce(
            Cast(arg, output_field=fields.TextField()),
            Value(""),
            output_field=fields.TextField(),
        )


class FwegoToVarchar(OneArgumentFwegoFunction):
    """
    Internal function not registered in the frontend intentionally as we don't want
    users making char types. Used purely for working with our FwegoFormulaCharType
    on internal operations.
    """

    type = "tovarchar"
    arg_type = [FwegoFormulaTextType]
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return arg.with_valid_type(
            FwegoFormulaCharType(nullable=arg.expression_type.nullable)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Cast(arg, output_field=fields.CharField())


class FwegoT(OneArgumentFwegoFunction):
    type = "t"
    arg_type = [FwegoFormulaValidType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        if isinstance(arg.expression_type, FwegoFormulaTextType):
            return arg
        else:
            return func_call.with_valid_type(
                FwegoFormulaTextType(nullable=arg.expression_type.nullable)
            )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Cast(Value(""), output_field=fields.TextField())


class FwegoConcat(FwegoFunctionDefinition):
    type = "concat"
    num_args = NumOfArgsGreaterThan(1)
    try_coerce_nullable_args_to_not_null = False

    @property
    def arg_types(self) -> FwegoArgumentTypeChecker:
        return lambda _, _2: [FwegoFormulaValidType]

    def type_function_given_valid_args(
        self,
        args: List[FwegoExpression[FwegoFormulaValidType]],
        expression: "FwegoFunctionCall[UnTyped]",
    ) -> FwegoExpression[FwegoFormulaType]:
        typed_args = [FwegoToText()(a) for a in args]
        return expression.with_args(typed_args).with_valid_type(
            FwegoFormulaTextType()
        )

    def to_django_expression_given_args(
        self, expr_args: List[WrappedExpressionWithMetadata], *args, **kwargs
    ) -> WrappedExpressionWithMetadata:
        return WrappedExpressionWithMetadata.from_args(
            Concat(*[e.expression for e in expr_args], output_field=fields.TextField()),
            expr_args,
        )


class FwegoAdd(TwoArgumentFwegoFunction):
    type = "add"
    operator = "+"
    arg1_type = [FwegoFormulaNumberType]
    arg2_type = [FwegoFormulaNumberType]

    @property
    def arg_types(self) -> FwegoArgumentTypeChecker:
        def type_checker(arg_index: int, arg_types: List[FwegoFormulaType]):
            if arg_index == 1:
                return arg_types[0].addable_types
            else:
                return [FwegoFormulaValidType]

        return type_checker

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return arg1.expression_type.add(func_call, arg1, arg2)

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        # date + interval = date
        # non date/interval types + non date/interval types = first arg type always

        first_arg_is_duration = isinstance(arg1.output_field, fields.DurationField)
        second_arg_is_duration = isinstance(arg2.output_field, fields.DurationField)
        first_arg_is_date = isinstance(arg1.output_field, fields.DateField)
        second_arg_is_date = isinstance(arg2.output_field, fields.DateField)
        if (first_arg_is_duration or second_arg_is_duration) and (
            first_arg_is_date or second_arg_is_date
        ):
            # interval + date = datetime
            # date + interval = datetime
            output_field = fields.DateTimeField()
        elif first_arg_is_duration:
            # interval + interval = interval
            # interval + datetime = datetime
            output_field = arg2.output_field
        else:
            output_field = arg1.output_field
        return ExpressionWrapper(arg1 + arg2, output_field=output_field)


class FwegoMultiply(TwoArgumentFwegoFunction):
    type = "multiply"
    operator = "*"
    arg1_type = [FwegoFormulaNumberType]
    arg2_type = [FwegoFormulaNumberType]

    @property
    def arg_types(self) -> FwegoArgumentTypeChecker:
        def type_checker(arg_index: int, arg_types: List[FwegoFormulaType]):
            if arg_index == 1:
                return arg_types[0].multipliable_types
            else:
                return [FwegoFormulaValidType]

        return type_checker

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaNumberType],
        arg2: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return arg1.expression_type.multiply(func_call, arg1, arg2)

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        if isinstance(arg1.output_field, fields.DurationField):
            total_secs = Extract(arg1, "epoch", output_field=arg2.output_field) * arg2
            return ExpressionWrapper(
                timedelta(seconds=1) * total_secs,
                output_field=arg1.output_field,
            )
        else:
            return ExpressionWrapper(arg1 * arg2, output_field=arg1.output_field)


class FwegoMinus(TwoArgumentFwegoFunction):
    type = "minus"
    operator = "-"
    arg1_type = [FwegoFormulaNumberType]
    arg2_type = [FwegoFormulaNumberType]

    @property
    def arg_types(self) -> FwegoArgumentTypeChecker:
        def type_checker(arg_index: int, arg_types: List[FwegoFormulaType]):
            if arg_index == 1:
                # Only type check the left hand side is one of the subtractable types
                # of the right hand side argument.
                return arg_types[0].subtractable_types
            else:
                return [FwegoFormulaValidType]

        return type_checker

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return arg1.expression_type.minus(func_call, arg1, arg2)

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        first_arg_is_duration = isinstance(arg1.output_field, fields.DurationField)
        second_arg_is_duration = isinstance(arg2.output_field, fields.DurationField)
        first_arg_is_date = isinstance(arg1.output_field, fields.DateField)
        second_arg_is_date = isinstance(arg2.output_field, fields.DateField)
        if first_arg_is_duration and second_arg_is_duration:
            # interval - interval = interval
            output_field = fields.DurationField()
        elif first_arg_is_date and second_arg_is_duration:
            # date/datetime - interval = datetime
            output_field = fields.DateTimeField()
        elif first_arg_is_date and second_arg_is_date:
            # date - date = interval (django does this magic)
            output_field = fields.DurationField()
        else:
            output_field = arg1.output_field

        return ExpressionWrapper(arg1 - arg2, output_field=output_field)


class FwegoGreatest(TwoArgumentFwegoFunction):
    type = "greatest"
    arg1_type = [FwegoFormulaNumberType]
    arg2_type = [FwegoFormulaNumberType]
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaNumberType],
        arg2: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            calculate_number_type([arg1.expression_type, arg2.expression_type]),
            nullable=arg1.expression_type.nullable and arg2.expression_type.nullable,
        )

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return Greatest(arg1, arg2, output_field=arg1.output_field)


class FwegoLeast(TwoArgumentFwegoFunction):
    type = "least"
    arg1_type = [FwegoFormulaNumberType]
    arg2_type = [FwegoFormulaNumberType]
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaNumberType],
        arg2: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            calculate_number_type([arg1.expression_type, arg2.expression_type]),
            nullable=arg1.expression_type.nullable and arg2.expression_type.nullable,
        )

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return Least(arg1, arg2, output_field=arg1.output_field)


class FwegoRound(TwoArgumentFwegoFunction):
    type = "round"
    arg1_type = [FwegoFormulaNumberType]
    arg2_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaNumberType],
        arg2: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        if isinstance(arg2, FwegoIntegerLiteral):
            guessed_number_decimal_places = arg2.literal
        elif isinstance(arg2, FwegoDecimalLiteral):
            guessed_number_decimal_places = int(arg2.literal)
        else:
            guessed_number_decimal_places = NUMBER_MAX_DECIMAL_PLACES

        return func_call.with_valid_type(
            FwegoFormulaNumberType(
                number_decimal_places=min(
                    max(guessed_number_decimal_places, 0), NUMBER_MAX_DECIMAL_PLACES
                )
            )
        )

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return handle_arg_being_nan(
            arg_to_check_if_nan=arg2,
            when_nan=Value(Decimal("NaN")),
            when_not_nan=(
                Func(
                    Cast(
                        arg1,
                        output_field=DecimalField(
                            max_digits=FwegoFormulaNumberType.MAX_DIGITS,
                            decimal_places=NUMBER_MAX_DECIMAL_PLACES,
                        ),
                    ),
                    # The round function requires an integer input.
                    trunc_numeric_to_int(arg2),
                    function="round",
                    output_field=arg1.output_field,
                )
            ),
        )


class FwegoMod(TwoArgumentFwegoFunction):
    type = "mod"
    arg1_type = [FwegoFormulaNumberType]
    arg2_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaNumberType],
        arg2: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            calculate_number_type([arg1.expression_type, arg2.expression_type])
        )

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return Case(
            When(
                condition=(
                    EqualsExpr(arg2, Value(0), output_field=fields.BooleanField())
                ),
                then=Value(Decimal("NaN")),
            ),
            default=Mod(arg1, arg2, output_field=arg1.output_field),
            output_field=arg1.output_field,
        )


class FwegoPower(TwoArgumentFwegoFunction):
    type = "power"
    arg1_type = [FwegoFormulaNumberType]
    arg2_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaNumberType],
        arg2: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            calculate_number_type([arg1.expression_type, arg2.expression_type])
        )

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return Power(arg1, arg2, output_field=arg1.output_field)


class FwegoLog(TwoArgumentFwegoFunction):
    type = "log"
    arg1_type = [FwegoFormulaNumberType]
    arg2_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaNumberType],
        arg2: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            calculate_number_type([arg1.expression_type, arg2.expression_type])
        )

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return Case(
            When(
                condition=(
                    LessThanEqualOrExpr(
                        arg1, Value(0), output_field=fields.BooleanField()
                    )
                ),
                then=Value(Decimal("NaN")),
            ),
            When(
                condition=(
                    LessThanEqualOrExpr(
                        arg2, Value(0), output_field=fields.BooleanField()
                    )
                ),
                then=Value(Decimal("NaN")),
            ),
            default=Log(arg1, arg2, output_field=arg1.output_field),
            output_field=arg1.output_field,
        )


class FwegoAbs(OneArgumentFwegoFunction):
    type = "abs"
    arg_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return Abs(arg, output_field=arg.output_field)


class FwegoExp(OneArgumentFwegoFunction):
    type = "exp"
    arg_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return Exp(arg, output_field=arg.output_field)


class FwegoEven(OneArgumentFwegoFunction):
    type = "even"
    arg_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaBooleanType())

    def to_django_expression(self, arg: Expression) -> Expression:
        return EqualsExpr(
            Mod(arg, Value(2), output_field=arg.output_field),
            Value(0),
            output_field=fields.BooleanField(),
        )


class FwegoOdd(OneArgumentFwegoFunction):
    type = "odd"
    arg_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaBooleanType())

    def to_django_expression(self, arg: Expression) -> Expression:
        return EqualsExpr(
            Mod(arg, Value(2), output_field=arg.output_field),
            Value(1),
            output_field=fields.BooleanField(),
        )


class FwegoLn(OneArgumentFwegoFunction):
    type = "ln"
    arg_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        # If we get given a negative number ln will crash, instead just return NaN.
        return Case(
            When(
                condition=(
                    LessThanEqualOrExpr(
                        arg, Value(0), output_field=fields.BooleanField()
                    )
                ),
                then=Value(Decimal("NaN")),
            ),
            default=Ln(arg, output_field=arg.output_field),
            output_field=arg.output_field,
        )


class FwegoSqrt(OneArgumentFwegoFunction):
    type = "sqrt"
    arg_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        # If we get given a negative number sqrt will crash, instead just return NaN.
        return Case(
            When(
                condition=(
                    LessThanExpr(arg, Value(0), output_field=fields.BooleanField())
                ),
                then=Value(Decimal("NaN")),
            ),
            default=Sqrt(arg, output_field=arg.output_field),
            output_field=arg.output_field,
        )


class FwegoSign(OneArgumentFwegoFunction):
    type = "sign"
    arg_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(number_decimal_places=0)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Sign(arg, output_field=int_like_numeric_output_field())


class FwegoCeil(OneArgumentFwegoFunction):
    type = "ceil"
    arg_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(number_decimal_places=0)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Ceil(arg, output_field=int_like_numeric_output_field())


class FwegoFloor(OneArgumentFwegoFunction):
    type = "floor"
    arg_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(number_decimal_places=0)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Floor(arg, output_field=int_like_numeric_output_field())


class FwegoSplitPart(ThreeArgumentFwegoFunction):
    type = "split_part"
    arg1_type = [FwegoFormulaTextType]
    arg2_type = [FwegoFormulaTextType]
    arg3_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaTextType],
        arg2: FwegoExpression[FwegoFormulaTextType],
        arg3: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaTextType(
                nullable=arg1.expression_type.nullable
                or arg2.expression_type.nullable
                or arg3.expression_type.nullable
            )
        )

    def to_django_expression(
        self, arg1: Expression, arg2: Expression, arg3: Expression
    ) -> Expression:
        return Case(
            When(
                condition=(
                    LessThanEqualOrExpr(
                        arg3, Value(0), output_field=fields.BooleanField()
                    )
                ),
                then=Value(""),
            ),
            default=Func(
                arg1,
                arg2,
                trunc_numeric_to_int(arg3),
                function="SPLIT_PART",
                output_field=fields.CharField(),
            ),
            output_field=fields.CharField(),
        )


class FwegoTrunc(OneArgumentFwegoFunction):
    type = "trunc"
    arg_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(
                number_decimal_places=0, nullable=arg.expression_type.nullable
            )
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(arg, function="trunc", output_field=int_like_numeric_output_field())


def int_like_numeric_output_field() -> fields.DecimalField:
    return fields.DecimalField(
        max_digits=FwegoFormulaNumberType.MAX_DIGITS, decimal_places=0
    )


class FwegoIsNaN(OneArgumentFwegoFunction):
    type = "is_nan"
    arg_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaBooleanType(nullable=arg.expression_type.nullable)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return EqualsExpr(
            arg, Value(Decimal("NaN")), output_field=fields.BooleanField()
        )


class FwegoWhenNan(TwoArgumentFwegoFunction):
    type = "when_nan"
    arg1_type = [FwegoFormulaNumberType]
    arg2_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaNumberType],
        arg2: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            calculate_number_type([arg1.expression_type, arg2.expression_type]),
        )

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return handle_arg_being_nan(arg1, arg2, arg1)


class FwegoInt(FwegoTrunc):
    """
    Kept for backwards compatability as was introduced in v3 of formula language but
    renamed to trunc in v4.
    """

    type = "int"


def trunc_numeric_to_int(expr: Expression) -> Expression:
    return Cast(
        Func(expr, function="trunc", output_field=expr.output_field),
        output_field=fields.IntegerField(),
    )


def handle_arg_being_nan(
    arg_to_check_if_nan: Expression,
    when_nan: Expression,
    when_not_nan: Expression,
) -> Expression:
    return Case(
        When(
            condition=(
                EqualsExpr(
                    arg_to_check_if_nan,
                    Value(Decimal("Nan")),
                    output_field=fields.BooleanField(),
                )
            ),
            then=when_nan,
        ),
        default=when_not_nan,
        output_field=when_not_nan.output_field,
    )


class FwegoDivide(TwoArgumentFwegoFunction):
    type = "divide"
    operator = "/"

    arg1_type = [FwegoFormulaNumberType]
    arg2_type = [FwegoFormulaNumberType]

    @property
    def arg_types(self) -> FwegoArgumentTypeChecker:
        def type_checker(arg_index: int, arg_types: List[FwegoFormulaType]):
            if arg_index == 1:
                return arg_types[0].dividable_types
            else:
                return [FwegoFormulaValidType]

        return type_checker

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaNumberType],
        arg2: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        # Show all the decimal places we can by default if the user makes a formula
        # with a division to prevent weird results like `1/3=0`
        return arg1.expression_type.divide(func_call, arg1, arg2)

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        if isinstance(arg1.output_field, fields.DurationField):
            expression = timedelta(seconds=1) * (
                Extract(arg1, "epoch", output_field=arg2.output_field) / arg2
            )
            output_field = arg1.output_field
            safe_value = Value(None)
        else:
            # Prevent divide by zero's by swapping 0 for NaN causing the entire
            # expression to evaluate to NaN. The front-end then treats NaN values as a
            # per cell error to display to the user.
            output_field = fields.DecimalField(
                max_digits=FwegoFormulaNumberType.MAX_DIGITS,
                decimal_places=NUMBER_MAX_DECIMAL_PLACES,
            )
            expression = arg1 / Cast(arg2, output_field=output_field)
            safe_value = Value(Decimal("NaN"))
        safe_expression = Case(
            When(
                condition=(
                    EqualsExpr(arg2, Value(0), output_field=fields.BooleanField())
                ),
                then=safe_value,
            ),
            default=expression,
            output_field=output_field,
        )

        return ExpressionWrapper(safe_expression, output_field=output_field)


class FwegoHasOption(TwoArgumentFwegoFunction):
    type = "has_option"
    arg1_type = [
        FwegoFormulaMultipleSelectType,
        FwegoFormulaArrayType,
        MustBeManyExprChecker(FwegoFormulaSingleSelectType),
    ]
    arg2_type = [FwegoFormulaTextType]
    aggregate = True

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaTextType],
    ) -> FwegoExpression[FwegoFormulaType]:
        arg1_type = arg1.expression_type
        # Convert a lookup to a single select field to be a JSONArray of single
        # selects to make the `to_django_expression` work.
        if isinstance(arg1_type, FwegoFormulaSingleSelectType) and arg1.many:
            return FwegoHasOption().call_and_type_with_args(
                [FwegoArrayAggNoNesting().call_and_type_with_args([arg1]), arg2]
            )
        return func_call.with_valid_type(FwegoFormulaBooleanType())

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return EqualsExpr(
            Func(
                Func(arg1, function="jsonb_array_elements"),
                Value("value"),
                function="jsonb_extract_path_text",
                output_field=fields.CharField(),
            ),
            arg2,
            output_field=fields.BooleanField(),
        )

    def to_django_expression_given_args(
        self,
        args: List["WrappedExpressionWithMetadata"],
        context: FwegoExpressionContext,
    ) -> "WrappedExpressionWithMetadata":
        expr_with_metadata = WrappedExpressionWithMetadata.from_args(
            self.to_django_expression(args[0].expression, args[1].expression), args
        )
        subquery = construct_aggregate_wrapper_queryset(
            expr_with_metadata, context.model
        )

        # This subquery would return more than one row, but we only care if
        # there is at least one result that is true, so order by the result
        # and take the first row.
        expr: Expression = Subquery(subquery.order_by("-result")[:1])

        return WrappedExpressionWithMetadata(
            ExpressionWrapper(
                Coalesce(expr, Value(False, output_field=fields.BooleanField())),
                output_field=fields.BooleanField(),
            )
        )


class FwegoEqual(TwoArgumentFwegoFunction):
    type = "equal"
    operator = "="
    try_coerce_nullable_args_to_not_null = False

    # Overridden by the arg_types property below
    arg1_type = [FwegoFormulaValidType]
    arg2_type = [FwegoFormulaValidType]

    @property
    def arg_types(self) -> FwegoArgumentTypeChecker:
        def type_checker(arg_index: int, arg_types: List[FwegoFormulaType]):
            if arg_index == 1:
                return arg_types[0].comparable_types
            else:
                return [FwegoFormulaValidType]

        return type_checker

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        arg1_type = arg1.expression_type
        arg2_type = arg2.expression_type
        if not (type(arg1_type) is type(arg2_type)):
            # If trying to compare two types which can be compared, but are of different
            # types, then first cast them to text and then compare.
            # We to ourselves via the __class__ property here so subtypes of this type
            # use themselves here instead of us!

            return self.__class__()(
                FwegoToText()(arg1),
                FwegoToText()(arg2),
            )
        else:
            return func_call.with_valid_type(FwegoFormulaBooleanType())

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return Case(
            When(
                condition=IsNullExpr(arg1, output_field=fields.BooleanField()),
                then=IsNullExpr(arg2, output_field=fields.BooleanField()),
            ),
            default=EqualsExpr(arg1, arg2, output_field=fields.BooleanField()),
            output_field=fields.BooleanField(),
        )


class FwegoIf(ThreeArgumentFwegoFunction):
    type = "if"
    try_coerce_nullable_args_to_not_null = False

    arg1_type = [FwegoFormulaBooleanType]
    # Overridden by the type function property below
    arg2_type = [FwegoFormulaValidType]
    arg3_type = [FwegoFormulaValidType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
        arg3: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        arg2_type = arg2.expression_type
        arg3_type = arg3.expression_type
        if not (type(arg2_type) is type(arg3_type)):
            # Replace the current if func_call with one which casts both args to text
            # if they are of different types as PostgreSQL requires all cases of a case
            # statement to be of the same type.
            return FwegoIf()(
                arg1,
                FwegoToText()(arg2),
                FwegoToText()(arg3),
            )
        else:
            if isinstance(arg2_type, FwegoFormulaNumberType) and isinstance(
                arg3_type, FwegoFormulaNumberType
            ):
                resulting_type = calculate_number_type([arg2_type, arg3_type])
            else:
                resulting_type = arg2_type

            return func_call.with_valid_type(
                resulting_type,
                nullable=arg2_type.nullable or arg3_type.nullable,
            )

    def to_django_expression(
        self, arg1: Expression, arg2: Expression, arg3: Expression
    ) -> Expression:
        return Case(
            When(condition=arg1, then=arg2),
            default=arg3,
            output_field=arg2.output_field,
        )


class FwegoDurationToSeconds(OneArgumentFwegoFunction):
    type = "toseconds"
    arg_type = [FwegoFormulaDurationType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(number_decimal_places=0)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Extract(arg, "epoch", output_field=int_like_numeric_output_field())


class FwegoSecondsToDuration(OneArgumentFwegoFunction):
    type = "toduration"
    arg_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaDurationType(nullable=True))

    def to_django_expression(self, arg: Expression) -> Expression:
        return ExpressionWrapper(
            Case(
                When(
                    condition=(
                        EqualsExpr(
                            arg,
                            Value(Decimal("NaN")),
                            output_field=fields.BooleanField(),
                        )
                    ),
                    then=Value(None),
                ),
                default=timedelta(seconds=1) * arg,
                output_field=fields.DurationField(),
            ),
            output_field=fields.DurationField(),
        )


class FwegoToNumber(OneArgumentFwegoFunction):
    type = "tonumber"
    arg_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(number_decimal_places=NUMBER_MAX_DECIMAL_PLACES)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(
            arg,
            function="try_cast_to_numeric",
            output_field=int_like_numeric_output_field(),
        )


class FwegoErrorToNan(OneArgumentFwegoFunction):
    type = "error_to_nan"
    arg_type = [FwegoFormulaNumberType]
    is_wrapper = True

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(
            arg, function="replace_errors_with_nan", output_field=arg.output_field
        )


class FwegoErrorToNull(OneArgumentFwegoFunction):
    type = "error_to_null"
    arg_type = [FwegoFormulaValidType]
    is_wrapper = True

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        # FIXME: This function should set `nullable=True` on the resulting type,
        # but since this is used as the most external wrapper function, don't
        # want to loose the real nullable state of the expression. This should
        # be fixed in the future (e.g. saving only the inner expression and wrapping
        # at runtime somehow).

        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(
            arg, function="replace_errors_with_null", output_field=arg.output_field
        )


class FwegoIsBlank(OneArgumentFwegoFunction):
    type = "isblank"
    arg_type = [FwegoFormulaValidType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return arg.expression_type.is_blank(func_call, arg)

    def to_django_expression(self, arg: Expression) -> Expression:
        return EqualsExpr(
            Coalesce(
                arg,
                Value(""),
            ),
            Value(""),
            output_field=fields.BooleanField(),
        )


class FwegoIsNull(OneArgumentFwegoFunction):
    type = "is_null"
    arg_type = [FwegoFormulaValidType]
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaBooleanType())

    def to_django_expression(self, arg: Expression) -> Expression:
        return IsNullExpr(arg, output_field=fields.BooleanField())


class FwegoNot(OneArgumentFwegoFunction):
    type = "not"
    arg_type = [FwegoFormulaBooleanType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaBooleanType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaBooleanType())

    def to_django_expression(self, arg: Expression) -> Expression:
        return NotExpr(arg, output_field=fields.BooleanField())


class FwegoNotEqual(FwegoEqual):
    type = "not_equal"
    operator = "!="

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return NotEqualsExpr(
            arg1,
            arg2,
            output_field=fields.BooleanField(),
        )


class BaseLimitComparableFunction(TwoArgumentFwegoFunction, ABC):
    # Overridden by the arg_types property below
    arg1_type = [FwegoFormulaValidType]
    arg2_type = [FwegoFormulaValidType]

    @property
    def arg_types(self) -> FwegoArgumentTypeChecker:
        def type_checker(arg_index: int, arg_types: List[FwegoFormulaType]):
            if arg_index == 1:
                return arg_types[0].limit_comparable_types
            else:
                return [FwegoFormulaValidType]

        return type_checker

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaBooleanType())


class FwegoGreaterThan(BaseLimitComparableFunction):
    type = "greater_than"
    operator = ">"

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return GreaterThanExpr(
            arg1,
            arg2,
            output_field=fields.BooleanField(),
        )


class FwegoGreaterThanOrEqual(BaseLimitComparableFunction):
    type = "greater_than_or_equal"
    operator = ">="

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return GreaterThanOrEqualExpr(
            arg1,
            arg2,
            output_field=fields.BooleanField(),
        )


class FwegoLessThan(BaseLimitComparableFunction):
    type = "less_than"
    operator = "<"

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return LessThanExpr(
            arg1,
            arg2,
            output_field=fields.BooleanField(),
        )


class FwegoLessThanOrEqual(BaseLimitComparableFunction):
    type = "less_than_or_equal"
    operator = "<="

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return LessThanEqualOrExpr(
            arg1,
            arg2,
            output_field=fields.BooleanField(),
        )


class FwegoNow(ZeroArgumentFwegoFunction):
    type = "now"
    needs_periodic_update = True

    def type_function(
        self, func_call: FwegoFunctionCall[UnTyped]
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaDateType(
                date_format="ISO", date_include_time=True, date_time_format="24"
            )
        )

    def to_django_expression(self) -> Expression:
        pass

    def to_django_expression_given_args(
        self,
        args: List["WrappedExpressionWithMetadata"],
        context: FwegoExpressionContext,
    ) -> "WrappedExpressionWithMetadata":
        return WrappedExpressionWithMetadata(
            Value(context.get_utc_now(), output_field=fields.DateTimeField()),
        )


class FwegoToday(ZeroArgumentFwegoFunction):
    type = "today"
    needs_periodic_update = True

    def type_function(
        self, func_call: FwegoFunctionCall[UnTyped]
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaDateType(
                date_format="ISO",
                date_include_time=False,
                date_time_format="24",
                date_force_timezone="UTC",
            )
        )

    def to_django_expression(self) -> Expression:
        pass

    def to_django_expression_given_args(
        self,
        args: List["WrappedExpressionWithMetadata"],
        context: FwegoExpressionContext,
    ) -> "WrappedExpressionWithMetadata":
        return WrappedExpressionWithMetadata(
            Value(context.get_utc_now(), output_field=fields.DateField()),
        )


class FwegoToDate(TwoArgumentFwegoFunction):
    type = "todate"
    arg1_type = [FwegoFormulaTextType]
    arg2_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaDateType(
                date_format="ISO",
                date_include_time=False,
                date_time_format="24",
                nullable=True,
            )
        )

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return Func(
            arg1,
            arg2,
            function="try_cast_to_date",
            output_field=fields.DateTimeField(),
        )


class FwegoToDateTz(ThreeArgumentFwegoFunction):
    type = "todate_tz"
    arg1_type = [FwegoFormulaTextType]
    arg2_type = [FwegoFormulaTextType]
    arg3_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
        arg3: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaDateType(
                date_format="ISO",
                date_include_time=True,
                date_time_format="24",
                date_show_tzinfo=True,
                date_force_timezone=getattr(arg3, "literal", None),
                nullable=True,
            )
        )

    def to_django_expression(
        self, arg1: Expression, arg2: Expression, arg3: Expression
    ) -> Expression:
        return Func(
            arg1,
            arg2,
            arg3,
            function="try_cast_to_date_tz",
            output_field=fields.DateTimeField(),
        )


class FwegoDay(OneArgumentFwegoFunction):
    type = "day"
    arg_type = [FwegoFormulaDateType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(
                number_decimal_places=0, nullable=arg.expression_type.nullable
            )
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return FwegoExtract(arg, "day", output_field=int_like_numeric_output_field())


class FwegoMonth(OneArgumentFwegoFunction):
    type = "month"
    arg_type = [FwegoFormulaDateType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(
                number_decimal_places=0, nullable=arg.expression_type.nullable
            )
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return FwegoExtract(
            arg, "month", output_field=int_like_numeric_output_field()
        )


class FwegoDateDiff(ThreeArgumentFwegoFunction):
    type = "date_diff"

    arg1_type = [FwegoFormulaTextType]
    arg2_type = [FwegoFormulaDateType]
    arg3_type = [FwegoFormulaDateType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
        arg3: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        nullable = arg2.expression_type.nullable or arg3.expression_type.nullable
        return func_call.with_valid_type(
            FwegoFormulaNumberType(number_decimal_places=0, nullable=nullable)
        )

    def to_django_expression(
        self, arg1: Expression, arg2: Expression, arg3: Expression
    ) -> Expression:
        return Func(
            arg1,
            arg2,
            arg3,
            function="date_diff",
            output_field=int_like_numeric_output_field(),
        )


class FwegoAnd(TwoArgumentFwegoFunction):
    type = "and"
    operator = "&&"
    arg1_type = [FwegoFormulaBooleanType]
    arg2_type = [FwegoFormulaBooleanType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaBooleanType())

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return AndExpr(arg1, arg2, output_field=fields.BooleanField())


class FwegoOr(TwoArgumentFwegoFunction):
    type = "or"
    arg1_type = [FwegoFormulaBooleanType]
    arg2_type = [FwegoFormulaBooleanType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaBooleanType())

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return OrExpr(arg1, arg2, output_field=fields.BooleanField())


class FwegoDateInterval(OneArgumentFwegoFunction):
    type = "date_interval"
    arg_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaDurationType(nullable=True))

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(
            arg, function="try_cast_to_interval", output_field=fields.DurationField()
        )


class FwegoReplace(ThreeArgumentFwegoFunction):
    type = "replace"
    arg1_type = [FwegoFormulaTextType]
    arg2_type = [FwegoFormulaTextType]
    arg3_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
        arg3: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaTextType(nullable=False))

    def to_django_expression(
        self, arg1: Expression, arg2: Expression, arg3: Expression
    ) -> Expression:
        return Replace(arg1, arg2, arg3, output_field=fields.TextField())


class FwegoSearch(TwoArgumentFwegoFunction):
    type = "search"
    arg1_type = [FwegoFormulaTextType]
    arg2_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(number_decimal_places=0)
        )

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return StrIndex(arg1, arg2, output_field=int_like_numeric_output_field())


class FwegoContains(TwoArgumentFwegoFunction):
    type = "contains"
    arg1_type = [FwegoFormulaTextType]
    arg2_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaBooleanType())

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return NotEqualsExpr(
            StrIndex(arg1, arg2), Value(0), output_field=fields.BooleanField()
        )


class FwegoRowId(ZeroArgumentFwegoFunction):
    type = "row_id"
    requires_refresh_after_insert = True

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(number_decimal_places=0)
        )

    def to_django_expression(self) -> Expression:
        pass

    def to_django_expression_given_args(
        self,
        args: List["WrappedExpressionWithMetadata"],
        context: FwegoExpressionContext,
    ) -> "WrappedExpressionWithMetadata":
        if context.model_instance is None:
            return WrappedExpressionWithMetadata(
                ExpressionWrapper(F("id"), output_field=int_like_numeric_output_field())
            )
        else:
            # noinspection PyUnresolvedReferences
            return WrappedExpressionWithMetadata(
                Cast(
                    Value(context.model_instance.id),
                    output_field=fields.IntegerField(),
                )
            )


class FwegoLength(OneArgumentFwegoFunction):
    type = "length"
    arg_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(number_decimal_places=0)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Length(arg, output_field=int_like_numeric_output_field())


class FwegoReverse(OneArgumentFwegoFunction):
    type = "reverse"
    arg_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return Reverse(arg, output_field=fields.TextField())


class FwegoWhenEmpty(TwoArgumentFwegoFunction):
    type = "when_empty"
    arg1_type = [FwegoFormulaValidType]
    arg2_type = [FwegoFormulaValidType]
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        if not isinstance(arg1.expression_type, type(arg2.expression_type)):
            return func_call.with_invalid_type(
                "both inputs for when_empty must be the same type"
            )
        return func_call.with_valid_type(
            arg1.expression_type, nullable=arg2.expression_type.nullable
        )

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return Coalesce(arg1, arg2, output_field=arg2.output_field)


def _calculate_aggregate_orders(join_ids: JoinIdsType):
    orders = []
    for join in reversed(join_ids):
        orders.append(join[0] + "__order")
        orders.append(join[0] + "__id")
    return orders


def array_agg_expression(
    args: List["WrappedExpressionWithMetadata"],
    context: FwegoExpressionContext,
    nest_in_value: bool,
):
    pre_annotations = dict()
    aggregate_filters = []
    join_ids = []
    for child in args:
        pre_annotations.update(child.pre_annotations)
        aggregate_filters.extend(child.aggregate_filters)
        join_ids.extend(child.join_ids)

    join_ids = list(dict.fromkeys(join_ids))
    orders = _calculate_aggregate_orders(join_ids)
    if nest_in_value:
        json_builder_args = {"value": args[0].expression}
        # Remove any duplicates from join_ids
        if len(join_ids) > 1:
            json_builder_args["ids"] = JSONObject(
                **{tbl: F(i + "__id") for i, tbl in join_ids}
            )
        else:
            json_builder_args["id"] = F(join_ids[0][0] + "__id")
        expr = JSONBAgg(JSONObject(**json_builder_args), ordering=orders)
    else:
        expr = JSONBAgg(args[0].expression, ordering=orders)
    wrapped_expr = aggregate_wrapper(
        WrappedExpressionWithMetadata(
            expr, pre_annotations, aggregate_filters, join_ids
        ),
        context.model,
    ).expression
    return WrappedExpressionWithMetadata(
        Coalesce(
            wrapped_expr,
            Value([], output_field=JSONField()),
            output_field=JSONField(),
        )
    )


def string_agg_array_of_multiple_select_field(
    expr_with_metadata: WrappedExpressionWithMetadata, model, delimiter=", "
) -> WrappedExpressionWithMetadata:
    """
    This function aggregates an array of multiple select field values into a
    single string. The array is a result of a lookup operation. For every linked
    row, each select option value will be separated by the delimiter provided as
    argument.

    For example, consider a formula like `totext(lookup('link_row_field',
    'multiple_select_field'))`. This formula would call this function to
    aggregate the values. The result would be an array like:

    [{"id": $linked_row_1, "value": "option1, option2"}, ...]

    In this array of JSON objects, $linked_row_1 is the id of the linked row,
    while "option1" and "option2" are the values of the selected options in the
    multiple select field looked up.

    :param expr_with_metadata: The expression to aggregate.
    :param model: The model to aggregate on.
    :param delimiter: The delimiter to use to separate the values.
    :return: The wrapped expression with metadata needed to aggregate the get
        the expected result.
    """

    # We need to enforce that each filtered relation is not null so django generates us
    # inner joins.
    not_null_filters_for_inner_join = construct_not_null_filters_for_inner_join(
        expr_with_metadata.pre_annotations
    )
    aggregated_filters = aggregate_expr_with_metadata_filters(expr_with_metadata)

    # There is only one tuple of (field, database_table) in this case in the join_ids,
    # the one needed to join the linked table.
    join_field, _ = expr_with_metadata.join_ids[0]

    extract_value_subquery = Subquery(
        model.objects_and_trash.annotate(**expr_with_metadata.pre_annotations)
        .filter(
            id=OuterRef("id"),
            **{join_field: OuterRef(join_field)},
            **not_null_filters_for_inner_join,
        )
        .values(
            result=Func(
                Func(expr_with_metadata.expression, function="jsonb_array_elements"),
                Value("value"),
                function="jsonb_extract_path_text",
                output_field=fields.CharField(),
            )
        )
        .filter(aggregated_filters)
    )

    join_field_id = f"{join_field}__id"
    json_builder_args = {"value": F("value"), "id": F(join_field_id)}
    orders = _calculate_aggregate_orders(expr_with_metadata.join_ids)

    string_agg_values_subquery = Subquery(
        model.objects_and_trash.annotate(**expr_with_metadata.pre_annotations)
        .filter(id=OuterRef("id"), **not_null_filters_for_inner_join)
        .annotate(
            value=Func(
                Func(extract_value_subquery, function="array"),
                Value(delimiter),
                function="array_to_string",
            )
        )
        .annotate(res=JSONObject(**json_builder_args))
        .values(result=JSONBAgg(F("res"), ordering=orders))[:1],
        output_field=JSONField(),
    )

    return WrappedExpressionWithMetadata(
        ExpressionWrapper(string_agg_values_subquery, output_field=JSONField())
    )


def aggregate_multiple_selects_options(
    expr_with_metadata: WrappedExpressionWithMetadata, model
) -> WrappedExpressionWithMetadata:
    """
    This function aggregates an array of multiple select field options into a
    JSON array. The array is a result of a lookup operation. Each select option
    will be represented by a JSON object with an id, a color and a value.

    For example, consider a formula like `lookup('link_row_field',
    'multiple_select_field')`. This formula would call this function to
    aggregate the select options. The result would be an array like:

    [{
        "id": $linked_row_1,
        "value": [
            {"id": 1, "color": "red", "value": "option1"},
            {"id": 2, "color": "green", "value": "option2"},
        ]
    }, ...]

    In this array of JSON objects, $linked_row_1 is the id of the linked row,
    while the JSON objects inside the "value" array are the JSON serialized
    version of the options selected in the multiple select field looked up.

    :param expr_with_metadata: The expression to aggregate.
    :param model: The model to aggregate on.
    :param delimiter: The delimiter to use to separate the values.
    :return: The wrapped expression with metadata needed to aggregate the get
        the expected result.
    """

    # We need to enforce that each filtered relation is not null so django generates us
    # inner joins.

    not_null_filters_for_inner_join = construct_not_null_filters_for_inner_join(
        expr_with_metadata.pre_annotations
    )

    aggregated_filters = aggregate_expr_with_metadata_filters(expr_with_metadata)

    # There is only one tuple of (field, database_table) in this case in the join_ids,
    # the one needed to join the linked table.
    join_field, _ = expr_with_metadata.join_ids[0]

    inner_subquery = Subquery(
        model.objects_and_trash.annotate(**expr_with_metadata.pre_annotations)
        .filter(
            id=OuterRef("id"),
            **{join_field: OuterRef(join_field)},
            **not_null_filters_for_inner_join,
        )
        .values(result=expr_with_metadata.expression)
        .filter(aggregated_filters)
    )

    join_field_id = f"{join_field}__id"
    json_builder_args = {"value": inner_subquery, "id": F(join_field_id)}
    orders = _calculate_aggregate_orders(expr_with_metadata.join_ids)

    subquery = Subquery(
        model.objects_and_trash.annotate(**expr_with_metadata.pre_annotations)
        .filter(id=OuterRef("id"), **not_null_filters_for_inner_join)
        .annotate(res=JSONObject(**json_builder_args))
        .values(result=JSONBAgg(F("res"), ordering=orders))[:1],
        output_field=JSONField(),
    )

    return WrappedExpressionWithMetadata(
        ExpressionWrapper(
            Coalesce(subquery, Value([], output_field=JSONField())),
            output_field=JSONField(),
        )
    )


class FwegoArrayAgg(OneArgumentFwegoFunction, CollapseManyFwegoFunction):
    type = "array_agg"
    arg_type = [MustBeManyExprChecker(FwegoFormulaValidType)]
    aggregate = True

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaArrayType(arg.expression_type))

    def to_django_expression(self, arg: Expression) -> Expression:
        pass

    def to_django_expression_given_args(
        self,
        args: List["WrappedExpressionWithMetadata"],
        context: FwegoExpressionContext,
    ) -> "WrappedExpressionWithMetadata":
        return array_agg_expression(args, context, nest_in_value=True)


class FwegoArrayAggNoNesting(FwegoArrayAgg, CollapseManyFwegoFunction):
    type = "array_agg_no_nesting"

    def to_django_expression(self, arg: Expression) -> Expression:
        pass

    def to_django_expression_given_args(
        self,
        args: List["WrappedExpressionWithMetadata"],
        context: FwegoExpressionContext,
    ) -> "WrappedExpressionWithMetadata":
        return array_agg_expression(args, context, nest_in_value=False)


class FwegoMultipleSelectOptionsAgg(
    OneArgumentFwegoFunction, CollapseManyFwegoFunction
):
    type = "multiple_select_options_agg"
    arg_type = [MustBeManyExprChecker(FwegoFormulaMultipleSelectType)]
    aggregate = True

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaArrayType(arg.expression_type))

    def to_django_expression(self, arg: Expression) -> Expression:
        return arg

    def to_django_expression_given_args(
        self,
        args: List["WrappedExpressionWithMetadata"],
        context: FwegoExpressionContext,
    ) -> "WrappedExpressionWithMetadata":
        expr = aggregate_multiple_selects_options(args[0], context.model)
        return super().to_django_expression_given_args([expr], context)


class Fwego2dArrayAgg(OneArgumentFwegoFunction, CollapseManyFwegoFunction):
    type = "array_agg_unnesting"
    arg_type = [MustBeManyExprChecker(FwegoFormulaArrayType)]
    aggregate = True

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(
            Func(JSONBAgg(arg), function="jsonb_array_elements"),
            function="jsonb_array_elements",
            output_field=JSONField(),
        )

    def to_django_expression_given_args(
        self,
        args: List["WrappedExpressionWithMetadata"],
        context: FwegoExpressionContext,
    ) -> "WrappedExpressionWithMetadata":
        subquery = super().to_django_expression_given_args(args, context)
        return WrappedExpressionWithMetadata(
            Func(Func(subquery.expression, function="array"), function="to_jsonb")
        )


class FwegoMultipleSelectCount(OneArgumentFwegoFunction):
    type = "multiple_select_count"
    arg_type = [FwegoFormulaMultipleSelectType]
    aggregate = True

    def can_accept_arg(self, arg):
        return isinstance(arg.expression_type, FwegoFormulaMultipleSelectType)

    def type_function(
        self,
        func_call: FwegoFunctionCall,
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(number_decimal_places=0)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(arg, function="jsonb_array_elements")

    def to_django_expression_given_args(
        self,
        args: List["WrappedExpressionWithMetadata"],
        context: FwegoExpressionContext,
    ) -> "WrappedExpressionWithMetadata":
        subquery = super().to_django_expression_given_args(args, context)
        return WrappedExpressionWithMetadata(
            Coalesce(
                Func(
                    Func(subquery.expression, function="array"),
                    Value(1),
                    function="array_length",
                    output_field=fields.IntegerField(),
                ),
                Value(0),
                output_field=fields.IntegerField(),
            )
        )


class FwegoStringAggMultipleSelectValues(OneArgumentFwegoFunction):
    type = "string_agg_multiple_select_values"
    arg_type = [FwegoFormulaMultipleSelectType]
    aggregate = True

    def type_function(
        self,
        func_call: FwegoFunctionCall,
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaTextType())

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(
            Func(arg, function="jsonb_array_elements"),
            Value("value"),
            function="jsonb_extract_path_text",
            output_field=fields.TextField(),
        )

    def to_django_expression_given_args(
        self,
        args: List["WrappedExpressionWithMetadata"],
        context: FwegoExpressionContext,
    ) -> "WrappedExpressionWithMetadata":
        subquery = super().to_django_expression_given_args(args, context)
        return WrappedExpressionWithMetadata(
            Func(
                Func(subquery.expression, function="array"),
                Value(", "),
                function="array_to_string",
            )
        )


class FwegoStringAggArrayOfMultipleSelectValues(OneArgumentFwegoFunction):
    type = "string_agg_array_of_multiple_select_values"
    arg_type = [MustBeManyExprChecker(FwegoFormulaMultipleSelectType)]
    aggregate = True

    def type_function(
        self,
        func_call: FwegoFunctionCall,
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaArrayType(FwegoFormulaTextType())
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return arg

    def to_django_expression_given_args(
        self,
        args: List["WrappedExpressionWithMetadata"],
        context: FwegoExpressionContext,
    ) -> "WrappedExpressionWithMetadata":
        expr = string_agg_array_of_multiple_select_field(args[0], context.model)
        return super().to_django_expression_given_args([expr], context)


class FwegoCount(OneArgumentFwegoFunction):
    type = "count"
    arg_type = [
        MustBeManyExprChecker(FwegoFormulaValidType),
        FwegoFormulaMultipleSelectType,
    ]
    aggregate = True
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        if FwegoGetFileCount().can_accept_arg(arg):
            return FwegoGetFileCount()(arg)

        return arg.expression_type.count(func_call, arg).with_valid_type(
            FwegoFormulaNumberType(number_decimal_places=0)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Count(arg, output_field=int_like_numeric_output_field())


class FwegoGetFileCount(OneArgumentFwegoFunction):
    type = "get_file_count"
    arg_type = [FwegoFormulaArrayType]

    def can_accept_arg(self, arg):
        return isinstance(arg.expression_type, FwegoFormulaArrayType) and isinstance(
            arg.expression_type.sub_type, FwegoFormulaSingleFileType
        )

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        if not self.can_accept_arg(arg):
            return func_call.with_invalid_type("can only count file fields")
        else:
            return func_call.with_valid_type(
                FwegoFormulaNumberType(number_decimal_places=0)
            )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(
            arg, function="jsonb_array_length", output_field=fields.IntegerField()
        )


class FwegoFilter(TwoArgumentFwegoFunction):
    type = "filter"
    arg1_type = [FwegoFormulaValidType]
    arg2_type = [FwegoFormulaBooleanType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        if not arg1.many:
            return func_call.with_invalid_type(
                "first input to filter must be an expression of many values ("
                "a lookup function call or a field reference to a lookup/link "
                "field)"
            )
        valid_type = func_call.with_valid_type(arg1.expression_type)
        # Force all usages of filter to be immediately wrapped by an aggregate call
        # otherwise formula behaviour when filtering is odd.
        valid_type.requires_aggregate_wrapper = True
        return valid_type

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return arg1

    def to_django_expression_given_args(
        self,
        args: List["WrappedExpressionWithMetadata"],
        context: FwegoExpressionContext,
    ) -> "WrappedExpressionWithMetadata":
        result = super().to_django_expression_given_args(args, context)
        return WrappedExpressionWithMetadata(
            result.expression,
            result.pre_annotations,
            result.aggregate_filters + [args[1].expression],
            result.join_ids,
        )


def _to_django_aggregate_number_or_duration_expression(
    func: Expression, arg: Expression, **func_kwargs
):
    """
    An utility function to create an aggregate expression for a number or duration
    field.

    :param func: The aggregate function to use.
    :param arg: The expression to aggregate.
    :param func_kwargs: Additional keyword arguments to pass to the aggregate function.
    :return: The aggregate expression.
    """

    if isinstance(arg.output_field, fields.DurationField):
        expr = func(Extract(arg, "epoch"), **func_kwargs) * timedelta(seconds=1)
    else:
        expr = func(arg, **func_kwargs)
    return ExpressionWrapper(expr, output_field=arg.output_field)


class FwegoAny(OneArgumentFwegoFunction):
    type = "any"
    arg_type = [MustBeManyExprChecker(FwegoFormulaBooleanType)]
    aggregate = True

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(arg, function="bool_or", output_field=fields.BooleanField())


class FwegoEvery(OneArgumentFwegoFunction):
    type = "every"
    arg_type = [MustBeManyExprChecker(FwegoFormulaBooleanType)]
    aggregate = True

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(arg, function="every", output_field=fields.BooleanField())


class FwegoMax(OneArgumentFwegoFunction):
    type = "max"
    arg_type = [
        MustBeManyExprChecker(
            FwegoFormulaTextType,
            FwegoFormulaNumberType,
            FwegoFormulaCharType,
            FwegoFormulaDateType,
            FwegoFormulaDurationType,
        ),
    ]
    aggregate = True
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return _to_django_aggregate_number_or_duration_expression(Max, arg)


class FwegoMin(OneArgumentFwegoFunction):
    type = "min"
    arg_type = [
        MustBeManyExprChecker(
            FwegoFormulaTextType,
            FwegoFormulaNumberType,
            FwegoFormulaCharType,
            FwegoFormulaDateType,
            FwegoFormulaDurationType,
        ),
    ]
    aggregate = True
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return _to_django_aggregate_number_or_duration_expression(Min, arg)


class FwegoAvg(OneArgumentFwegoFunction):
    type = "avg"
    arg_type = [
        MustBeManyExprChecker(FwegoFormulaNumberType, FwegoFormulaDurationType),
    ]
    aggregate = True
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return _to_django_aggregate_number_or_duration_expression(Avg, arg)


class FwegoStdDevPop(OneArgumentFwegoFunction):
    type = "stddev_pop"
    arg_type = [
        MustBeManyExprChecker(FwegoFormulaNumberType, FwegoFormulaDurationType)
    ]
    aggregate = True
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return _to_django_aggregate_number_or_duration_expression(
            StdDev, arg, sample=False
        )


class FwegoStdDevSample(OneArgumentFwegoFunction):
    type = "stddev_sample"
    arg_type = [
        MustBeManyExprChecker(FwegoFormulaNumberType, FwegoFormulaDurationType)
    ]
    aggregate = True
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return _to_django_aggregate_number_or_duration_expression(
            StdDev, arg, sample=True
        )


class FwegoAggJoin(TwoArgumentFwegoFunction):
    type = "join"
    arg1_type = [MustBeManyExprChecker(FwegoFormulaTextType)]
    arg2_type = [FwegoFormulaTextType]
    aggregate = True

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaTextType())

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        pass

    def to_django_expression_given_args(
        self,
        args: List["WrappedExpressionWithMetadata"],
        context: FwegoExpressionContext,
    ) -> "WrappedExpressionWithMetadata":
        pre_annotations = {}
        aggregate_filters = []
        join_ids = []
        for child in args:
            pre_annotations.update(child.pre_annotations)
            aggregate_filters.extend(child.aggregate_filters)
            join_ids.extend(child.join_ids)

        # Remove any duplicates from join_ids
        join_ids = list(dict.fromkeys(join_ids))
        orders = _calculate_aggregate_orders(join_ids)
        return aggregate_wrapper(
            WrappedExpressionWithMetadata(
                FwegoStringAgg(
                    args[0].expression,
                    args[1].expression,
                    ordering=orders,
                    output_field=fields.TextField(),
                ),
                pre_annotations,
                aggregate_filters,
                join_ids,
            ),
            context.model,
        )


class FwegoSum(OneArgumentFwegoFunction):
    type = "sum"
    aggregate = True
    arg_type = [
        MustBeManyExprChecker(FwegoFormulaNumberType, FwegoFormulaDurationType),
    ]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return _to_django_aggregate_number_or_duration_expression(Sum, arg)


class FwegoVarianceSample(OneArgumentFwegoFunction):
    type = "variance_sample"
    aggregate = True
    arg_type = [
        MustBeManyExprChecker(FwegoFormulaNumberType, FwegoFormulaDurationType)
    ]
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return _to_django_aggregate_number_or_duration_expression(
            Variance, arg, sample=True
        )


class FwegoVariancePop(OneArgumentFwegoFunction):
    type = "variance_pop"
    aggregate = True
    arg_type = [
        MustBeManyExprChecker(FwegoFormulaNumberType, FwegoFormulaDurationType)
    ]
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type)

    def to_django_expression(self, arg: Expression) -> Expression:
        return _to_django_aggregate_number_or_duration_expression(
            Variance, arg, sample=False
        )


class FwegoGetSingleSelectValue(OneArgumentFwegoFunction):
    type = "get_single_select_value"
    arg_type = [FwegoFormulaSingleSelectType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaTextType(nullable=arg.expression_type.nullable)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(
            arg,
            Value("value"),
            function="jsonb_extract_path_text",
            output_field=fields.TextField(),
        )


class FwegoIndex(TwoArgumentFwegoFunction):
    arg1_type = [FwegoFormulaArrayType]
    arg2_type = [FwegoFormulaNumberType]

    type = "index"

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        if not isinstance(arg1.expression_type.sub_type, FwegoFormulaSingleFileType):
            return func_call.with_invalid_type(
                "index only currently supports indexing file fields."
            )
        else:
            if arg1.many:
                arg1 = arg1.expression_type.collapse_many(arg1)
            return func_call.with_args([arg1, arg2]).with_valid_type(
                arg1.expression_type.sub_type
            )

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return Func(
            arg1,
            Cast(arg2, fields.TextField()),
            function="jsonb_extract_path",
            output_field=JSONField(),
        )


class FwegoJsonbExtractPathText(FwegoFunctionDefinition):
    type = "jsonb_extract_path_text"
    num_args = NumOfArgsGreaterThan(1)

    @property
    def arg_types(self) -> FwegoArgumentTypeChecker:
        def type_checker(arg_index: int, arg_types: List[FwegoFormulaType]):
            if arg_index == 0:
                return [FwegoJSONBObjectBaseType]
            else:
                return [FwegoFormulaTextType]

        return type_checker

    def type_function_given_valid_args(
        self,
        args: List[FwegoExpression[FwegoFormulaValidType]],
        expression: "FwegoFunctionCall[UnTyped]",
    ) -> FwegoExpression[FwegoFormulaType]:
        return expression.with_valid_type(FwegoFormulaTextType(nullable=True))

    def to_django_expression_given_args(
        self, expr_args: List[WrappedExpressionWithMetadata], *args, **kwargs
    ) -> WrappedExpressionWithMetadata:
        return WrappedExpressionWithMetadata(
            Func(
                *[e.expression for e in expr_args],
                function="jsonb_extract_path_text",
                output_field=fields.TextField(),
            )
        )

    def __call__(
        self,
        arg: FwegoExpression[FwegoJSONBObjectBaseType],
        *path: FwegoExpression[FwegoFormulaTextType],
    ) -> FwegoFunctionCall[FwegoFormulaTextType]:
        return self.call_and_type_with_args([arg, *path])


class FwegoGetFileVisibleName(OneArgumentFwegoFunction):
    type = "get_file_visible_name"
    arg_type = [FwegoFormulaSingleFileType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaSingleFileType],
    ) -> FwegoExpression[FwegoFormulaTextType]:
        return FwegoJsonbExtractPathText()(arg, literal("visible_name"))

    def to_django_expression(self, arg: Expression) -> Expression:
        return arg


class FwegoGetFileMimeType(OneArgumentFwegoFunction):
    type = "get_file_mime_type"
    arg_type = [FwegoFormulaSingleFileType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaSingleFileType],
    ) -> FwegoExpression[FwegoFormulaTextType]:
        return FwegoJsonbExtractPathText()(arg, literal("mime_type"))

    def to_django_expression(self, arg: Expression) -> Expression:
        return arg


class FwegoGetFileSize(OneArgumentFwegoFunction):
    type = "get_file_size"
    arg_type = [FwegoFormulaSingleFileType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaSingleFileType],
    ) -> FwegoExpression[FwegoFormulaNumberType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(
                nullable=arg.expression_type.nullable, number_decimal_places=0
            )
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Cast(
            Func(
                arg,
                Value("size"),
                function="jsonb_extract_path_text",
                output_field=fields.IntegerField(),
            ),
            output_field=fields.IntegerField(),
        )


class FwegoGetImageWidth(OneArgumentFwegoFunction):
    type = "get_image_width"
    arg_type = [FwegoFormulaSingleFileType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaSingleFileType],
    ) -> FwegoExpression[FwegoFormulaNumberType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(nullable=True, number_decimal_places=0)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Cast(
            Func(
                arg,
                Value("image_width"),
                function="jsonb_extract_path_text",
                output_field=fields.IntegerField(),
            ),
            output_field=fields.IntegerField(),
        )


class FwegoGetImageHeight(OneArgumentFwegoFunction):
    type = "get_image_height"
    arg_type = [FwegoFormulaSingleFileType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaSingleFileType],
    ) -> FwegoExpression[FwegoFormulaNumberType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(nullable=True, number_decimal_places=0)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Cast(
            Func(
                arg,
                Value("image_height"),
                function="jsonb_extract_path_text",
                output_field=fields.IntegerField(),
            ),
            output_field=fields.IntegerField(),
        )


class FwegoIsImage(OneArgumentFwegoFunction):
    type = "is_image"
    arg_type = [FwegoFormulaSingleFileType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaSingleFileType],
    ) -> FwegoExpression[FwegoFormulaBooleanType]:
        return func_call.with_valid_type(
            FwegoFormulaBooleanType(nullable=arg.expression_type.nullable)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Coalesce(
            Cast(
                Func(
                    arg,
                    Value("is_image"),
                    function="jsonb_extract_path_text",
                    output_field=fields.BooleanField(),
                ),
                output_field=fields.BooleanField(),
            ),
            Value(False),
            output_field=fields.BooleanField(),
        )


class FwegoGetLinkUrl(OneArgumentFwegoFunction):
    type = "get_link_url"
    arg_type = [FwegoFormulaLinkType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaTextType(nullable=arg.expression_type.nullable)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(
            arg,
            Value("url"),
            function="jsonb_extract_path_text",
            output_field=fields.TextField(),
        )


class FwegoGetLinkLabel(OneArgumentFwegoFunction):
    type = "get_link_label"
    arg_type = [FwegoFormulaLinkType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaTextType(nullable=arg.expression_type.nullable)
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(
            arg,
            Value("label"),
            function="jsonb_extract_path_text",
            output_field=fields.TextField(),
        )


class FwegoLeft(TwoArgumentFwegoFunction):
    type = "left"
    arg1_type = [FwegoFormulaTextType]
    arg2_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg1.expression_type, nullable=True)

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return handle_arg_being_nan(
            arg_to_check_if_nan=arg2,
            when_nan=Value(None),
            when_not_nan=(
                Left(arg1, trunc_numeric_to_int(arg2), output_field=fields.TextField())
            ),
        )


class FwegoRight(TwoArgumentFwegoFunction):
    type = "right"
    arg1_type = [FwegoFormulaTextType]
    arg2_type = [FwegoFormulaNumberType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaNumberType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg1.expression_type, nullable=True)

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return handle_arg_being_nan(
            arg_to_check_if_nan=arg2,
            when_nan=Value(None),
            when_not_nan=(
                Right(
                    arg1,
                    trunc_numeric_to_int(arg2),
                    output_field=fields.TextField(),
                )
            ),
        )


class FwegoRegexReplace(ThreeArgumentFwegoFunction):
    type = "regex_replace"
    arg1_type = [FwegoFormulaTextType]
    arg2_type = [FwegoFormulaTextType]
    arg3_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
        arg3: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg1.expression_type)

    def to_django_expression(
        self, arg1: Expression, arg2: Expression, arg3: Expression
    ) -> Expression:
        return Func(
            arg1,
            arg2,
            arg3,
            Value("g", output_field=fields.TextField()),
            function="regexp_replace",
            output_field=fields.TextField(),
        )


class FwegoLink(FwegoFunctionDefinition):
    type = "link"
    num_args = NumOfArgsBetween(1, 2, inclusive=True)
    try_coerce_nullable_args_to_not_null = False

    @property
    def arg_types(self) -> FwegoArgumentTypeChecker:
        return lambda _, _2: [FwegoFormulaTextType]

    def type_function_given_valid_args(
        self,
        args: List[FwegoExpression[FwegoFormulaValidType]],
        expression: "FwegoFunctionCall[UnTyped]",
    ) -> FwegoExpression[FwegoFormulaType]:
        typed_args = [FwegoToText()(a) for a in args]
        return expression.with_args(typed_args).with_valid_type(
            FwegoFormulaLinkType(nullable=args[0].expression_type.nullable)
        )

    def to_django_expression_given_args(
        self, expr_args: List[WrappedExpressionWithMetadata], *args, **kwargs
    ) -> WrappedExpressionWithMetadata:
        url_kwargs = {"url": expr_args[0].expression}
        if len(expr_args) > 1:
            url_kwargs["label"] = expr_args[1].expression
        expr = JSONObject(**url_kwargs)
        return WrappedExpressionWithMetadata.from_args(
            ExpressionWrapper(expr, output_field=JSONField()),
            expr_args,
        )


class FwegoButton(TwoArgumentFwegoFunction):
    type = "button"
    arg1_type = [FwegoFormulaTextType]
    arg2_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg1: FwegoExpression[FwegoFormulaValidType],
        arg2: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaButtonType(nullable=arg1.expression_type.nullable)
        )

    def to_django_expression(self, arg1: Expression, arg2: Expression) -> Expression:
        return JSONObject(url=arg1, label=arg2)


class FwegoTrim(OneArgumentFwegoFunction):
    type = "trim"
    arg_type = [FwegoFormulaTextType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return FwegoRegexReplace()(arg, literal("(^\\s+|\\s+$)"), literal(""))

    def to_django_expression(self, arg: Expression) -> Expression:
        # This function should always be completely substituted when typing and replaced
        # with FwegoRegexReplace and hence this should never be called.
        raise FwegoToDjangoExpressionGenerationError()


class FwegoYear(OneArgumentFwegoFunction):
    type = "year"
    arg_type = [FwegoFormulaDateType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(
            FwegoFormulaNumberType(
                number_decimal_places=0, nullable=arg.expression_type.nullable
            )
        )

    def to_django_expression(self, arg: Expression) -> Expression:
        return FwegoExtract(arg, "year", output_field=int_like_numeric_output_field())


class FwegoSecond(OneArgumentFwegoFunction):
    type = "second"
    arg_type = [FwegoFormulaDateType]

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaDateType],
    ) -> FwegoExpression[FwegoFormulaType]:
        if not arg.expression_type.date_include_time:
            return func_call.with_invalid_type(
                "cannot extract seconds from a date without time"
            )
        else:
            return func_call.with_valid_type(
                FwegoFormulaNumberType(
                    number_decimal_places=0, nullable=arg.expression_type.nullable
                )
            )

    def to_django_expression(self, arg: Expression) -> Expression:
        return FwegoExtract(
            arg, "second", output_field=int_like_numeric_output_field()
        )


class FwegoBcToNull(OneArgumentFwegoFunction):
    type = "bc_to_null"
    arg_type = [FwegoFormulaDateType]
    is_wrapper = True

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(arg.expression_type, nullable=True)

    def to_django_expression(self, arg: Expression) -> Expression:
        expr_to_get_year = FwegoExtract(
            arg, "year", output_field=int_like_numeric_output_field()
        )
        return Case(
            When(
                condition=LessThanExpr(
                    expr_to_get_year, Value(0), output_field=fields.BooleanField()
                ),
                then=Value(None, output_field=arg.output_field),
            ),
            default=arg,
        )


class FwegoToURL(OneArgumentFwegoFunction):
    type = "tourl"
    arg_type = [FwegoFormulaTextType]
    try_coerce_nullable_args_to_not_null = False

    def type_function(
        self,
        func_call: FwegoFunctionCall[UnTyped],
        arg: FwegoExpression[FwegoFormulaValidType],
    ) -> FwegoExpression[FwegoFormulaType]:
        return func_call.with_valid_type(FwegoFormulaURLType())

    def to_django_expression(self, arg: Expression) -> Expression:
        return Func(arg, function="try_cast_to_url", output_field=fields.CharField())
