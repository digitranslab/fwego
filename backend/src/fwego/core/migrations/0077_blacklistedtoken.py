# Generated by Django 3.2.21 on 2023-10-25 08:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import fwego.core.fields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0076_userprofile_last_password_change"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlacklistedToken",
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
                (
                    "hashed_token",
                    models.CharField(db_index=True, max_length=64, unique=True),
                ),
                ("expires_at", models.DateTimeField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]