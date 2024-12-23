# Generated by Django 3.2.21 on 2023-11-02 15:31

from django.db import migrations
from django.db.models import F


def forward(apps, schema_editor):
    """
    Delete all the ViewFieldOptions where the field has been moved to another table.
    """

    GridViewFieldOptions = apps.get_model("database", "GridViewFieldOptions")
    FormViewFieldOptions = apps.get_model("database", "FormViewFieldOptions")
    GalleryViewFieldOptions = apps.get_model("database", "GalleryViewFieldOptions")

    for ViewFieldOptions, view_fk_field_name in (
        (GridViewFieldOptions, "grid_view_id"),
        (GalleryViewFieldOptions, "gallery_view_id"),
        (FormViewFieldOptions, "form_view_id"),
    ):
        ViewFieldOptions.objects.exclude(
            **{f"{view_fk_field_name}__table_id": F("field__table_id")}
        ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0133_formviewfieldoptions_field_component"),
    ]

    operations = [
        migrations.RunPython(forward, migrations.RunPython.noop),
    ]
