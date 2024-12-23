from django.urls import re_path

from .views import (
    AdminAuthProvidersLoginUrlView,
    AssertionConsumerServiceView,
    FwegoInitiatedSingleSignOn,
)

app_name = "fwego_enterprise.api.sso.saml"

urlpatterns = [
    re_path(r"^acs/$", AssertionConsumerServiceView.as_view(), name="acs"),
    re_path(r"^login/$", FwegoInitiatedSingleSignOn.as_view(), name="login"),
    re_path(
        r"^login-url/$", AdminAuthProvidersLoginUrlView.as_view(), name="login_url"
    ),
]
