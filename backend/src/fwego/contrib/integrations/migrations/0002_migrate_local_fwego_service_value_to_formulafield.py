import django.db.models.manager
from django.db import migrations

import fwego.contrib.integrations.local_fwego.models
import fwego.core.formula.field


class Migration(migrations.Migration):
    dependencies = [
        ("integrations", "0001_squashed_0011_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="localfwegotableservicefilter",
            managers=[
                ("objects_and_trash", django.db.models.manager.Manager()),
                (
                    "objects",
                    fwego.contrib.integrations.local_fwego.models.LocalFwegoTableServiceRefinementManager(),
                ),
            ],
        ),
        migrations.AlterModelManagers(
            name="localfwegotableservicesort",
            managers=[
                ("objects_and_trash", django.db.models.manager.Manager()),
                (
                    "objects",
                    fwego.contrib.integrations.local_fwego.models.LocalFwegoTableServiceRefinementManager(),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="localfwegotableservicefilter",
            name="value",
            field=fwego.core.formula.field.FormulaField(
                blank=True,
                default="",
                help_text="The filter value that must be compared to the field's value.",
            ),
        ),
    ]
