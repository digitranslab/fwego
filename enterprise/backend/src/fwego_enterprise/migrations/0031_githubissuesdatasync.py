# Generated by Django 5.0.9 on 2024-10-21 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fwego_enterprise", "0030_jiraissuesdatasync"),
        ("database", "0170_update_password_tsv_fields"),
    ]

    operations = [
        migrations.CreateModel(
            name="GitHubIssuesDataSync",
            fields=[
                (
                    "datasync_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="database.datasync",
                    ),
                ),
                (
                    "github_issues_owner",
                    models.CharField(
                        help_text="The owner of the repository on GitHub.",
                        max_length=255,
                    ),
                ),
                (
                    "github_issues_repo",
                    models.CharField(
                        help_text="The name of the repository on GitHub.",
                        max_length=255,
                    ),
                ),
                (
                    "github_issues_api_token",
                    models.CharField(
                        help_text="The API token used to authenticate requests to GitHub.",
                        max_length=255,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("database.datasync",),
        ),
    ]
