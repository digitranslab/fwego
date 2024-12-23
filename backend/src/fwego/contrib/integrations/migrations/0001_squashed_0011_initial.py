# Generated by Django 4.0.10 on 2024-01-16 19:12

import django.db.models.deletion
import django.db.models.manager
from django.conf import settings
from django.db import migrations, models

import fwego.core.formula.field


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("database", "0133_formviewfieldoptions_field_component"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("database", "0125_add_row_history"),
        ("core", "0077_blacklistedtoken"),
        ("core", "0070_integration_service"),
        ("database", "0115_countfield"),
        ("core", "0074_email_notifications_user_timezone"),
        ("database", "0126_alter_rowhistory_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="LocalFwegoIntegration",
            fields=[
                (
                    "integration_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.integration",
                    ),
                ),
                (
                    "authorized_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.integration",),
        ),
        migrations.CreateModel(
            name="LocalFwegoGetRow",
            fields=[
                (
                    "service_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.service",
                    ),
                ),
                ("row_id", fwego.core.formula.field.FormulaField()),
                (
                    "view",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="database.view",
                    ),
                ),
                (
                    "search_query",
                    models.TextField(
                        default="",
                        help_text="The query to apply to the service to narrow the results down.",
                        max_length=225,
                    ),
                ),
                (
                    "table",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="database.table",
                    ),
                ),
                (
                    "filter_type",
                    models.CharField(
                        choices=[("AND", "And"), ("OR", "Or")],
                        default="AND",
                        help_text="Indicates whether all the rows should apply to all filters (AND) or to any filter (OR).",
                        max_length=3,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.service",),
        ),
        migrations.CreateModel(
            name="LocalFwegoListRows",
            fields=[
                (
                    "service_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.service",
                    ),
                ),
                (
                    "view",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="database.view",
                    ),
                ),
                (
                    "search_query",
                    models.TextField(
                        default="",
                        help_text="The query to apply to the service to narrow the results down.",
                        max_length=225,
                    ),
                ),
                (
                    "table",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="database.table",
                    ),
                ),
                (
                    "filter_type",
                    models.CharField(
                        choices=[("AND", "And"), ("OR", "Or")],
                        default="AND",
                        help_text="Indicates whether all the rows should apply to all filters (AND) or to any filter (OR).",
                        max_length=3,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.service",),
        ),
        migrations.CreateModel(
            name="LocalFwegoTableServiceFilter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        help_text="Indicates how the field's value must be compared to the filter's value. The filter is always in this order `field` `type` `value` (example: `field_1` `contains` `Test`).",
                        max_length=48,
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        blank=True,
                        help_text="The filter value that must be compared to the field's value.",
                        max_length=255,
                    ),
                ),
                (
                    "field",
                    models.ForeignKey(
                        help_text="The database Field, in the LocalFwegoTableService, which we would like to filter upon.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database.field",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        help_text="The service which this filter belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="service_filters",
                        to="core.service",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("order", "id"),
            },
        ),
        migrations.AddField(
            model_name="localfwegotableservicefilter",
            name="order",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="LocalFwegoTableServiceSort",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveIntegerField()),
                (
                    "field",
                    models.ForeignKey(
                        help_text="The database Field, in the LocalFwegoTableService service, which we would like to sort upon.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database.field",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        help_text="The service which this sort belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="service_sorts",
                        to="core.service",
                    ),
                ),
                (
                    "order_by",
                    models.CharField(
                        choices=[("ASC", "Ascending"), ("DESC", "Descending")],
                        default="ASC",
                        help_text="Indicates the sort order direction. ASC (Ascending) is from A to Z and DESC (Descending) is from Z to A.",
                        max_length=4,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "ordering": ("order", "id"),
            },
        ),
        migrations.AlterModelManagers(
            name="localfwegotableservicefilter",
            managers=[
                ("objects_and_trash", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name="localfwegotableservicesort",
            managers=[
                ("objects_and_trash", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="LocalFwegoTableServiceFieldMapping",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "value",
                    fwego.core.formula.field.FormulaField(
                        default="", help_text="The field mapping's value."
                    ),
                ),
                (
                    "field",
                    models.ForeignKey(
                        help_text="The Fwego field that this mapping relates to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database.field",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        help_text="The LocalFwego Service that this field mapping relates to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="field_mappings",
                        to="core.service",
                    ),
                ),
            ],
            managers=[
                ("objects_and_trash", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="LocalFwegoUpsertRow",
            fields=[
                (
                    "service_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.service",
                    ),
                ),
                (
                    "table",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="database.table",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.service",),
        ),
        migrations.AddField(
            model_name="localfwegoupsertrow",
            name="row_id",
            field=fwego.core.formula.field.FormulaField(default=None),
            preserve_default=False,
        ),
    ]
