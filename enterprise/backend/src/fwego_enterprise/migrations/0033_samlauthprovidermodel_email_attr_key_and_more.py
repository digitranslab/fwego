# Generated by Django 5.0.9 on 2024-11-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fwego_enterprise", "0032_gitlabissuesdatasync"),
    ]

    operations = [
        migrations.AddField(
            model_name="samlauthprovidermodel",
            name="email_attr_key",
            field=models.CharField(
                db_default="user.email",
                default="user.email",
                help_text="The key in the SAML response that contains the email address of the user. If this is not set, the email will be taken from the user's profile.",
                max_length=32,
            ),
        ),
        migrations.AddField(
            model_name="samlauthprovidermodel",
            name="first_name_attr_key",
            field=models.CharField(
                db_default="user.first_name",
                default="user.first_name",
                help_text="The key in the SAML response that contains the first name of the user. If this is not set, the first name will be taken from the user's profile.",
                max_length=32,
            ),
        ),
        migrations.AddField(
            model_name="samlauthprovidermodel",
            name="last_name_attr_key",
            field=models.CharField(
                blank=True,
                db_default="user.last_name",
                default="user.last_name",
                help_text="The key in the SAML response that contains the last name of the user. If this is not set, the last name will be taken from the user's profile.",
                max_length=32,
            ),
        ),
    ]
