# Generated by Django 5.0.9 on 2024-10-24 13:20

import django.db.models.deletion
from django.db import migrations, models

import fwego.core.formula.field


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0039_alter_page_options_page_shared"),
    ]

    operations = [
        migrations.CreateModel(
            name="DateTimePickerElement",
            fields=[
                (
                    "element_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="builder.element",
                    ),
                ),
                (
                    "required",
                    models.BooleanField(
                        default=False,
                        help_text="Whether this form element is a required field.",
                    ),
                ),
                (
                    "label",
                    fwego.core.formula.field.FormulaField(
                        default="", help_text="The text label for this date time picker"
                    ),
                ),
                (
                    "default_value",
                    fwego.core.formula.field.FormulaField(
                        default="",
                        help_text="This date time picker input's default value.",
                    ),
                ),
                (
                    "date_format",
                    models.CharField(
                        choices=[
                            ("EU", "European (D/M/Y)"),
                            ("US", "US (M/D/Y)"),
                            ("ISO", "ISO (Y-M-D)"),
                        ],
                        default="EU",
                        help_text="EU (25/04/2024), US (04/25/2024) or ISO (2024-04-25)",
                        max_length=32,
                    ),
                ),
                (
                    "include_time",
                    models.BooleanField(
                        default=False,
                        help_text="Whether to include time in the representation of the date",
                    ),
                ),
                (
                    "time_format",
                    models.CharField(
                        choices=[("24", "24 hour"), ("12", "12 hour")],
                        default="24",
                        help_text="24 (14:00) or 12 (02:30) PM",
                        max_length=32,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("builder.element",),
        ),
    ]
