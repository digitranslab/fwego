# Generated by Django 3.2.6 on 2022-01-11 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0057_fix_invalid_type_filters_and_sorts"),
        ("fwego_premium", "0003_kanban_view"),
    ]

    operations = [
        migrations.AddField(
            model_name="kanbanview",
            name="card_cover_image_field",
            field=models.ForeignKey(
                blank=True,
                help_text=(
                    "References a file field of which the first image "
                    "must be shown as card cover image."
                ),
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="kanban_view_card_cover_field",
                to="database.filefield",
            ),
        ),
    ]
