# Generated by Django 5.0.9 on 2024-10-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fwego_premium", "0021_timelineview_timescale"),
    ]

    operations = [
        migrations.AddField(
            model_name="aifield",
            name="ai_temperature",
            field=models.FloatField(null=True),
        ),
    ]
