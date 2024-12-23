from django.apps import AppConfig


class WSConfig(AppConfig):
    name = "fwego.ws"

    def ready(self):
        import fwego.ws.signals  # noqa: F403, F401
