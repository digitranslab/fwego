from typing import List

from django.contrib.auth.models import AbstractUser

from fwego.core.models import Workspace
from fwego.core.registries import SubjectType
from fwego.core.types import Subject
from fwego.core.user_sources.user_source_user import UserSourceUser


class UserSourceUserSubjectType(SubjectType):
    """
    The user source user subject.
    """

    type = "user_source.user"
    model_class = UserSourceUser

    def are_in_workspace(
        self, subjects: List[Subject], workspace: Workspace
    ) -> List[bool]:
        """
        Check whether the given subjects are member of the given workspace.
        """

        return [False for _ in subjects]

    def get_serializer(self, model_instance, **kwargs):
        return None

    def get_users_included_in_subject(
        self, subject: AbstractUser
    ) -> List[AbstractUser]:
        return [subject]
