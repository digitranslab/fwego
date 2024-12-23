from django.db import models

from fwego.contrib.database.models import Database
from fwego.core.jobs.mixins import JobWithUserIpAddress
from fwego.core.jobs.models import Job
from fwego.core.models import Workspace


class AirtableImportJob(JobWithUserIpAddress, Job):
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        help_text="The workspace where the Airtable base must be imported into.",
    )
    airtable_share_id = models.CharField(
        max_length=200,
        help_text="Public ID of the shared Airtable base that must be imported.",
    )
    database = models.ForeignKey(
        Database,
        null=True,
        on_delete=models.SET_NULL,
        help_text="The imported Fwego database.",
    )
