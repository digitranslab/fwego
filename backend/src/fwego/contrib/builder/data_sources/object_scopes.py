from typing import Optional

from django.db.models import Q, QuerySet

from fwego.contrib.builder.data_sources.models import DataSource
from fwego.contrib.builder.object_scopes import BuilderObjectScopeType
from fwego.contrib.builder.pages.object_scopes import BuilderPageObjectScopeType
from fwego.core.object_scopes import (
    ApplicationObjectScopeType,
    WorkspaceObjectScopeType,
)
from fwego.core.registries import ObjectScopeType, object_scope_type_registry


class BuilderDataSourceObjectScopeType(ObjectScopeType):
    type = "builder_data_source"
    model_class = DataSource

    def get_parent_scope(self) -> Optional["ObjectScopeType"]:
        return object_scope_type_registry.get("builder_page")

    def get_base_queryset(self, include_trash: bool = False) -> QuerySet:
        return (
            super()
            .get_base_queryset(include_trash)
            .filter(page__builder__workspace__isnull=False)
        )

    def get_enhanced_queryset(self, include_trash: bool = False) -> QuerySet:
        return self.get_base_queryset(include_trash).select_related(
            "page__builder__workspace"
        )

    def get_filter_for_scope_type(self, scope_type, scopes):
        if scope_type.type == WorkspaceObjectScopeType.type:
            return Q(page__builder__workspace__in=[s.id for s in scopes])

        if (
            scope_type.type == BuilderObjectScopeType.type
            or scope_type.type == ApplicationObjectScopeType.type
        ):
            return Q(page__builder__in=[s.id for s in scopes])

        if scope_type.type == BuilderPageObjectScopeType.type:
            return Q(page__in=[s.id for s in scopes])

        if scope_type.type == self.type:
            return Q(id__in=[s.id for s in scopes])

        raise TypeError("The given type is not handled.")
