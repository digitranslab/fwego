import ssl
from typing import Optional
from urllib.parse import urlparse

from redis.asyncio.connection import Connection, RedisSSLContext

from .base import *  # noqa: F403, F401


# Required to get Channels v4 working with Heroku Redis
# See https://github.com/django/channels_redis/issues/235
class CustomSSLConnection(Connection):
    def __init__(
        self,
        ssl_context: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.ssl_context = RedisSSLContext(ssl_context)


class RedisSSLContext:  # noqa: F811
    __slots__ = ("context",)

    def __init__(
        self,
        ssl_context,
    ):
        self.context = ssl_context

    def get(self):
        return self.context


REDIS_TLS_URL = os.getenv("REDIS_TLS_URL", REDIS_URL)  # noqa: F405

if REDIS_PROTOCOL == "rediss" or "rediss" in REDIS_TLS_URL:  # noqa: F405
    # We need to set the certificate check to None, otherwise it is not compatible with
    # the `heroku-redis:mini` addon. The URL generated by that addon is over a
    # secured connection with a self signed certificate. The redis broker could fail
    # if the certificate can't be verified.
    CELERY_REDBEAT_REDIS_USE_SSL = {"ssl_cert_reqs": ssl.CERT_NONE}

    parsed_redis_url = urlparse(REDIS_TLS_URL)
    ssl_context = ssl.SSLContext()
    ssl_context.check_hostname = False
    CHANNELS_REDIS_HOST = {
        "host": parsed_redis_url.hostname,
        "port": parsed_redis_url.port,
        "username": parsed_redis_url.username,
        "password": parsed_redis_url.password,
        "connection_class": CustomSSLConnection,
        "ssl_context": ssl_context,
    }
    CHANNEL_LAYERS["default"]["CONFIG"]["hosts"] = [CHANNELS_REDIS_HOST]  # noqa: F405

    # The built in healthcheck does not handle customizing ssl_cert_reqs...
    INSTALLED_APPS.remove("health_check.contrib.redis")  # noqa: F405
    for CACHE in CACHES.values():  # noqa: F405
        CACHE["OPTIONS"]["CONNECTION_POOL_KWARGS"] = {"ssl_cert_reqs": None}

# Set the limit of the connection pool based on the amount of workers that must be
# started with a limit of 10, which is the default value. This is needed because the
# `heroku-redis:mini` doesn't accept more than 20 connections.
CELERY_BROKER_POOL_LIMIT = min(
    4 * int(os.getenv("FWEGO_AMOUNT_OF_WORKERS", "1")), 10  # noqa: F405
)
CELERY_REDIS_MAX_CONNECTIONS = min(
    4 * int(os.getenv("FWEGO_AMOUNT_OF_WORKERS", "1")), 10  # noqa: F405
)

HEROKU_ENABLED = True
