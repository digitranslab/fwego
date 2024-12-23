from django.urls import include, path

from fwego_premium.api import urls as api_urls
from fwego_premium.license.plugin import LicensePlugin

from fwego.core.registries import Plugin


class PremiumPlugin(Plugin):
    type = "premium"

    def get_api_urls(self):
        return [
            path("", include(api_urls, namespace=self.type)),
        ]

    def get_license_plugin(self, cache_queries: bool = False) -> LicensePlugin:
        return LicensePlugin(cache_queries)
