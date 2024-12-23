from django.contrib.auth import get_user_model
from django.db import models

from fwego.contrib.database.fields.models import Field
from fwego.contrib.database.table.models import Table
from fwego.core.app_auth_providers.models import AppAuthProvider
from fwego.core.user_sources.models import UserSource

User = get_user_model()


class LocalFwegoUserSource(UserSource):
    """
    This model represents the Local fwego user source. This source save user accounts
    in a database table of the same instance.
    """

    table = models.ForeignKey(Table, null=True, default=None, on_delete=models.SET_NULL)

    email_field = models.ForeignKey(
        Field,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="The Fwego field that contains the email value for the user.",
    )

    name_field = models.ForeignKey(
        Field,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="The Fwego field that contains the name of the user.",
    )

    role_field = models.ForeignKey(
        Field,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="The Fwego field that contains the role of the user.",
    )


class LocalFwegoPasswordAppAuthProvider(AppAuthProvider):
    password_field = models.ForeignKey(
        Field,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="The Fwego field that contains the password of the user.",
    )
