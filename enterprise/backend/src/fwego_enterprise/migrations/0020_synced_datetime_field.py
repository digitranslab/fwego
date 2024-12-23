# Generated by Django 3.2.18 on 2023-06-15 09:55

from django.db import migrations

import fwego.core.fields


class Migration(migrations.Migration):
    dependencies = [
        ("fwego_enterprise", "0019_alter_auditlogexportjob_filter_workspace_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auditlogentry",
            name="updated_on",
            field=fwego.core.fields.SyncedDateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="role",
            name="updated_on",
            field=fwego.core.fields.SyncedDateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="roleassignment",
            name="updated_on",
            field=fwego.core.fields.SyncedDateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="team",
            name="updated_on",
            field=fwego.core.fields.SyncedDateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="teamsubject",
            name="updated_on",
            field=fwego.core.fields.SyncedDateTimeField(auto_now=True),
        ),
    ]