from django.contrib.auth import get_user_model

from fwego.contrib.database.fields.operations import ListFieldsOperationType
from fwego.contrib.database.operations import ListTablesDatabaseTableOperationType
from fwego.contrib.database.rows.operations import ReadDatabaseRowOperationType
from fwego.contrib.database.table.operations import ListRowsDatabaseTableOperationType
from fwego.contrib.database.views.operations import (
    ListAggregationsViewOperationType,
    ListViewDecorationOperationType,
    ListViewsOperationType,
    ReadAggregationsViewOperationType,
    ReadViewFieldOptionsOperationType,
    ReadViewOperationType,
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

    DATABASE_OPERATION_ALLOWED_ON_TEMPLATES = [
        ListTablesDatabaseTableOperationType.type,
        ListFieldsOperationType.type,
        ListRowsDatabaseTableOperationType.type,
        ListViewsOperationType.type,
        ReadDatabaseRowOperationType.type,
        ReadViewOperationType.type,
        ReadViewFieldOptionsOperationType.type,
        ListViewDecorationOperationType.type,
        ListAggregationsViewOperationType.type,
        ReadAggregationsViewOperationType.type,
    ]

    @property
    def OPERATION_ALLOWED_ON_TEMPLATES(self):
        return (
            self.prev_manager_type.OPERATION_ALLOWED_ON_TEMPLATES
            + self.DATABASE_OPERATION_ALLOWED_ON_TEMPLATES
        )

    def __init__(self, prev_manager_type: PermissionManagerType):
        self.prev_manager_type = prev_manager_type
