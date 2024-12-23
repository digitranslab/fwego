from django.contrib.auth.hashers import make_password

from fwego.core.user_sources.registries import user_source_type_registry
from fwego_enterprise.integrations.local_fwego.models import (
    LocalFwegoPasswordAppAuthProvider,
)


def populate_local_fwego_test_data(data_fixture, role_name="", extra_fields=None):
    user = data_fixture.create_user()
    workspace = data_fixture.create_workspace(user=user)
    builder = data_fixture.create_builder_application(user=user, workspace=workspace)
    published_builder = data_fixture.create_builder_application(workspace=None)
    domain = data_fixture.create_builder_custom_domain(
        builder=builder, published_to=published_builder
    )
    database = data_fixture.create_database_application(workspace=workspace)
    data_fixture.create_database_table(database=database)
    integration = data_fixture.create_local_fwego_integration(
        application=published_builder, user=user
    )

    columns = [
        ("Email", "text"),
        ("Name", "text"),
        ("Password", "text"),
        ("Role", "text"),
    ]
    extra_args = []
    if extra_fields is not None:
        for item in extra_fields:
            columns.append((item["name"], item["field_type"]))
        extra_args = [i["value"] for i in extra_fields]

    table, fields, rows = data_fixture.build_table(
        user=user,
        columns=columns,
        rows=[
            [
                "test@fwego.io",
                "Test",
                make_password("super not secret"),
                role_name,
                *extra_args,
            ],
            [
                "test2@fwego.io",
                "Test2",
                make_password("super not secret"),
                role_name,
                *extra_args,
            ],
            [
                "test3@fwego.io",
                "Test3",
                make_password("super not secret"),
                role_name,
                *extra_args,
            ],
            ["test4@fwego.io", "Test4", None, role_name, *extra_args],
        ],
    )

    email_field, name_field, password_field, role_field, *other_fields = fields

    local_fwego_user_source_type = user_source_type_registry.get("local_fwego")

    user_source = data_fixture.create_user_source(
        local_fwego_user_source_type.model_class,
        application=published_builder,
        integration=integration,
        table=table,
        email_field=email_field,
        name_field=name_field,
        role_field=role_field,
    )

    app_auth_provider = data_fixture.create_app_auth_provider(
        LocalFwegoPasswordAppAuthProvider,
        user_source=user_source,
        password_field=password_field,
    )

    return {
        "user_source": user_source,
        "auth_provider": app_auth_provider,
        "domain": domain,
        "user_table": table,
        "user": user,
        "rows": rows,
        "fields": fields,
    }
