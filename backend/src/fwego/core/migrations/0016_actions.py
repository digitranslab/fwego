# Generated by Django 3.2.12 on 2022-04-19 10:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import fwego.core.action.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0015_alter_userprofile_language"),
    ]

    operations = [
        migrations.CreateModel(
            name="Action",
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
                ("session", models.TextField(blank=True, db_index=True, null=True)),
                ("created_on", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("type", models.TextField()),
                (
                    "params",
                    models.JSONField(
                        encoder=fwego.core.action.models.JSONEncoderSupportingDataClasses
                    ),
                ),
                ("scope", models.TextField(db_index=True)),
                (
                    "undone_at",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                ("error", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("-created_on",),
            },
        ),
        migrations.AddIndex(
            model_name="action",
            index=models.Index(
                fields=["-created_on", "-id"], name="core_action_created_cd208a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="action",
            index=models.Index(
                fields=["-undone_at", "-id"], name="core_action_undone__215f89_idx"
            ),
        ),
    ]
