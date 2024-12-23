from django.contrib.auth import get_user_model
from django.db import transaction

from fwego.core.handler import CoreHandler
from fwego.core.models import Workspace, WorkspaceUser
from fwego.core.user.exceptions import UserAlreadyExist
from fwego.core.user.handler import UserHandler

User = get_user_model()


@transaction.atomic
def load_test_data():
    print("Add basic users...")
    user_handler = UserHandler()

    for i in range(3):
        # Create main admin
        email = f"admin{i + 1}@fwego.io" if i > 0 else "admin@fwego.io"
        try:
            admin = user_handler.create_user(f"Admin {i}", email, "password")
        except UserAlreadyExist:
            admin = User.objects.get(email=email)

        admin.is_staff = True
        admin.save()

        try:
            workspace = Workspace.objects.get(
                name=f"Acme Corp ({i +1})" if i > 0 else "Acme Corp"
            )
        except Workspace.DoesNotExist:
            workspace = (
                CoreHandler()
                .create_workspace(
                    admin, name=f"Acme Corp ({i +1})" if i > 0 else "Acme Corp"
                )
                .workspace
            )

        # Create a second admin for the workspace
        email = f"admin{i + 1}_bis@fwego.io" if i > 0 else "admin_bis@fwego.io"
        try:
            admin_bis = user_handler.create_user(f"Admin {i+1} bis", email, "password")
        except UserAlreadyExist:
            admin_bis = User.objects.get(email=email)
        WorkspaceUser.objects.update_or_create(
            workspace=workspace,
            user=admin_bis,
            defaults=dict(permissions="ADMIN", order=2),
        )

        for j in range(3):
            member_email_prefix = f"member{i+1}" if j > 0 else "member"
            member_email_prefix = (
                f"{member_email_prefix}_{j+1}" if i > 0 else member_email_prefix
            )
            member_email = f"{member_email_prefix}@fwego.io"
            try:
                member = user_handler.create_user(
                    f"Member {i+1} {j+1}", member_email, "password"
                )
            except UserAlreadyExist:
                member = User.objects.get(email=member_email)

            WorkspaceUser.objects.update_or_create(
                workspace=workspace,
                user=member,
                defaults=dict(permissions="MEMBER", order=j + 2),
            )
