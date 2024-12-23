from django.contrib.auth import get_user_model

from fwego.contrib.builder.data_sources.operations import (
    DispatchDataSourceOperationType,
    ListDataSourcesPageOperationType,
)
from fwego.contrib.builder.elements.operations import ListElementsPageOperationType
from fwego.contrib.builder.operations import ListPagesBuilderOperationType
from fwego.contrib.builder.workflow_actions.operations import (
    ListBuilderWorkflowActionsPageOperationType,
)
from fwego.core.permission_manager import (
    AllowIfTemplatePermissionManagerType as CoreAllowIfTemplatePermissionManagerType,
)
from fwego.core.registries import PermissionManagerType

User = get_user_model()


class AllowIfTemplatePermissionManagerType(CoreAllowIfTemplatePermissionManagerType):
    """
    Allows read operation on templates.
    """

    BUILDER_OPERATION_ALLOWED_ON_TEMPLATES = [
        ListPagesBuilderOperationType.type,
        ListElementsPageOperationType.type,
        ListBuilderWorkflowActionsPageOperationType.type,
        DispatchDataSourceOperationType.type,
        ListDataSourcesPageOperationType.type,
    ]

    @property
    def OPERATION_ALLOWED_ON_TEMPLATES(self):
        return (
            self.prev_manager_type.OPERATION_ALLOWED_ON_TEMPLATES
            + self.BUILDER_OPERATION_ALLOWED_ON_TEMPLATES
        )

    def __init__(self, prev_manager_type: PermissionManagerType):
        self.prev_manager_type = prev_manager_type
