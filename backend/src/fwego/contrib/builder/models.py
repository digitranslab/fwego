from functools import cached_property

from django.db import models

from fwego.contrib.builder.domains.models import Domain, PublishDomainJob
from fwego.contrib.builder.elements.models import Element
from fwego.contrib.builder.pages.models import Page
from fwego.contrib.builder.theme.models import (
    ButtonThemeConfigBlock,
    ColorThemeConfigBlock,
    TypographyThemeConfigBlock,
)
from fwego.core.models import Application, UserFile

__all__ = [
    "Builder",
    "Page",
    "Domain",
    "PublishDomainJob",
    "Element",
    "ColorThemeConfigBlock",
    "TypographyThemeConfigBlock",
    "ButtonThemeConfigBlock",
]


class Builder(Application):
    favicon_file = models.ForeignKey(
        UserFile,
        on_delete=models.SET_NULL,
        null=True,
        related_name="builder_favicon_file",
    )

    login_page = models.OneToOneField(
        Page,
        on_delete=models.SET_NULL,
        help_text="The login page for this application. This is related to the visibility settings of builder pages.",
        related_name="login_page",
        null=True,
    )

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new:
            from fwego.contrib.builder.pages.handler import PageHandler

            # Create the shared page
            PageHandler().create_shared_page(self)

    def get_parent(self):
        # Parent is the Application here even if it's at the "same" level
        # but it's a more generic type
        return self.application_ptr

    @cached_property
    def shared_page(self):
        from fwego.contrib.builder.pages.handler import PageHandler

        return PageHandler().get_shared_page(self)
