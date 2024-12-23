from fwego.contrib.database.fields.field_types import (
    AutonumberFieldType,
    BooleanFieldType,
    CreatedByFieldType,
    CreatedOnFieldType,
    DateFieldType,
    DurationFieldType,
    EmailFieldType,
    FileFieldType,
    FormulaFieldType,
    LastModifiedByFieldType,
    LastModifiedFieldType,
    LinkRowFieldType,
    LongTextFieldType,
    MultipleSelectFieldType,
    NumberFieldType,
    PasswordFieldType,
    PhoneNumberFieldType,
    RatingFieldType,
    SingleSelectFieldType,
    TextFieldType,
    URLFieldType,
)
from fwego.contrib.database.fields.registries import FieldAggregationType
from fwego.contrib.database.formula import (
    FwegoFormulaBooleanType,
    FwegoFormulaCharType,
    FwegoFormulaDateType,
    FwegoFormulaNumberType,
    FwegoFormulaTextType,
)
from fwego.contrib.database.formula.types.formula_types import (
    FwegoFormulaSingleFileType,
)
from fwego.contrib.database.views.view_aggregations import (
    AverageViewAggregationType,
    EmptyCountViewAggregationType,
    MaxViewAggregationType,
    MedianViewAggregationType,
    MinViewAggregationType,
    NotEmptyCountViewAggregationType,
    StdDevViewAggregationType,
    SumViewAggregationType,
    UniqueCountViewAggregationType,
    VarianceViewAggregationType,
)


class EmptyCountFieldAggregationType(FieldAggregationType):
    """
    Empty count aggregation.
    """

    type = "empty_count"
    raw_type = EmptyCountViewAggregationType
    compatible_field_types = raw_type.compatible_field_types


class NotEmptyCountFieldAggregationType(FieldAggregationType):
    """
    Not empty count aggregation.
    """

    type = "not_empty_count"
    raw_type = NotEmptyCountViewAggregationType
    compatible_field_types = raw_type.compatible_field_types


class CheckedFieldAggregationType(FieldAggregationType):
    """
    Checked count aggregation.
    """

    type = "checked_count"
    raw_type = NotEmptyCountViewAggregationType
    compatible_field_types = [
        BooleanFieldType.type,
        FormulaFieldType.compatible_with_formula_types(
            FwegoFormulaBooleanType.type,
        ),
    ]


class NotCheckedFieldAggregationType(FieldAggregationType):
    """
    Not checked count aggregation.
    """

    type = "not_checked_count"
    raw_type = EmptyCountViewAggregationType
    compatible_field_types = [
        BooleanFieldType.type,
        FormulaFieldType.compatible_with_formula_types(
            FwegoFormulaBooleanType.type,
        ),
    ]


class EmptyPercentageFieldAggregationType(FieldAggregationType):
    """
    Empty percentage aggregation.
    """

    type = "empty_percentage"
    raw_type = EmptyCountViewAggregationType
    with_total = True
    compatible_field_types = [
        TextFieldType.type,
        LongTextFieldType.type,
        URLFieldType.type,
        NumberFieldType.type,
        RatingFieldType.type,
        DateFieldType.type,
        DurationFieldType.type,
        LastModifiedFieldType.type,
        LastModifiedByFieldType.type,
        CreatedOnFieldType.type,
        CreatedByFieldType.type,
        LinkRowFieldType.type,
        EmailFieldType.type,
        FileFieldType.type,
        PhoneNumberFieldType.type,
        SingleSelectFieldType.type,
        MultipleSelectFieldType.type,
        PasswordFieldType.type,
        FormulaFieldType.compatible_with_formula_types(
            FwegoFormulaTextType.type,
            FwegoFormulaCharType.type,
            FwegoFormulaNumberType.type,
            FwegoFormulaDateType.type,
            FormulaFieldType.array_of(FwegoFormulaSingleFileType.type),
        ),
    ]


