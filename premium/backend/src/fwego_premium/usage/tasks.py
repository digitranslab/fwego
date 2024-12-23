from django.conf import settings

from fwego_premium.usage.handler import PremiumUsageHandler

from fwego.config.celery import app
from fwego.core.handler import CoreHandler


@app.task(queue=settings.FWEGO_ROLE_USAGE_QUEUE)
def run_calculate_seats():
    if CoreHandler().get_settings().track_workspace_usage:
        PremiumUsageHandler.calculate_per_workspace_seats_taken()


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        settings.FWEGO_SEAT_USAGE_JOB_CRONTAB,
        run_calculate_seats.s(),
    )
