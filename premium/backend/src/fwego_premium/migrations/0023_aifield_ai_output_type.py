# Generated by Django 5.0.9 on 2024-10-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fwego_premium", "0022_aifield_ai_temperature"),
    ]

    operations = [
        migrations.AddField(
            model_name="aifield",
            name="ai_output_type",
            field=models.CharField(db_default="text", default="text", max_length=32),
        ),
    ]