class NotEmptyPercentageFieldAggregationType(FieldAggregationType):
    """
    Not empty percentage aggregation.
    """

    type = "not_empty_percentage"
    raw_type = NotEmptyCountViewAggregationType
    with_total = True
    compatible_field_types = [
        TextFieldType.type,
        LongTextFieldType.type,
        URLFieldType.type,
        NumberFieldType.type,
        RatingFieldType.type,
        DateFieldType.type,
        DurationFieldType.type,
        LastModifiedFieldType.type,
        LastModifiedByFieldType.type,
        CreatedOnFieldType.type,
        CreatedByFieldType.type,
        LinkRowFieldType.type,
        EmailFieldType.type,
        FileFieldType.type,
        PhoneNumberFieldType.type,
        SingleSelectFieldType.type,
        MultipleSelectFieldType.type,
        PasswordFieldType.type,
        FormulaFieldType.compatible_with_formula_types(
            FwegoFormulaTextType.type,
            FwegoFormulaCharType.type,
            FwegoFormulaNumberType.type,
            FwegoFormulaDateType.type,
            FormulaFieldType.array_of(FwegoFormulaSingleFileType.type),
        ),
    ]


class CheckedPercentageFieldAggregationType(FieldAggregationType):
    """
    Checked percentage aggregation.
    """

    type = "checked_percentage"
    raw_type = NotEmptyCountViewAggregationType
    with_total = True
    compatible_field_types = [
        BooleanFieldType.type,
        FormulaFieldType.compatible_with_formula_types(
            FwegoFormulaBooleanType.type,
        ),
    ]


class NotCheckedPercentageFieldAggregationType(FieldAggregationType):
    """
    Not checked percentage aggregation.
    """

    type = "not_checked_percentage"
    raw_type = EmptyCountViewAggregationType
    with_total = True
    compatible_field_types = [
        BooleanFieldType.type,
        FormulaFieldType.compatible_with_formula_types(
            FwegoFormulaBooleanType.type,
        ),
    ]


class UniqueCountFieldAggregationType(FieldAggregationType):
    """
    Unique count aggregation.
    """

    type = "unique_count"
    raw_type = UniqueCountViewAggregationType
    compatible_field_types = raw_type.compatible_field_types


class MinFieldAggregationType(FieldAggregationType):
    """
    Min aggregation.
    """

    type = "min"
    raw_type = MinViewAggregationType
    compatible_field_types = [
        NumberFieldType.type,
        RatingFieldType.type,
        AutonumberFieldType.type,
        DurationFieldType.type,
        FormulaFieldType.compatible_with_formula_types(
            FwegoFormulaNumberType.type,
        ),
    ]


class MaxFieldAggregationType(FieldAggregationType):
    """
    Max aggregation.
    """

    type = "max"
    raw_type = MaxViewAggregationType
    compatible_field_types = [
        NumberFieldType.type,
        RatingFieldType.type,
        AutonumberFieldType.type,
        DurationFieldType.type,
        FormulaFieldType.compatible_with_formula_types(
            FwegoFormulaNumberType.type,
        ),
    ]


class EarliestDateFieldAggregationType(FieldAggregationType):
    """
    Earliest date aggregation.
    """

    type = "min_date"
    raw_type = MinViewAggregationType
    compatible_field_types = [
        DateFieldType.type,
        LastModifiedFieldType.type,
        CreatedOnFieldType.type,
        FormulaFieldType.compatible_with_formula_types(
            FwegoFormulaDateType.type,
        ),
    ]


class LatestDateFieldAggregationType(FieldAggregationType):
    """
    Latest date aggregation.
    """

    type = "max_date"
    raw_type = MaxViewAggregationType
    compatible_field_types = [
        DateFieldType.type,
        LastModifiedFieldType.type,
        CreatedOnFieldType.type,
        FormulaFieldType.compatible_with_formula_types(
            FwegoFormulaDateType.type,
        ),
    ]


class SumFieldAggregationType(FieldAggregationType):
    """
    Sum aggregation.
    """

    type = "sum"
    raw_type = SumViewAggregationType
    compatible_field_types = raw_type.compatible_field_types


class AverageFieldAggregationType(FieldAggregationType):
    """
    Average aggregation.
    """

    type = "average"
    raw_type = AverageViewAggregationType
    compatible_field_types = raw_type.compatible_field_types


class StdDevFieldAggregationType(FieldAggregationType):
    """
    Standard deviation aggregation.
    """

    type = "std_dev"
    raw_type = StdDevViewAggregationType
    compatible_field_types = raw_type.compatible_field_types


class VarianceFieldAggregationType(FieldAggregationType):
    """
    Variance deviation aggregation.
    """

    type = "variance"
    raw_type = VarianceViewAggregationType
    compatible_field_types = raw_type.compatible_field_types


class MedianFieldAggregationType(FieldAggregationType):
    """
    Median deviation aggregation.
    """

    type = "median"
    raw_type = MedianViewAggregationType
    compatible_field_types = raw_type.compatible_field_types
