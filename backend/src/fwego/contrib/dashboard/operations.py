from abc import ABC

from fwego.core.registries import OperationType


class DashboardOperationType(OperationType, ABC):
    context_scope_name = "dashboard"
