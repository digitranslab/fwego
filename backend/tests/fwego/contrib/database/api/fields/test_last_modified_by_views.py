from django.shortcuts import reverse

import pytest
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from fwego.contrib.database.fields.handler import FieldHandler
from fwego.contrib.database.fields.models import LastModifiedByField
from fwego.test_utils.helpers import is_dict_subset


@pytest.mark.field_last_modified_by
@pytest.mark.django_db
def test_api_create_last_modified_by_field_type(api_client, data_fixture):
    user, token = data_fixture.create_user_and_token(
        email="test@test.nl", password="password", first_name="Test1"
    )
    database = data_fixture.create_database_application(user=user, name="Placeholder")
    table = data_fixture.create_database_table(name="Example", database=database)

    response = api_client.post(
        reverse("api:database:fields:list", kwargs={"table_id": table.id}),
        {
            "name": "last modified by",
            "type": "last_modified_by",
        },
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )
    response_json = response.json()
    assert response.status_code == HTTP_200_OK
    assert response_json["name"] == "last modified by"
    assert response_json["type"] == "last_modified_by"
    assert LastModifiedByField.objects.all().count() == 1


@pytest.mark.field_last_modified_by
@pytest.mark.django_db
def test_api_update_last_modified_by_field_type(api_client, data_fixture):
    workspace = data_fixture.create_workspace()
    user, token = data_fixture.create_user_and_token(
        email="test@test.nl",
        password="password",
        first_name="Test1",
        workspace=workspace,
    )
    database = data_fixture.create_database_application(
        user=user, name="Placeholder", workspace=workspace
    )
    table = data_fixture.create_database_table(name="Example", database=database)
    field = data_fixture.create_last_modified_by_field(
        table=table, order=1, name="Last modified by", primary=True
    )

    response = api_client.patch(
        reverse("api:database:fields:item", kwargs={"field_id": field.id}),
        {"name": "Last modified by renamed"},
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )

    response_json = response.json()
    assert response.status_code == HTTP_200_OK
    assert response_json["name"] == "Last modified by renamed"
    assert response_json["type"] == "last_modified_by"


@pytest.mark.field_last_modified_by
@pytest.mark.django_db
def test_api_delete_last_modified_by_field_type(api_client, data_fixture):
    user, token = data_fixture.create_user_and_token(
        email="test@test.nl", password="password", first_name="Test1"
    )
    database = data_fixture.create_database_application(user=user, name="Placeholder")
    table = data_fixture.create_database_table(name="Example", database=database)
    field = data_fixture.create_last_modified_by_field(
        table=table,
        order=1,
        name="Last modified by",
    )

    response = api_client.delete(
        reverse("api:database:fields:item", kwargs={"field_id": field.id}),
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )

    assert response.status_code == HTTP_200_OK
    field.refresh_from_db()
    assert field.trashed is True


@pytest.mark.field_last_modified_by
@pytest.mark.api_rows
@pytest.mark.django_db
def test_api_create_last_modified_by_field_type_row(api_client, data_fixture):
    user, token = data_fixture.create_user_and_token()
    database = data_fixture.create_database_application(user=user, name="Placeholder")
    table = data_fixture.create_database_table(name="Example", database=database)
    text_field = data_fixture.create_text_field(table=table)
    field_handler = FieldHandler()
    field = field_handler.create_field(
        user=user,
        table=table,
        type_name="last_modified_by",
        name="modified by",
    )

    # can't set the field value directly
    response = api_client.post(
        reverse("api:database:rows:list", kwargs={"table_id": table.id}),
        {f"field_{field.id}": user.id},
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )
    response_json = response.json()
    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response_json["error"] == "ERROR_REQUEST_BODY_VALIDATION"

    # value will be set when other field value is set
    response = api_client.post(
        reverse("api:database:rows:list", kwargs={"table_id": table.id}),
        {f"field_{text_field.id}": "text"},
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )
    response_json = response.json()
    assert response.status_code == HTTP_200_OK
    assert response_json[f"field_{field.id}"] == {
        "name": user.first_name,
        "id": user.id,
    }


