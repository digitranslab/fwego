# Generated by Django 3.2.13 on 2022-07-22 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0029_duplicateapplicationjob"),
        ("database", "0083_form_field_options_conditions"),
    ]

    operations = [
        migrations.CreateModel(
            name="DuplicateTableJob",
            fields=[
                (
                    "job_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.job",
                    ),
                ),
                (
                    "user_session_id",
                    models.CharField(
                        help_text="The user session uuid needed for undo/redo functionality.",
                        max_length=36,
                        null=True,
                    ),
                ),
                (
                    "user_websocket_id",
                    models.CharField(
                        help_text="The user websocket uuid needed to manage signals sent correctly.",
                        max_length=36,
                        null=True,
                    ),
                ),
                (
                    "duplicated_table",
                    models.OneToOneField(
                        help_text="The duplicated Fwego table.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="duplicated_from_jobs",
                        to="database.table",
                    ),
                ),
                (
                    "original_table",
                    models.ForeignKey(
                        help_text="The Fwego table to duplicate.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="duplicated_by_jobs",
                        to="database.table",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.job", models.Model),
        ),
    ]
