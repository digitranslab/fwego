# Generated by Django 4.2.13 on 2024-07-25 15:37

import django.db.models.deletion
from django.db import migrations, models

import fwego.core.fields


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0031_remove_buttonelement_alignment_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TableThemeConfigBlock",
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
                    "table_border_color",
                    models.CharField(
                        blank=True,
                        default="#000000FF",
                        help_text="The color of the table border",
                        max_length=20,
                    ),
                ),
                (
                    "table_border_size",
                    models.SmallIntegerField(default=1, help_text="Table border size"),
                ),
                (
                    "table_border_radius",
                    models.SmallIntegerField(
                        default=0, help_text="Table border radius"
                    ),
                ),
                (
                    "table_header_background_color",
                    models.CharField(
                        blank=True,
                        default="#edededff",
                        help_text="The background color of the table header cells",
                        max_length=20,
                    ),
                ),
                (
                    "table_header_text_color",
                    models.CharField(
                        blank=True,
                        default="#000000ff",
                        help_text="The text color of the table header cells",
                        max_length=20,
                    ),
                ),
                (
                    "table_header_font_size",
                    models.SmallIntegerField(
                        default=13, help_text="The font size of the header cells"
                    ),
                ),
                (
                    "table_header_font_family",
                    models.CharField(
                        default="inter",
                        help_text="The font family of the table header cells",
                        max_length=250,
                    ),
                ),
                (
                    "table_header_text_alignment",
                    models.CharField(
                        choices=[
                            ("left", "Left"),
                            ("center", "Center"),
                            ("right", "Right"),
                        ],
                        default="left",
                        max_length=10,
                    ),
                ),
                (
                    "table_cell_background_color",
                    models.CharField(
                        blank=True,
                        default="transparent",
                        help_text="The background color of the table cells",
                        max_length=20,
                    ),
                ),
                (
                    "table_cell_alternate_background_color",
                    models.CharField(
                        blank=True,
                        default="transparent",
                        help_text="The alternate background color of the table cells",
                        max_length=20,
                    ),
                ),
                (
                    "table_cell_alignment",
                    models.CharField(
                        choices=[
                            ("left", "Left"),
                            ("center", "Center"),
                            ("right", "Right"),
                        ],
                        default="left",
                        max_length=10,
                    ),
                ),
                (
                    "table_cell_vertical_padding",
                    models.SmallIntegerField(
                        default=10, help_text="Table cell vertical padding"
                    ),
                ),
                (
                    "table_cell_horizontal_padding",
                    models.SmallIntegerField(
                        default=20, help_text="Table cell horizontal padding"
                    ),
                ),
                (
                    "table_vertical_separator_color",
                    models.CharField(
                        blank=True,
                        default="#000000FF",
                        help_text="The color of the table vertical separator",
                        max_length=20,
                    ),
                ),
                (
                    "table_vertical_separator_size",
                    models.SmallIntegerField(
                        default=0, help_text="Table vertical separator size"
                    ),
                ),
                (
                    "table_horizontal_separator_color",
                    models.CharField(
                        blank=True,
                        default="#000000FF",
                        help_text="The color of the table horizontal separator",
                        max_length=20,
                    ),
                ),
                (
                    "table_horizontal_separator_size",
                    models.SmallIntegerField(
                        default=1, help_text="Table horizontal separator size"
                    ),
                ),
                (
                    "builder",
                    fwego.core.fields.AutoOneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s",
                        to="builder.builder",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
