# Generated by Django 4.1.13 on 2024-02-07 10:01
from django.db import migrations

from fwego.contrib.integrations.migrations.helpers.migrate_local_fwego_table_service_filter_formulas_to_value_is_formula import (  # noqa: E501
    value_parses_as_formula,
)


def forward(apps, schema_editor):
    LocalFwegoTableServiceFilter = apps.get_model(
        "integrations", "LocalFwegoTableServiceFilter"
    )
    updates = []
    service_filters = LocalFwegoTableServiceFilter.objects.all()
    for service_filter in service_filters:
        if value_parses_as_formula(service_filter.value):
            service_filter.value_is_formula = True
            updates.append(service_filter)

    LocalFwegoTableServiceFilter.objects.bulk_update(updates, ["value_is_formula"])


class Migration(migrations.Migration):
    dependencies = [
        (
            "integrations",
            "0005_add_localfwegotableservicefilter_value_is_formula",
        ),
    ]

    operations = [
        migrations.RunPython(forward, migrations.RunPython.noop),
    ]
