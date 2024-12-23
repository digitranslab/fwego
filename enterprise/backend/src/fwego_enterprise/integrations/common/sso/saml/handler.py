from fwego_enterprise.integrations.common.sso.saml.models import (
    SamlAppAuthProviderModel,
)
from fwego_enterprise.sso.saml.handler import SamlAuthProviderHandler


class SamlAppAuthProviderHandler(SamlAuthProviderHandler):
    model_class = SamlAppAuthProviderModel
