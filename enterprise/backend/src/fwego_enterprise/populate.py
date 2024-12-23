from django.contrib.auth import get_user_model

from fwego.contrib.builder.models import Builder
from fwego.contrib.database.fields.models import Field
from fwego.contrib.database.table.models import Table
from fwego.core.app_auth_providers.registries import app_auth_provider_type_registry
from fwego.core.integrations.models import Integration
from fwego.core.models import WorkspaceUser
from fwego.core.user.exceptions import UserAlreadyExist
from fwego.core.user.handler import UserHandler
from fwego.core.user_sources.handler import UserSourceHandler
from fwego.core.user_sources.registries import user_source_type_registry
from fwego_enterprise.integrations.local_fwego.models import (
    LocalFwegoPasswordAppAuthProvider,
    LocalFwegoUserSource,
)
from fwego_enterprise.role.default_roles import default_roles

User = get_user_model()


def load_test_data():
    # Get the user created in the main module
    user = User.objects.get(email="admin@fwego.io")
    workspace = user.workspaceuser_set.get(workspace__name="Acme Corp").workspace

    print("Add one user per existing role in the same workspace as admin")
    for i, r in enumerate(default_roles.keys()):
        rl = r.lower()
        try:
            user = UserHandler().create_user(rl, f"{rl}@fwego.io", "password")
        except UserAlreadyExist:
            user = User.objects.get(email=f"{rl}@fwego.io")

        WorkspaceUser.objects.update_or_create(
            workspace=workspace, user=user, defaults=dict(permissions=r, order=i + 1)
        )

    builder = Builder.objects.get(
        name="Back to local website", workspace__isnull=False, trashed=False
    )

    integration = Integration.objects.get(
        name="Local fwego", application__trashed=False, application_id=builder.id
    )

    user_table = Table.objects.get(
        name="User Accounts",
        database__workspace=workspace,
        database__trashed=False,
    )

    email_field = Field.objects.get(table=user_table, name="Email")
    username_field = Field.objects.get(table=user_table, name="Username")
    password_field = Field.objects.get(table=user_table, name="Password")

    user_source_type = user_source_type_registry.get("local_fwego")

    try:
        user_source = LocalFwegoUserSource.objects.get(
            name="Local fwego",
            application__trashed=False,
            application_id=builder.id,
        )
    except LocalFwegoUserSource.DoesNotExist:
        user_source = UserSourceHandler().create_user_source(
            user_source_type,
            builder,
            name="Local fwego",
            table=user_table,
            application_id=builder.id,
            integration=integration,
            email_field=email_field,
            name_field=username_field,
        )

    auth_provider_type = app_auth_provider_type_registry.get("local_fwego_password")

    try:
        LocalFwegoPasswordAppAuthProvider.objects.get(
            user_source_id=user_source.id,
        )
    except LocalFwegoPasswordAppAuthProvider.DoesNotExist:
        auth_provider_type.create(
            user_source=user_source, password_field=password_field, enabled=True
        )
