from rest_framework import serializers

from fwego.contrib.integrations.local_fwego.models import (
    LocalFwegoTableServiceFilter,
    LocalFwegoTableServiceSort,
)
from fwego.core.formula.serializers import (
    FormulaSerializerField,
    OptionalFormulaSerializerField,
)


class LocalFwegoTableServiceSortSerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(read_only=True)

    class Meta:
        model = LocalFwegoTableServiceSort
        fields = ("id", "field", "order", "order_by")


class LocalFwegoTableServiceFilterSerializer(serializers.ModelSerializer):
    value = OptionalFormulaSerializerField(
        allow_blank=True,
        help_text="A formula for the filter's value.",
        is_formula_field_name="value_is_formula",
    )
    value_is_formula = serializers.BooleanField(
        default=False, help_text="Indicates whether the value is a formula or not."
    )
    order = serializers.IntegerField(read_only=True)

    class Meta:
        model = LocalFwegoTableServiceFilter
        fields = ("id", "order", "field", "type", "value", "value_is_formula")


class LocalFwegoTableServiceFieldMappingSerializer(serializers.Serializer):
    field_id = serializers.IntegerField(
        help_text="The primary key of the associated database table field."
    )
    enabled = serializers.BooleanField(
        help_text="Indicates whether the field mapping is enabled or not."
    )
    value = FormulaSerializerField(allow_blank=True)
