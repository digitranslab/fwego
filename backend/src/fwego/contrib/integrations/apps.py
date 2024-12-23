from django.apps import AppConfig


class IntegrationsConfig(AppConfig):
    name = "fwego.contrib.integrations"

    def ready(self):
        from fwego.contrib.integrations.local_fwego.integration_types import (
            LocalFwegoIntegrationType,
        )
        from fwego.core.integrations.registries import integration_type_registry
        from fwego.core.services.registries import service_type_registry

        integration_type_registry.register(LocalFwegoIntegrationType())

        from fwego.contrib.integrations.local_fwego.service_types import (
            LocalFwegoAggregateRowsUserServiceType,
            LocalFwegoDeleteRowServiceType,
            LocalFwegoGetRowUserServiceType,
            LocalFwegoListRowsUserServiceType,
            LocalFwegoUpsertRowServiceType,
        )

        service_type_registry.register(LocalFwegoGetRowUserServiceType())
        service_type_registry.register(LocalFwegoListRowsUserServiceType())
        service_type_registry.register(LocalFwegoAggregateRowsUserServiceType())
        service_type_registry.register(LocalFwegoUpsertRowServiceType())
        service_type_registry.register(LocalFwegoDeleteRowServiceType())

        import fwego.contrib.integrations.signals  # noqa: F403, F401
