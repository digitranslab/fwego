# Generated by Django 4.1.13 on 2024-04-04 20:03

import django.db.models.deletion
from django.db import migrations, models

import fwego.core.formula.field


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0153_passwordfield"),
        ("fwego_premium", "0016_rowcommentsnotificationmode"),
    ]

    operations = [
        migrations.CreateModel(
            name="AIField",
            fields=[
                (
                    "field_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="database.field",
                    ),
                ),
                ("ai_generative_ai_type", models.CharField(max_length=32, null=True)),
                ("ai_generative_ai_model", models.CharField(max_length=32, null=True)),
                ("ai_prompt", fwego.core.formula.field.FormulaField(default="")),
            ],
            options={
                "abstract": False,
            },
            bases=("database.field",),
        ),
    ]
