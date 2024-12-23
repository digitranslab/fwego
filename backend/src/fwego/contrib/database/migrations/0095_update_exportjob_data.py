# Generated by Django 3.2.13 on 2022-12-23 07:36

from django.db import migrations, models

from fwego.contrib.database.export.models import ExportJob


def forward(apps, schema_editor):
    """
    This migration will update job's state from 'complete' to 'finished' and
    multiply the progress_percentage by 100 to make them compatible with
    job that inherit from the Job class in 'core/jobs/models.py'.
    """

    ExportJob.objects.filter(state="complete").update(state="finished")
    ExportJob.objects.all().update(
        progress_percentage=models.F("progress_percentage") * 100
    )


def reverse(apps, schema_editor):
    ExportJob.objects.filter(state="finished").update(state="complete")
    ExportJob.objects.all().update(
        progress_percentage=models.F("progress_percentage") / 100
    )


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0094_exportjob_refactor"),
    ]

    operations = [migrations.RunPython(forward, reverse)]