@pytest.mark.field_last_modified_by
@pytest.mark.api_rows
@pytest.mark.django_db
def test_update_last_modified_by_field_type_row(api_client, data_fixture):
    user, token = data_fixture.create_user_and_token()
    database = data_fixture.create_database_application(user=user, name="Placeholder")
    table = data_fixture.create_database_table(name="Example", database=database)
    text_field = data_fixture.create_text_field(table=table)
    field_handler = FieldHandler()
    field = field_handler.create_field(
        user=user,
        table=table,
        type_name="last_modified_by",
        name="modified by",
    )

    model = table.get_model()
    row = model.objects.create(**{f"field_{text_field.id}": "text"})

    # can't set the field value directly
    response = api_client.patch(
        reverse(
            "api:database:rows:item", kwargs={"table_id": table.id, "row_id": row.id}
        ),
        {f"field_{field.id}": user.id},
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )
    response_json = response.json()
    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response_json["error"] == "ERROR_REQUEST_BODY_VALIDATION"

    # value will be set when other field value is set
    response = api_client.patch(
        reverse(
            "api:database:rows:item", kwargs={"table_id": table.id, "row_id": row.id}
        ),
        {f"field_{text_field.id}": "updated text"},
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )
    response_json = response.json()
    assert response.status_code == HTTP_200_OK
    assert response_json[f"field_{field.id}"] == {
        "name": user.first_name,
        "id": user.id,
    }


@pytest.mark.field_last_modified_by
@pytest.mark.api_rows
@pytest.mark.django_db
def test_last_modified_by_field_type_batch_insert_rows(api_client, data_fixture):
    workspace = data_fixture.create_workspace()
    user, token = data_fixture.create_user_and_token(
        email="test@test.nl",
        password="password",
        first_name="Test1",
        workspace=workspace,
    )
    user2 = data_fixture.create_user(workspace=workspace)
    user3 = data_fixture.create_user(workspace=workspace)
    database = data_fixture.create_database_application(
        user=user, workspace=workspace, name="Placeholder"
    )
    table = data_fixture.create_database_table(name="Example", database=database)
    field = data_fixture.create_last_modified_by_field(
        table=table, order=1, name="Last modified by", primary=True
    )
    text_field = data_fixture.create_text_field(table=table, order=2, name="Text")

    # can't set the field value directly
    response = api_client.post(
        reverse("api:database:rows:batch", kwargs={"table_id": table.id}),
        {
            "items": [
                {f"field_{field.id}": user.id},
            ]
        },
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )
    response_json = response.json()
    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response_json["error"] == "ERROR_REQUEST_BODY_VALIDATION"

    # value will be set when other field value is set
    response = api_client.post(
        reverse("api:database:rows:batch", kwargs={"table_id": table.id}),
        {
            "items": [
                {f"field_{text_field.id}": "text"},
            ]
        },
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )

    assert response.status_code == HTTP_200_OK
    assert is_dict_subset(
        {"items": [{f"field_{field.id}": {"id": user.id, "name": user.first_name}}]},
        response.json(),
    )


@pytest.mark.field_last_modified_by
@pytest.mark.api_rows
@pytest.mark.django_db
def test_last_modified_by_field_type_batch_update_rows(api_client, data_fixture):
    workspace = data_fixture.create_workspace()
    user, token = data_fixture.create_user_and_token(
        email="test@test.nl",
        password="password",
        first_name="Test1",
        workspace=workspace,
    )
    user2 = data_fixture.create_user(workspace=workspace)
    user3 = data_fixture.create_user(workspace=workspace)
    database = data_fixture.create_database_application(
        user=user, workspace=workspace, name="Placeholder"
    )
    table = data_fixture.create_database_table(name="Example", database=database)
    field = data_fixture.create_last_modified_by_field(
        table=table, order=1, name="Last modified by", primary=True
    )
    text_field = data_fixture.create_text_field(table=table, order=2, name="Text")
    model = table.get_model()
    row1 = model.objects.create(last_modified_by=user2)
    row2 = model.objects.create(last_modified_by=user3)
    row3 = model.objects.create(last_modified_by=user3)

    # can't set the field value directly
    response = api_client.patch(
        reverse("api:database:rows:batch", kwargs={"table_id": table.id}),
        {
            "items": [
                {"id": row1.id, f"field_{text_field.id}": "new text"},
                {"id": row2.id, f"field_{field.id}": user.id},
            ]
        },
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )
    response_json = response.json()
    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response_json["error"] == "ERROR_REQUEST_BODY_VALIDATION"

    # value will be set when other field value is set
    response = api_client.patch(
        reverse("api:database:rows:batch", kwargs={"table_id": table.id}),
        {
            "items": [
                {"id": row1.id, f"field_{text_field.id}": "new text"},
                {"id": row2.id, f"field_{text_field.id}": "new text"},
            ]
        },
        format="json",
        HTTP_AUTHORIZATION=f"JWT {token}",
    )

    assert response.status_code == HTTP_200_OK
    response_json = response.json()

    # assert response_json == {}
    assert response_json["items"][0][f"field_{field.id}"]["id"] == user.id
    assert response_json["items"][1][f"field_{field.id}"]["id"] == user.id
    assert getattr(row3, f"field_{field.id}") == user3
