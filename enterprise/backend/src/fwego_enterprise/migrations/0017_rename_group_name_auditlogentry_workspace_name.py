# Generated by Django 3.2.13 on 2023-02-23 09:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fwego_enterprise", "0016_rename_auditlogentry_group_id_workspace_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="auditlogentry",
            old_name="group_name",
            new_name="workspace_name",
        ),
    ]
