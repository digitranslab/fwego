# Generated by Django 4.1.13 on 2024-06-04 08:05

from django.db import migrations, models

import fwego.core.formula.field


def populate_show_as_dropdown_default_value(apps, schema_editor):
    """
    Sets the default value for new `show_as_dropdown` property.
    """

    ChoiceElement = apps.get_model("builder", "choiceelement")
    ChoiceElement.objects.update(show_as_dropdown=True)


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0021_dropdownelement_multiple"),
    ]

    operations = [
        migrations.RenameModel(old_name="DropdownElementOption", new_name="ChoiceElementOption"),
        migrations.RenameModel(old_name="DropdownElement", new_name="ChoiceElement"),
        migrations.AlterField(
            model_name="choiceelement",
            name="default_value",
            field=fwego.core.formula.field.FormulaField(
                default="", help_text="This choice's input default value."
            ),
        ),
        migrations.AlterField(
            model_name="choiceelement",
            name="label",
            field=fwego.core.formula.field.FormulaField(
                default="", help_text="The text label for this choice"
            ),
        ),
        migrations.AlterField(
            model_name="choiceelement",
            name="multiple",
            field=models.BooleanField(
                default=False,
                help_text="Whether this choice allows users to choose multiple values.",
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="choiceelementoption",
            old_name="dropdown",
            new_name="choice",
        ),
        migrations.AddField(
            model_name="choiceelement",
            name="show_as_dropdown",
            field=models.BooleanField(
                default=True,
                help_text="Whether to show the choices as a dropdown.",
                null=True,
            ),
        ),
        migrations.RunPython(populate_show_as_dropdown_default_value, reverse_code=migrations.RunPython.noop),
    ]
