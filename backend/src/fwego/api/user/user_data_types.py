from typing import List

from fwego.api.user.registries import UserDataType
from fwego.core.handler import CoreHandler


class GlobalPermissionsDataType(UserDataType):
    type = "permissions"

    def get_user_data(self, user, request) -> List[dict]:
        """
        Responsible for annotating `User` responses with global permissions
        (which don't relate to a `Workspace`).
        """

        return CoreHandler().get_permissions(user)
