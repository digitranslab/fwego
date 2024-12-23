from django.urls import re_path

from fwego.api.admin.users.views import (
    UserAdminImpersonateView,
    UserAdminView,
    UsersAdminView,
)

app_name = "fwego.api.admin.users"

urlpatterns = [
    re_path(r"^$", UsersAdminView.as_view(), name="list"),
    re_path(r"^impersonate/$", UserAdminImpersonateView.as_view(), name="impersonate"),
    re_path(r"^(?P<user_id>[0-9]+)/$", UserAdminView.as_view(), name="edit"),
]
