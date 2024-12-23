# Generated by Django 4.2.13 on 2024-07-02 16:58

import django.db.models.deletion
from django.db import migrations, models

import fwego.core.fields


def migrate_element_styles(apps, schema_editor):
    """
    Migrates on model element styles into the style property.
    """

    Element = apps.get_model("builder", "element")

    # Set default values for element styles
    Element.objects.all().update(
        style_margin_left=0,
        style_margin_right=0,
        style_margin_top=0,
        style_margin_bottom=0,
        style_background_mode="fill",
    )


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0088_remove_blacklistedtoken_user"),
        ("builder", "0026_add_more_style_properties"),
    ]

    operations = [
        migrations.AddField(
            model_name="buttonthemeconfigblock",
            name="button_border_color",
            field=models.CharField(
                blank=True,
                default="border",
                help_text="The border color of buttons",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="buttonthemeconfigblock",
            name="button_border_radius",
            field=models.SmallIntegerField(default=4, help_text="Button border radius"),
        ),
        migrations.AddField(
            model_name="buttonthemeconfigblock",
            name="button_border_size",
            field=models.SmallIntegerField(default=0, help_text="Button border size"),
        ),
        migrations.AddField(
            model_name="buttonthemeconfigblock",
            name="button_font_family",
            field=models.CharField(default="inter", max_length=250),
        ),
        migrations.AddField(
            model_name="buttonthemeconfigblock",
            name="button_font_size",
            field=models.SmallIntegerField(default=13),
        ),
        migrations.AddField(
            model_name="buttonthemeconfigblock",
            name="button_horizontal_padding",
            field=models.SmallIntegerField(
                default=12, help_text="Button horizontal padding"
            ),
        ),
        migrations.AddField(
            model_name="buttonthemeconfigblock",
            name="button_hover_border_color",
            field=models.CharField(
                blank=True,
                default="border",
                help_text="The border color of buttons when hovered",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="buttonthemeconfigblock",
            name="button_hover_text_color",
            field=models.CharField(
                blank=True,
                default="#ffffffff",
                help_text="The text color of buttons when hovered",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="buttonthemeconfigblock",
            name="button_text_color",
            field=models.CharField(
                blank=True,
                default="#ffffffff",
                help_text="The text color of buttons",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="buttonthemeconfigblock",
            name="button_vertical_padding",
            field=models.SmallIntegerField(
                default=12, help_text="Button vertical padding"
            ),
        ),
        migrations.AddField(
            model_name="colorthemeconfigblock",
            name="main_error_color",
            field=models.CharField(default="#FF5A4A", max_length=9),
        ),
        migrations.AddField(
            model_name="colorthemeconfigblock",
            name="main_success_color",
            field=models.CharField(default="#12D452", max_length=9),
        ),
        migrations.AddField(
            model_name="colorthemeconfigblock",
            name="main_warning_color",
            field=models.CharField(default="#FCC74A", max_length=9),
        ),
        migrations.AddField(
            model_name="element",
            name="style_background_file",
            field=models.ForeignKey(
                help_text="An image file uploaded by the user to be used as element background",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="element_background_image_file",
                to="core.userfile",
            ),
        ),
        migrations.AddField(
            model_name="element",
            name="style_background_mode",
            field=models.CharField(
                choices=[("tile", "Tile"), ("fill", "Fill"), ("fit", "Fit")],
                default="fill",
                help_text="The mode of the background image",
                max_length=32,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="element",
            name="style_margin_bottom",
            field=models.PositiveIntegerField(
                default=0, help_text="Margin size of the bottom border.", null=True
            ),
        ),
        migrations.AddField(
            model_name="element",
            name="style_margin_left",
            field=models.PositiveIntegerField(
                default=0, help_text="Margin size of the left border.", null=True
            ),
        ),
        migrations.AddField(
            model_name="element",
            name="style_margin_right",
            field=models.PositiveIntegerField(
                default=0, help_text="Margin size of the right border.", null=True
            ),
        ),
        migrations.AddField(
            model_name="element",
            name="style_margin_top",
            field=models.PositiveIntegerField(
                default=0, help_text="Margin size of the top border.", null=True
            ),
        ),
        migrations.AddField(
            model_name="linkthemeconfigblock",
            name="link_font_family",
            field=models.CharField(default="inter", max_length=250),
        ),
        migrations.AddField(
            model_name="linkthemeconfigblock",
            name="link_font_size",
            field=models.SmallIntegerField(default=13),
        ),
        migrations.AddField(
            model_name="typographythemeconfigblock",
            name="body_font_family",
            field=models.CharField(default="inter", max_length=250),
        ),
        migrations.AddField(
            model_name="typographythemeconfigblock",
            name="heading_1_font_family",
            field=models.CharField(default="inter", max_length=250),
        ),
        migrations.AddField(
            model_name="typographythemeconfigblock",
            name="heading_2_font_family",
            field=models.CharField(default="inter", max_length=250),
        ),
        migrations.AddField(
            model_name="typographythemeconfigblock",
            name="heading_3_font_family",
            field=models.CharField(default="inter", max_length=250),
        ),
        migrations.AddField(
            model_name="typographythemeconfigblock",
            name="heading_4_font_family",
            field=models.CharField(default="inter", max_length=250),
        ),
        migrations.AddField(
            model_name="typographythemeconfigblock",
            name="heading_5_font_family",
            field=models.CharField(default="inter", max_length=250),
        ),
        migrations.AddField(
            model_name="typographythemeconfigblock",
            name="heading_6_font_family",
            field=models.CharField(default="inter", max_length=250),
        ),
        migrations.AlterField(
            model_name="element",
            name="style_background",
            field=models.CharField(
                choices=[("none", "None"), ("color", "Color"), ("image", "Image")],
                default="none",
                help_text="What type of background the element should have.",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="element",
            name="style_width",
            field=models.CharField(
                choices=[
                    ("full", "Full"),
                    ("full-width", "Full Width"),
                    ("normal", "Normal"),
                    ("medium", "Medium"),
                    ("small", "Small"),
                ],
                default="normal",
                help_text="Indicates the width of the element.",
                max_length=20,
            ),
        ),
        migrations.CreateModel(
            name="PageThemeConfigBlock",
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
                    "page_background_color",
                    models.CharField(
                        blank=True,
                        default="#ffffffff",
                        help_text="The background color of the page",
                        max_length=20,
                    ),
                ),
                (
                    "page_background_mode",
                    models.CharField(
                        choices=[("tile", "Tile"), ("fill", "Fill"), ("fit", "Fit")],
                        default="tile",
                        help_text="The mode of the background image",
                        max_length=32,
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
                (
                    "page_background_file",
                    models.ForeignKey(
                        help_text="An image file uploaded by the user to be used as page background",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="page_background_image_file",
                        to="core.userfile",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RunPython(
            migrate_element_styles, reverse_code=migrations.RunPython.noop
        ),
    ]