from typing import NamedTuple, Optional

from fwego.core.types import ScopeObject, Subject
from fwego_enterprise.role.models import Role


class AssignmentTuple(NamedTuple):
    subject_type_name: str
    subject_id: int
    original_role_uid: Optional[str]
    role_uid: Optional[str]
    scope_type_name: str
    scope_id: int


class NewRoleAssignment(NamedTuple):
    subject: Subject
    role: Role
    scope: ScopeObject
