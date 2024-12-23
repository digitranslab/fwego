from datetime import datetime
from typing import Any, Dict, Optional, Type

from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

from fwego.core.action.registries import ActionType
from fwego.core.action.signals import ActionCommandType, action_done
from fwego.core.models import Workspace

from .handler import AuditLogHandler


@receiver(action_done)
def log_action(
    sender,
    user: AbstractUser,
    action_type: Type[ActionType],
    action_params: Dict[str, Any],
    action_timestamp: datetime,
    action_command_type: ActionCommandType,
    action_uuid: str,
    workspace: Optional[Workspace] = None,
    **kwargs,
):
    AuditLogHandler.log_action(
        user,
        action_type,
        action_params,
        action_timestamp,
        action_command_type,
        action_uuid=action_uuid,
        workspace=workspace,
        **kwargs,
    )
