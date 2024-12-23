# Generated by Django 3.2.18 on 2023-06-02 14:49

import django.db.models.deletion
from django.db import migrations, models

import fwego.core.integrations.models
import fwego.core.mixins
import fwego.core.services.models


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("core", "0069_synced_datetime_field"),
    ]

    operations = [
        migrations.CreateModel(
            name="Integration",
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
                ("trashed", models.BooleanField(db_index=True, default=False)),
                ("name", models.CharField(max_length=255)),
                (
                    "order",
                    models.DecimalField(
                        decimal_places=20,
                        default=1,
                        editable=False,
                        help_text="Lowest first.",
                        max_digits=40,
                    ),
                ),
                (
                    "application",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="integrations",
                        to="core.application",
                    ),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=models.SET(
                            fwego.core.integrations.models.get_default_integration
                        ),
                        related_name="integrations",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "ordering": ("order", "id"),
            },
            bases=(
                fwego.core.mixins.PolymorphicContentTypeMixin,
                fwego.core.mixins.FractionOrderableMixin,
                models.Model,
            ),
        ),
        migrations.CreateModel(
            name="Service",
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
                ("trashed", models.BooleanField(db_index=True, default=False)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=models.SET(
                            fwego.core.services.models.get_default_service_service
                        ),
                        related_name="services",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "integration",
                    models.ForeignKey(
                        help_text="The integration used to establish the connection with the service.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="services",
                        to="core.integration",
                    ),
                ),
            ],
            options={
                "ordering": ("id",),
            },
            bases=(fwego.core.mixins.PolymorphicContentTypeMixin, models.Model),
        ),
    ]
