from django.urls import re_path

from fwego.api.integrations.views import (
    IntegrationsView,
    IntegrationView,
    MoveIntegrationView,
)

app_name = "fwego.api.integrations"

urlpatterns = [
    re_path(
        r"application/(?P<application_id>[0-9]+)/integrations/$",
        IntegrationsView.as_view(),
        name="list",
    ),
    re_path(
        r"integration/(?P<integration_id>[0-9]+)/$",
        IntegrationView.as_view(),
        name="item",
    ),
    re_path(
        r"integration/(?P<integration_id>[0-9]+)/move/$",
        MoveIntegrationView.as_view(),
        name="move",
    ),
]
