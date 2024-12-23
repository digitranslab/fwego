import pytest


@pytest.mark.django_db
def test_premium_app_installed(settings):
    assert "fwego_premium" in settings.INSTALLED_APPS
