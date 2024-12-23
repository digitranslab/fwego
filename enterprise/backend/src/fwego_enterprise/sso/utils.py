from fwego_premium.license.exceptions import FeaturesNotAvailableError
from fwego_premium.license.handler import LicenseHandler

from fwego_enterprise.features import SSO


def is_sso_feature_active():
    return LicenseHandler.instance_has_feature(SSO)


def check_sso_feature_is_active_or_raise():
    if not is_sso_feature_active():
        raise FeaturesNotAvailableError()
