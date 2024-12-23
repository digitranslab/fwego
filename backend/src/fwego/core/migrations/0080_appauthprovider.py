# Generated by Django 3.2.21 on 2023-11-24 14:00

import django.db.models.deletion
from django.db import migrations, models

import fwego.core.fields
import fwego.core.mixins


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("core", "0079_remove_dangling_snapshots"),
    ]

    operations = [
        migrations.CreateModel(
            name="AppAuthProvider",
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
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", fwego.core.fields.SyncedDateTimeField(auto_now=True)),
                ("domain", models.CharField(max_length=255, null=True)),
                ("enabled", models.BooleanField(default=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="app_auth_providers",
                        to="contenttypes.contenttype",
                        verbose_name="content type",
                    ),
                ),
                (
                    "user_source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="auth_providers",
                        to="core.usersource",
                    ),
                ),
            ],
            options={
                "ordering": ["domain", "id"],
            },
            bases=(
                fwego.core.mixins.PolymorphicContentTypeMixin,
                models.Model,
                fwego.core.mixins.WithRegistry,
            ),
        ),
    ]
