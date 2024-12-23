import pytest

from fwego.contrib.database.webhooks.actions import (
    CreateWebhookActionType,
    DeleteWebhookActionType,
    UpdateWebhookActionType,
)
from fwego.contrib.database.webhooks.models import TableWebhook
from fwego.core.action.registries import action_type_registry


@pytest.mark.django_db
def test_create_webhook_action_type(data_fixture):
    user = data_fixture.create_user()
    table = data_fixture.create_database_table(user=user)
    webhook_data = {
        "url": "https://fwego.io/endpoint",
        "name": "My Webhook",
        "include_all_events": True,
        "request_method": "POST",
    }
    webhook = action_type_registry.get(CreateWebhookActionType.type).do(
        user, table, **webhook_data
    )
    assert webhook.url == webhook_data["url"]
    assert webhook.name == webhook_data["name"]
    assert webhook.include_all_events == webhook_data["include_all_events"]
    assert webhook.request_method == webhook_data["request_method"]


@pytest.mark.django_db
def test_update_webhook_action_type(data_fixture):
    user = data_fixture.create_user()
    table = data_fixture.create_database_table(user=user)
    webhook = data_fixture.create_table_webhook(
        table=table,
        events=["rows.created"],
        headers={"Fwego-test-1": "Value 1", "Fwego-test-2": "Value 2"},
    )

    webhook = action_type_registry.get(UpdateWebhookActionType.type).do(
        user=user,
        webhook=webhook,
        name="Test",
        url="https://fwego.io/endpoint",
        include_all_events=False,
        request_method="GET",
        use_user_field_names=False,
        active=False,
    )
    assert webhook.name == "Test"
    assert webhook.url == "https://fwego.io/endpoint"
    assert webhook.include_all_events is False
    assert webhook.request_method == "GET"
    assert webhook.use_user_field_names is False
    assert webhook.active is False


@pytest.mark.django_db
def test_delete_webhook_action_type(data_fixture):
    user = data_fixture.create_user()
    table = data_fixture.create_database_table(user=user)
    webhook = data_fixture.create_table_webhook(table=table)
    action_type_registry.get(DeleteWebhookActionType.type).do(user, webhook)
    assert TableWebhook.objects.count() == 0
