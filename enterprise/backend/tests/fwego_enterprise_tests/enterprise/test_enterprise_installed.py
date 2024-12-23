import pytest


@pytest.mark.django_db
def test_enterprise_app_installed(settings):
    assert "fwego_enterprise" in settings.INSTALLED_APPS
