from django.template.exceptions import TemplateDoesNotExist

import pytest

from fwego.core.emails import BaseEmailMessage


class WithoutTemplateNameEmail(BaseEmailMessage):
    subject = "Test"


class WithoutSubjectEmail(BaseEmailMessage):
    template_name = "test.html"


class WrongTemplateEmail(BaseEmailMessage):
    subject = "Test"
    template_name = "test.html"


class SimpleResetPasswordEmail(BaseEmailMessage):
    subject = "Reset password"
    template_name = "fwego/core/user/reset_password.html"


@pytest.mark.django_db
def test_base_email_message():
    with pytest.raises(NotImplementedError):
        WithoutSubjectEmail("test@fwego.io")

    with pytest.raises(NotImplementedError):
        WithoutSubjectEmail("test@fwego.io")

    with pytest.raises(TemplateDoesNotExist):
        WrongTemplateEmail("test@fwego.io")

    email = SimpleResetPasswordEmail(["test@fwego.io"])
    context = email.get_context()
    assert "public_backend_url" in context
    assert "public_backend_hostname" in context
    assert "public_web_frontend_url" in context
    assert "public_web_frontend_hostname" in context
    assert "fwego_embedded_share_url" in context
    assert "fwego_embedded_share_hostname" in context
    assert email.get_from_email() == "no-reply@localhost"
    assert email.get_subject() == "Reset password"
