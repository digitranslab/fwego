from django.db import transaction

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from fwego.api.decorators import map_exceptions, validate_body
from fwego.api.errors import ERROR_USER_NOT_IN_GROUP
from fwego.api.schemas import get_error_schema
from fwego.contrib.database.api.fields.errors import (
    ERROR_FIELD_SELF_REFERENCE,
    ERROR_WITH_FORMULA,
)
from fwego.contrib.database.api.formula.serializers import (
    TypeFormulaRequestSerializer,
    TypeFormulaResultSerializer,
)
from fwego.contrib.database.api.tables.errors import ERROR_TABLE_DOES_NOT_EXIST
from fwego.contrib.database.fields.dependencies.exceptions import (
    SelfReferenceFieldDependencyError,
)
from fwego.contrib.database.fields.models import FormulaField
from fwego.contrib.database.formula import TypeFormulaOperationType
from fwego.contrib.database.table.exceptions import TableDoesNotExist
from fwego.contrib.database.table.handler import TableHandler
from fwego.core.exceptions import UserNotInWorkspace
from fwego.core.formula import FwegoFormulaException
from fwego.core.handler import CoreHandler


class TypeFormulaView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="table_id",
                location=OpenApiParameter.PATH,
                type=OpenApiTypes.INT,
                description="The table id of the formula field to type.",
            ),
        ],
        tags=["Database table fields"],
        operation_id="type_formula_field",
        description="Calculates and returns the type of the specified formula value. "
        "Does not change the state of the field in any way.",
        request=TypeFormulaRequestSerializer,
        responses={
            200: TypeFormulaResultSerializer,
            400: get_error_schema(
                [
                    "ERROR_USER_NOT_IN_GROUP",
                    "ERROR_REQUEST_BODY_VALIDATION",
                    "ERROR_WITH_FORMULA",
                    "ERROR_FIELD_SELF_REFERENCE",
                ]
            ),
            404: get_error_schema(["ERROR_TABLE_DOES_NOT_EXIST"]),
        },
    )
    @transaction.atomic
    @map_exceptions(
        {
            UserNotInWorkspace: ERROR_USER_NOT_IN_GROUP,
            TableDoesNotExist: ERROR_TABLE_DOES_NOT_EXIST,
            FwegoFormulaException: ERROR_WITH_FORMULA,
            SelfReferenceFieldDependencyError: ERROR_FIELD_SELF_REFERENCE,
        }
    )
    @validate_body(TypeFormulaRequestSerializer)
    def post(self, request, table_id, data):
        """
        Given a formula value for a table returns the type of that formula value.
        """

        table = TableHandler().get_table(table_id)
        CoreHandler().check_permissions(
            request.user,
            TypeFormulaOperationType.type,
            workspace=table.database.workspace,
            context=table,
        )

        field = FormulaField(
            formula=data["formula"], table=table, name=data["name"], order=0
        )
        field.recalculate_internal_fields(raise_if_invalid=True)

        return Response(TypeFormulaResultSerializer(field).data)
