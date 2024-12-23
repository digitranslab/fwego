from rest_framework import serializers

from fwego.api.applications.serializers import ApplicationSerializer
from fwego.contrib.database.api.fields.serializers import PolymorphicFieldSerializer
from fwego.contrib.database.api.tables.serializers import TableSerializer
from fwego.contrib.database.views.models import View


class LocalFwegoViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = ("id", "table_id", "name")


class TableSerializerWithFields(TableSerializer):
    fields = PolymorphicFieldSerializer(many=True, help_text="Fields of this table")

    class Meta(TableSerializer.Meta):
        fields = ("id", "name", "order", "database_id", "fields")


class LocalFwegoDatabaseSerializer(ApplicationSerializer):
    tables = TableSerializerWithFields(
        many=True,
        help_text="This field is specific to the `database` application and contains "
        "an array of tables that are in the database.",
    )
    views = LocalFwegoViewSerializer(
        many=True,
        help_text="This field is specific to the `database` application and contains "
        "an array of views that are in the tables.",
    )

    class Meta(ApplicationSerializer.Meta):
        ref_name = "LocalFwegoDatabaseApplication"
        fields = ApplicationSerializer.Meta.fields + ("tables", "views")


class LocalFwegoContextDataSerializer(serializers.Serializer):
    databases = LocalFwegoDatabaseSerializer(many=True)
