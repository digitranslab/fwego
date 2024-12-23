from django.db import models

from fwego.contrib.dashboard.data_sources.models import DashboardDataSource
from fwego.contrib.dashboard.widgets.models import SummaryWidget, Widget
from fwego.core.models import Application

__all__ = ["Dashboard", "DashboardDataSource", "SummaryWidget", "Widget"]


class Dashboard(Application):
    description = models.TextField(blank=True, db_default="")

    def get_parent(self):
        # Parent is the Application here even if it's at the "same" level
        # but it's a more generic type
        return self.application_ptr
