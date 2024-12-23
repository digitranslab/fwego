from fwego.contrib.dashboard.data_sources.models import DashboardDataSource
from fwego.contrib.integrations.local_fwego.models import (
    LocalFwegoAggregateRows,
    LocalFwegoListRows,
)


class DashboardDataSourceFixtures:
    def create_dashboard_local_fwego_list_rows_data_source(self, **kwargs):
        return self.create_dashboard_data_source(
            service_model_class=LocalFwegoListRows, **kwargs
        )

    def create_dashboard_local_fwego_aggregate_rows_data_source(self, **kwargs):
        return self.create_dashboard_data_source(
            service_model_class=LocalFwegoAggregateRows, **kwargs
        )

    def create_dashboard_data_source(
        self,
        dashboard=None,
        user=None,
        service_model_class=None,
        order=None,
        name=None,
        **kwargs,
    ):
        if not dashboard:
            if user is None:
                user = self.create_user()
            dashboard = self.create_dashboard_application(user=user)

        service = kwargs.pop("service", None)

        if service is None:
            if not service_model_class:
                service_model_class = LocalFwegoAggregateRows

            integrations_args = kwargs.pop("integration_args", {})
            integrations_args["application"] = dashboard
            service = self.create_service(
                service_model_class, integration_args=integrations_args, **kwargs
            )

        if order is None:
            order = DashboardDataSource.get_last_order(dashboard)

        if name is None:
            name = self.fake.unique.word()

        data_source = DashboardDataSource.objects.create(
            dashboard=dashboard, name=name, service=service, order=order
        )

        return data_source
