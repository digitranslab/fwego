from django.urls import re_path

from fwego.api.admin.dashboard.views import AdminDashboardView

app_name = "fwego.api.admin.dashboard"

urlpatterns = [
    re_path(r"^$", AdminDashboardView.as_view(), name="dashboard"),
]
