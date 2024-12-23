# Generated by Django 3.2.13 on 2022-07-08 11:19

import django.core.validators
from django.db import migrations, models

import fwego.contrib.database.webhooks.validators


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0088_multiple_collaborators_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tablewebhook",
            name="url",
            field=models.TextField(
                help_text="The URL that must be called when the webhook is triggered.",
                validators=[
                    django.core.validators.MaxLengthValidator(2000),
                    fwego.contrib.database.webhooks.validators.url_validator,
                ],
            ),
        ),
        migrations.AlterField(
            model_name="tablewebhookcall",
            name="called_url",
            field=models.TextField(
                validators=[
                    django.core.validators.MaxLengthValidator(2000),
                    fwego.contrib.database.webhooks.validators.url_validator,
                ]
            ),
        ),
    ]
