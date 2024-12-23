from django.db import migrations

from fwego.core.formula.parser.parser import convert_string_to_string_literal_token


def forward(apps, schema_editor):
    getrow_updates = []
    listrows_updates = []
    LocalFwegoGetRow = apps.get_model("integrations", "LocalFwegoGetRow")
    LocalFwegoListRows = apps.get_model("integrations", "LocalFwegoListRows")

    for service in LocalFwegoGetRow.objects.all():
        service.search_query = convert_string_to_string_literal_token(
            service.search_query, True
        )
        getrow_updates.append(service)
    LocalFwegoGetRow.objects.bulk_update(getrow_updates, ["search_query"])

    for service in LocalFwegoListRows.objects.all():
        service.search_query = convert_string_to_string_literal_token(
            service.search_query, True
        )
        listrows_updates.append(service)
    LocalFwegoListRows.objects.bulk_update(listrows_updates, ["search_query"])


class Migration(migrations.Migration):
    dependencies = [
        (
            "integrations",
            "0003_migrate_local_fwego_table_service_filter_values_to_formulas",
        ),
    ]

    operations = [
        migrations.RunPython(forward, migrations.RunPython.noop),
    ]
