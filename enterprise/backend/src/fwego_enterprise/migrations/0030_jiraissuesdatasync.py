# Generated by Django 5.0.9 on 2024-10-13 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fwego_enterprise", "0029_localfwegotabledatasync"),
        ("database", "0169_alter_galleryview_card_cover_image_field"),
    ]

    operations = [
        migrations.CreateModel(
            name="JiraIssuesDataSync",
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
                    "jira_url",
                    models.URLField(
                        help_text="The base URL of your Jira instance (e.g., https://your-domain.atlassian.net).",
                        max_length=2000,
                    ),
                ),
                (
                    "jira_project_key",
                    models.CharField(
                        blank=True,
                        help_text="The project key of the Jira project (e.g., PROJ).",
                        max_length=255,
                    ),
                ),
                (
                    "jira_username",
                    models.CharField(
                        help_text="The username of the Jira account used to authenticate.",
                        max_length=255,
                    ),
                ),
                (
                    "jira_api_token",
                    models.CharField(
                        help_text="The API token of the Jira account used for authentication.",
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
