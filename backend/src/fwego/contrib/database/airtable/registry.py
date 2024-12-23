from datetime import tzinfo
from typing import Any, Dict, Tuple, Union

from fwego.contrib.database.fields.models import Field
from fwego.core.registry import Instance, Registry


class AirtableColumnType(Instance):
    def to_fwego_field(
        self, raw_airtable_table: dict, raw_airtable_column: dict, timezone: tzinfo
    ) -> Union[Field, None]:
        """
        Converts the raw Airtable column to a Fwego field object. It should be
        possible to pass this object directly into the FieldType::export_serialized
        method to convert it to the Fwego export format.

        :param raw_airtable_table: The raw Airtable table data related to the column.
        :param raw_airtable_column: The raw Airtable column values that must be
            converted.
        :param timezone: The main timezone used for date conversions if needed.
        :return: The Fwego field type related to the Airtable column. If None is
            provided, then the column is ignored in the conversion.
        """

        raise NotImplementedError("The `to_fwego_field` must be implemented.")

    def to_fwego_export_serialized_value(
        self,
        row_id_mapping: Dict[str, Dict[str, int]],
        raw_airtable_column: dict,
        fwego_field: Field,
        value: Any,
        files_to_download: Dict[str, str],
    ):
        """
        This method should convert a raw Airtable row value to a Fwego export row
        value. This method is only called if the Airtable field is compatible with a
        Fwego field type, this is determined by the
        `from_airtable_field_to_serialized` method.

        :param row_id_mapping: A mapping containing the table as key as the value is
            another mapping where the Airtable row id maps the Fwego row id.
        :param raw_airtable_column: A dict containing the raw Airtable column values.
        :param fwego_field: The Fwego field that the column has been converted to.
        :param value: The raw Airtable value that must be converted.
        :param files_to_download: A dict that contains all the user file URLs that must
            be downloaded. The key is the file name and the value the URL. Additional
            files can be added to this dict.
        :return: The converted value is Fwego export format.
        """

        return value


class AirtableColumnTypeRegistry(Registry):
    name = "airtable_column"

    def from_airtable_column_to_serialized(
        self, raw_airtable_table: dict, raw_airtable_column: dict
    ) -> Union[Tuple[Field, AirtableColumnType], Tuple[None, None]]:
        """
        Tries to find a Fwego field that matches that raw Airtable column data. If
        None is returned, the column is not compatible with Fwego and must be ignored.

        :param raw_airtable_table: The raw Airtable table data related to the column.
        :param raw_airtable_column: The raw Airtable column data that must be
        :return: The related Fwego field and AirtableColumnType that should be used
            for the conversion.
        """

        try:
            type_name = raw_airtable_column.get("type", "")
            airtable_column_type = self.get(type_name)
            fwego_field = airtable_column_type.to_fwego_field(
                raw_airtable_table, raw_airtable_column
            )

            if fwego_field is None:
                return None, None
            else:
                return fwego_field, airtable_column_type
        except self.does_not_exist_exception_class:
            return None, None


# A default airtable column type registry is created here, this is the one that is used
# throughout the whole Fwego application to add a new airtable column type.
airtable_column_type_registry = AirtableColumnTypeRegistry()
