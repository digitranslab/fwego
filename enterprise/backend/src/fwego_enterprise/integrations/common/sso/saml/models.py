from fwego.core.app_auth_providers.models import AppAuthProvider
from fwego_enterprise.sso.saml.models import SamlAuthProviderModelMixin


class SamlAppAuthProviderModel(SamlAuthProviderModelMixin, AppAuthProvider):
    # Restore ordering
    class Meta(AppAuthProvider.Meta):
        ordering = ["id"]
