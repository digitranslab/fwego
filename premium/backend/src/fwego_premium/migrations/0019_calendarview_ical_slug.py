# Generated by Django 4.1.13 on 2024-06-14 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fwego_premium", "0018_aifield_ai_file_field"),
    ]

    operations = [
        migrations.AddField(
            model_name="calendarview",
            name="ical_public",
            field=models.BooleanField(
                db_index=True,
                default=False,
                null=True,
                help_text="Setting this to `True` will expose ical feed url",
            ),
        ),
        migrations.AddField(
            model_name="calendarview",
            name="ical_slug",
            field=models.SlugField(
                default=None,
                help_text="Additional slug that allow access to ical format feed",
                null=True,
                unique=True,
            ),
        ),
    ]
