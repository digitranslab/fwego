# Generated by Django 5.0.9 on 2024-10-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fwego_premium", "0020_timelineview_timelineviewfieldoptions_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="timelineview",
            name="timescale",
            field=models.CharField(
                choices=[
                    ("day", "Day"),
                    ("week", "Week"),
                    ("month", "Month"),
                    ("year", "Year"),
                ],
                db_default="month",
                default="month",
                help_text="The timescale that the timeline should be displayed in.",
                max_length=32,
            ),
        ),
    ]
