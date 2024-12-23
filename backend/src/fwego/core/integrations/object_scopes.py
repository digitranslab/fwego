from typing import Optional

from django.db.models import Q, QuerySet

from fwego.core.integrations.models import Integration
from fwego.core.object_scopes import (
    ApplicationObjectScopeType,
    WorkspaceObjectScopeType,
)
from fwego.core.registries import ObjectScopeType, object_scope_type_registry


class IntegrationObjectScopeType(ObjectScopeType):
    type = "integration"
    model_class = Integration

    def get_parent_scope(self) -> Optional["ObjectScopeType"]:
        return object_scope_type_registry.get("application")

    def get_enhanced_queryset(self, include_trash: bool = False) -> QuerySet:
        return self.get_base_queryset(include_trash).select_related(
            "application__workspace"
        )

    def get_filter_for_scope_type(self, scope_type, scopes):
        if scope_type.type == WorkspaceObjectScopeType.type:
            return Q(application__workspace__in=[s.id for s in scopes])

        if scope_type.type == ApplicationObjectScopeType.type:
            return Q(application__in=[s.id for s in scopes])

        if scope_type.type == self.type:
            return Q(id__in=[s.id for s in scopes])

        raise TypeError("The given type is not handled.")
