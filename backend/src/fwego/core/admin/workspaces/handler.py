from fwego.core.admin.workspaces.exceptions import CannotDeleteATemplateGroupError
from fwego.core.exceptions import IsNotAdminError
from fwego.core.signals import workspace_deleted
from fwego.core.trash.handler import TrashHandler


class WorkspacesAdminHandler:
    def delete_workspace(self, user, workspace):
        """
        Deletes an existing workspace and related applications if the user is staff.

        :param user: The user on whose behalf the workspace is deleted
        :type: user: User
        :param workspace: The workspace instance that must be deleted.
        :type: workspace: Workspace
        :raises IsNotAdminError: If the user is not admin or staff.
        """

        if not user.is_staff:
            raise IsNotAdminError()

        if workspace.has_template():
            raise CannotDeleteATemplateGroupError()

        # Load the workspace users before the workspace is deleted so that we can
        # pass those along with the signal.
        workspace_id = workspace.id
        workspace_users = list(workspace.users.all())

        TrashHandler.permanently_delete(workspace)

        workspace_deleted.send(
            self,
            workspace_id=workspace_id,
            workspace=workspace,
            workspace_users=workspace_users,
        )
