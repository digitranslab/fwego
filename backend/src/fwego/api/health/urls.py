from django.http import HttpResponse
from django.urls import re_path

from fwego.api.health.views import (
    CeleryQueueSizeExceededView,
    EmailTesterView,
    FullHealthCheckView,
)

app_name = "fwego.api.health"


def public_health_check(request):
    return HttpResponse("OK")


urlpatterns = [
    re_path(r"full/$", FullHealthCheckView.as_view(), name="full_health_check"),
    re_path(r"email/$", EmailTesterView.as_view(), name="email_tester"),
    re_path(
        r"celery-queue/$",
        CeleryQueueSizeExceededView.as_view(),
        name="celery_queue_size_exceeded",
    ),
    re_path("^$", public_health_check, name="public_health_check"),
]
