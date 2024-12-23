from abc import ABC

from fwego.contrib.database.tokens.object_scopes import TokenObjectScopeType
from fwego.core.operations import WorkspaceCoreOperationType
from fwego.core.registries import OperationType


class CreateTokenOperationType(WorkspaceCoreOperationType):
    type = "workspace.create_token"


class TokenOperationType(OperationType, ABC):
    context_scope_name = TokenObjectScopeType.type


class ReadTokenOperationType(TokenOperationType):
    type = "workspace.token.read"


class UpdateTokenOperationType(TokenOperationType):
    type = "workspace.token.update"


class UseTokenOperationType(TokenOperationType):
    type = "workspace.token.use"
