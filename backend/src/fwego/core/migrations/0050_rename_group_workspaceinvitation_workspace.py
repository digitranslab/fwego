# Generated by Django 3.2.13 on 2023-01-16 16:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0049_rename_groupinvitation_workspaceinvitation"),
    ]

    operations = [
        migrations.RenameField(
            model_name="workspaceinvitation",
            old_name="group",
            new_name="workspace",
        ),
    ]
