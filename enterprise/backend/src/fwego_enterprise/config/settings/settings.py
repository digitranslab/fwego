import os

from fwego.config.settings.utils import enum_member_by_value
from fwego_enterprise.secure_file_serve.constants import SecureFileServePermission


def setup(settings):
    """
    This function is called after Fwego as setup its own Django settings file but
    before Django starts. Read and modify provided settings object as appropriate
    just like you would in a normal Django settings file. E.g.:

    settings.INSTALLED_APPS += ["some_custom_plugin_dep"]
    for db, value in settings.DATABASES:
        value['engine'] = 'some custom engine'
    """

    settings.FWEGO_ENTERPRISE_USER_SOURCE_COUNTING_TASK_INTERVAL_MINUTES = int(
        os.getenv("FWEGO_ENTERPRISE_USER_SOURCE_COUNTING_TASK_INTERVAL_MINUTES", "")
        or 2 * 60
    )

    settings.FWEGO_ENTERPRISE_USER_SOURCE_COUNTING_CACHE_TTL_SECONDS = int(
        # Default TTL is 120 minutes: 60 seconds * 120
        os.getenv("FWEGO_ENTERPRISE_USER_SOURCE_COUNTING_CACHE_TTL_SECONDS")
        or 7200
    )

    settings.FWEGO_ENTERPRISE_AUDIT_LOG_CLEANUP_INTERVAL_MINUTES = int(
        os.getenv("FWEGO_ENTERPRISE_AUDIT_LOG_CLEANUP_INTERVAL_MINUTES", "")
        or 24 * 60
    )

    settings.FWEGO_ENTERPRISE_AUDIT_LOG_RETENTION_DAYS = int(
        os.getenv("FWEGO_ENTERPRISE_AUDIT_LOG_RETENTION_DAYS", "") or 365
    )

    # Set this to True to enable users to login with auth providers different than
    # the one they were originally created with.
    settings.FWEGO_ALLOW_MULTIPLE_SSO_PROVIDERS_FOR_SAME_ACCOUNT = bool(
        os.getenv("FWEGO_ALLOW_MULTIPLE_SSO_PROVIDERS_FOR_SAME_ACCOUNT", False)
    )

    serve_files_through_backend_permission = (
        os.getenv("FWEGO_SERVE_FILES_THROUGH_BACKEND_PERMISSION", "")
        or SecureFileServePermission.DISABLED.value
    )

    settings.FWEGO_SERVE_FILES_THROUGH_BACKEND_PERMISSION = enum_member_by_value(
        SecureFileServePermission, serve_files_through_backend_permission
    )

    # If the expire seconds is not set to a number greater than zero, the signature will
    # never expire.
    settings.FWEGO_SERVE_FILES_THROUGH_BACKEND_EXPIRE_SECONDS = (
        int(os.getenv("FWEGO_SERVE_FILES_THROUGH_BACKEND_EXPIRE_SECONDS", "") or 0)
        or None
    )

    serve_files_through_backend = bool(
        os.getenv("FWEGO_SERVE_FILES_THROUGH_BACKEND", False)
    )
    if serve_files_through_backend:
        settings.STORAGES["default"][
            "BACKEND"
        ] = "fwego_enterprise.secure_file_serve.storage.EnterpriseFileStorage"

    settings.FWEGO_SERVE_FILES_THROUGH_BACKEND = serve_files_through_backend
