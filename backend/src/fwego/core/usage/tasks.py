from django.conf import settings

from fwego.config.celery import app
from fwego.core.handler import CoreHandler


@app.task(queue=settings.FWEGO_GROUP_STORAGE_USAGE_QUEUE)
def run_calculate_storage():
    """
    Runs the calculate storage job to keep track of how many mb of memory has been used
    via files by a group
    """

    from fwego.core.usage.handler import UsageHandler

    if CoreHandler().get_settings().track_workspace_usage:
        UsageHandler.calculate_storage_usage()


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        settings.FWEGO_STORAGE_USAGE_JOB_CRONTAB,
        run_calculate_storage.s(),
    )
