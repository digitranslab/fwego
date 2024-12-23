from django.db import models

from fwego.core.jobs.mixins import JobWithUserIpAddress
from fwego.core.jobs.models import Job
from fwego.core.models import Snapshot


class CreateSnapshotJob(JobWithUserIpAddress, Job):
    snapshot: Snapshot = models.ForeignKey(
        Snapshot, null=True, on_delete=models.SET_NULL
    )


class RestoreSnapshotJob(JobWithUserIpAddress, Job):
    snapshot: Snapshot = models.ForeignKey(
        Snapshot, null=True, on_delete=models.SET_NULL
    )
