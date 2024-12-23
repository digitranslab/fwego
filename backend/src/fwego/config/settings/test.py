# flake8: noqa: F405
from copy import deepcopy

from .base import *  # noqa: F403, F401

TESTS = True

# This is a hardcoded key for test runs only.
SECRET_KEY = "test_hardcoded_secret_key"  # nosec
SIMPLE_JWT["SIGNING_KEY"] = "test_hardcoded_jwt_signing_key"

CELERY_BROKER_BACKEND = "memory"
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}

# Open a second database connection that can be used to test transactions.
DATABASES["default-copy"] = deepcopy(DATABASES["default"])

USER_FILES_DIRECTORY = "user_files"
USER_THUMBNAILS_DIRECTORY = "thumbnails"
USER_THUMBNAILS = {"tiny": [21, 21]}

# Make sure that we are not using the `MEDIA_URL` environment variable because that
# could break the tests. They are expecting it to be 'http://localhost:8000/media/'
# because that is default value in `base.py`.
MEDIA_URL = "http://localhost:8000/media/"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "KEY_PREFIX": "fwego-default-cache",
        "VERSION": VERSION,
    },
    GENERATED_MODEL_CACHE_NAME: {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "KEY_PREFIX": f"fwego-{GENERATED_MODEL_CACHE_NAME}-cache",
        "VERSION": None,
    },
    CACHALOT_CACHE: {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "KEY_PREFIX": f"fwego-{CACHALOT_CACHE}-cache",
        "VERSION": None,
    },
}

# Disable the default throttle classes because ConcurrentUserRequestsThrottle is
# using redis and it will cause errors when running the tests.
# Look into tests.fwego.api.test_api_utils.py if you need to test the throttle
REST_FRAMEWORK["DEFAULT_THROTTLE_CLASSES"] = []

if "cachalot" not in INSTALLED_APPS:
    install_cachalot()

CACHALOT_ENABLED = False

BUILDER_PUBLICLY_USED_PROPERTIES_CACHE_TTL_SECONDS = 10

AUTO_INDEX_VIEW_ENABLED = False
# For ease of testing tests assume this setting is set to this. Set it explicitly to
# prevent any dev env config from breaking the tests.
FWEGO_PERSONAL_VIEW_LOWEST_ROLE_ALLOWED = "VIEWER"

# Ensure the tests never run with the concurrent middleware unless they add it in to
# prevent failures caused by the middleware itself
if "fwego.middleware.ConcurrentUserRequestsMiddleware" in MIDDLEWARE:
    MIDDLEWARE.remove("fwego.middleware.ConcurrentUserRequestsMiddleware")


FWEGO_OPENAI_API_KEY = None
FWEGO_OPENAI_ORGANIZATION = None
FWEGO_OPENAI_MODELS = []
FWEGO_OPENROUTER_API_KEY = None
FWEGO_OPENROUTER_ORGANIZATION = None
FWEGO_OPENROUTER_MODELS = []
FWEGO_ANTHROPIC_API_KEY = None
FWEGO_ANTHROPIC_MODELS = []
FWEGO_MISTRAL_API_KEY = None
FWEGO_MISTRAL_MODELS = []
FWEGO_OLLAMA_HOST = None
FWEGO_OLLAMA_MODELS = []

PUBLIC_BACKEND_URL = "http://localhost:8000"
PUBLIC_WEB_FRONTEND_URL = "http://localhost:3000"
FWEGO_EMBEDDED_SHARE_URL = "http://localhost:3000"

FEATURE_FLAGS = "*"

# We must allow this because we're connecting to the same database in the tests.
FWEGO_PREVENT_POSTGRESQL_DATA_SYNC_CONNECTION_TO_DATABASE = False

# Make sure that default storage is used for the tests.
BASE_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
STORAGES["default"] = {"BACKEND": BASE_FILE_STORAGE}

FWEGO_LOGIN_ACTION_LOG_LIMIT = RateLimit.from_string("1000/s")

FWEGO_WEBHOOKS_ALLOW_PRIVATE_ADDRESS = False