# Generated by Django 3.2.13 on 2023-01-17 10:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fwego_enterprise", "0013_rename_group_role_workspace"),
    ]

    operations = [
        migrations.RenameField(
            model_name="roleassignment",
            old_name="group",
            new_name="workspace",
        ),
    ]