# Generated by Django 3.2.13 on 2022-10-20 20:26

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("core", "0036_operation"),
        ("fwego_enterprise", "0003_teamsubject"),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "uid",
                    models.CharField(
                        default=uuid.uuid4,
                        help_text="Role unique identifier.",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Role human readable name.", max_length=255
                    ),
                ),
                (
                    "default",
                    models.BooleanField(
                        default=False,
                        help_text="True if this role is a default role. The default role are the roles you can use by default.",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        help_text="The optional group that this role belongs to.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="roles",
                        to="core.group",
                    ),
                ),
                (
                    "operations",
                    models.ManyToManyField(
                        help_text="List of allowed operation for this role.",
                        related_name="roles",
                        to="core.Operation",
                    ),
                ),
            ],
            options={
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="RoleAssignment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("subject_id", models.IntegerField(help_text="The subject ID.")),
                ("scope_id", models.IntegerField(help_text="The unique scope ID.")),
                (
                    "group",
                    models.ForeignKey(
                        help_text="The group that this role assignment belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="role_assignments",
                        to="core.group",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        help_text="The role given to the subject for the group.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fwego_enterprise.role",
                    ),
                ),
                (
                    "scope_type",
                    models.ForeignKey(
                        help_text="The scope type.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="role_scope_assignments",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "subject_type",
                    models.ForeignKey(
                        help_text="The subject type.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="role_subject_assignments",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "ordering": ("id",),
            },
        ),
        migrations.AddIndex(
            model_name="role",
            index=models.Index(fields=["uid"], name="fwego_ent_uid_5e9e91_idx"),
        ),
    ]
