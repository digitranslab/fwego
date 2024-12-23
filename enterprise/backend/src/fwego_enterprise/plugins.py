from django.urls import include, path

from fwego.core.registries import Plugin
from fwego_enterprise.api import urls as api_urls


class EnterprisePlugin(Plugin):
    type = "enterprise"

    def get_api_urls(self):
        return [
            path("", include(api_urls, namespace=self.type)),
        ]
