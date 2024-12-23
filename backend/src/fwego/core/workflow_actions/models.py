from django.db import models

from fwego.core.mixins import (
    CreatedAndUpdatedOnMixin,
    HierarchicalModelMixin,
    PolymorphicContentTypeMixin,
    WithRegistry,
)
from fwego.core.registry import ModelRegistryMixin


class WorkflowAction(
    PolymorphicContentTypeMixin,
    CreatedAndUpdatedOnMixin,
    HierarchicalModelMixin,
    models.Model,
    WithRegistry,
):
    @staticmethod
    def get_type_registry() -> ModelRegistryMixin:
        raise Exception(
            "Needs to be implement by module specific workflow actions parent"
        )

    class Meta:
        abstract = True
