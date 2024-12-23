from fwego.contrib.integrations.local_fwego.models import (
    LocalFwegoAggregateRows,
    LocalFwegoDeleteRow,
    LocalFwegoGetRow,
    LocalFwegoListRows,
    LocalFwegoTableServiceFilter,
    LocalFwegoTableServiceSort,
    LocalFwegoUpsertRow,
)


class ServiceFixtures:
    def create_local_fwego_get_row_service(self, **kwargs) -> LocalFwegoGetRow:
        service = self.create_service(LocalFwegoGetRow, **kwargs)
        return service

    def create_local_fwego_list_rows_service(self, **kwargs) -> LocalFwegoListRows:
        service = self.create_service(LocalFwegoListRows, **kwargs)
        return service

    def create_local_fwego_upsert_row_service(
        self, **kwargs
    ) -> LocalFwegoUpsertRow:
        service = self.create_service(LocalFwegoUpsertRow, **kwargs)
        return service

    def create_local_fwego_delete_row_service(
        self, **kwargs
    ) -> LocalFwegoDeleteRow:
        service = self.create_service(LocalFwegoDeleteRow, **kwargs)
        return service

    def create_local_fwego_aggregate_rows_service(
        self, **kwargs
    ) -> LocalFwegoAggregateRows:
        service = self.create_service(LocalFwegoAggregateRows, **kwargs)
        return service

    def create_local_fwego_table_service_filter(
        self, **kwargs
    ) -> LocalFwegoTableServiceFilter:
        if "type" not in kwargs:
            kwargs["type"] = "equal"
        if "order" not in kwargs:
            kwargs["order"] = 0
        return LocalFwegoTableServiceFilter.objects.create(**kwargs)

    def create_local_fwego_table_service_sort(
        self, **kwargs
    ) -> LocalFwegoTableServiceSort:
        return LocalFwegoTableServiceSort.objects.create(**kwargs)

    def create_service(self, model_class, **kwargs):
        if "integration" not in kwargs:
            integrations_args = kwargs.pop("integration_args", {})
            integration = self.create_local_fwego_integration(**integrations_args)
        else:
            integration = kwargs.pop("integration", None)
            kwargs.pop("integration_args", None)

        service = model_class.objects.create(integration=integration, **kwargs)

        return service
