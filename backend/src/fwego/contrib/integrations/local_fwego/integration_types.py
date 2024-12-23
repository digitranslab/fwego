from collections import defaultdict
from typing import Any, Dict, List, Optional

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from fwego.api.user.serializers import SubjectUserSerializer
from fwego.contrib.database.fields.handler import FieldHandler
from fwego.contrib.database.table.handler import TableHandler
from fwego.contrib.database.views.handler import ViewHandler
from fwego.contrib.integrations.api.local_fwego.serializers import (
    LocalFwegoContextDataSerializer,
)
from fwego.contrib.integrations.local_fwego.models import LocalFwegoIntegration
from fwego.core.integrations.models import Integration
from fwego.core.integrations.registries import IntegrationType
from fwego.core.integrations.types import IntegrationDict
from fwego.core.models import Application

User = get_user_model()


class LocalFwegoIntegrationType(IntegrationType):
    type = "local_fwego"
    model_class = LocalFwegoIntegration

    class SerializedDict(IntegrationDict):
        authorized_user: str

    serializer_field_names = ["context_data", "authorized_user"]
    allowed_fields = ["authorized_user"]

    serializer_field_overrides = {
        "context_data": LocalFwegoContextDataSerializer(read_only=True),
        "authorized_user": SubjectUserSerializer(read_only=True),
    }

    request_serializer_field_names = []
    request_serializer_field_overrides = {}

    def prepare_values(
        self, values: Dict[str, Any], user: AbstractUser
    ) -> Dict[str, Any]:
        """Add the logged in user by default"""

        values["authorized_user"] = user

        return super().prepare_values(values, user)

    def serialize_property(
        self,
        integration: Integration,
        prop_name: str,
        files_zip=None,
        storage=None,
        cache=None,
    ):
        """
        Replace the authorized user property with it's username. Better when loading the
        data later.
        """

        if prop_name == "authorized_user":
            if integration.authorized_user:
                return integration.authorized_user.username
            return None

        return super().serialize_property(
            integration, prop_name, files_zip=files_zip, storage=storage, cache=cache
        )

    def after_template_install(
        self, user: AbstractUser, instance: LocalFwegoIntegration
    ):
        """Add the user who installed the template as authorized user"""

        instance.authorized_user = user
        instance.save()

    def import_serialized(
        self,
        application: Application,
        serialized_values: Dict[str, Any],
        id_mapping: Dict,
        files_zip=None,
        storage=None,
        cache=None,
    ) -> LocalFwegoIntegration:
        """
        Imports a serialized integration. Handles the user part with a cache for
        better performances.
        """

        if cache is None:
            cache = {}

        if "workspace_users" not in cache:
            # In order to prevent a lot of lookup queries in the through table, we want
            # to fetch all the users and add it to a temporary in memory cache
            # containing a mapping of user per email
            cache["workspace_users"] = {
                user.username: user
                for user in User.objects.filter(
                    workspaceuser__workspace_id=id_mapping["import_workspace_id"]
                )
            }

        username = serialized_values.pop("authorized_user", None)

        if username:
            serialized_values["authorized_user"] = cache["workspace_users"].get(
                username, None
            )

        return super().import_serialized(
            application,
            serialized_values,
            id_mapping,
            files_zip=files_zip,
            storage=storage,
            cache=cache,
        )

    def enhance_queryset(self, queryset):
        return queryset.select_related("authorized_user")

    def get_context_data(self, instance: LocalFwegoIntegration) -> Optional[Dict]:
        return {
            "databases": LocalFwegoIntegrationType.get_local_fwego_databases(
                instance
            )
        }

    @staticmethod
    def get_local_fwego_databases(integration: LocalFwegoIntegration) -> List:
        """
        This method returns the databases that the user has access to in a query
        efficient way while also checking for permissions. It will do so by fetching
        all the tables at ones, and then group them by database.

        A side effect of this solution is that databases without tables don't show up
        in this list.
        """

        if not integration.application.workspace_id:
            return []

        user = integration.specific.authorized_user
        workspace = integration.application.workspace

        tables = TableHandler().list_workspace_tables(user, workspace)

        views = ViewHandler().list_workspace_views(user, workspace)

        fields = FieldHandler().list_workspace_fields(user, workspace)

        views_by_table = defaultdict(list)
        [
            views_by_table[view.table_id].append(view)
            for view in views
            if view.get_type().can_filter or view.get_type().can_sort
        ]

        fields_by_table = defaultdict(list)
        [fields_by_table[field.table_id].append(field) for field in fields]

        database_map = {}
        for table in tables:
            if table.database not in database_map:
                database_map[table.database] = table.database
                database_map[table.database].tables = []
                database_map[table.database].views = []

            table.fields = fields_by_table[table.id]

            database_map[table.database].tables.append(table)
            database_map[table.database].views += views_by_table.get(table.id, [])

        databases = list(database_map.values())
        databases.sort(key=lambda x: x.order)

        # Sort views. Tables are already sorted.
        [db.views.sort(key=lambda x: x.order) for db in databases]

        return databases
