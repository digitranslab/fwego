from django.urls import re_path

from .views import (
    SamlAppAuthProviderAssertionConsumerServiceView,
    SamlAppAuthProviderFwegoInitiatedSingleSignOn,
)

app_name = "fwego_enterprise.api.integrations.common.sso.saml"

urlpatterns = [
    re_path(
        r"acs/$", SamlAppAuthProviderAssertionConsumerServiceView.as_view(), name="acs"
    ),
    re_path(
        r"login/$",
        SamlAppAuthProviderFwegoInitiatedSingleSignOn.as_view(),
        name="login",
    ),
]
