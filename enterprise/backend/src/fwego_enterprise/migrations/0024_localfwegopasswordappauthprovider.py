# Generated by Django 3.2.21 on 2023-11-29 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0141_formview_users_to_notify_on_submit"),
        ("core", "0080_appauthprovider"),
        ("fwego_enterprise", "0023_localfwegousersource"),
    ]

    operations = [
        migrations.CreateModel(
            name="LocalFwegoPasswordAppAuthProvider",
            fields=[
                (
                    "appauthprovider_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.appauthprovider",
                    ),
                ),
                (
                    "password_field",
                    models.ForeignKey(
                        help_text="The Fwego field that contains the password of the user.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="database.field",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.appauthprovider",),
        ),
    ]