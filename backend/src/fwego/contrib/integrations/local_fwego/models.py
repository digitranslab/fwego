from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, OrderBy

from fwego.contrib.database.fields.field_filters import FILTER_TYPE_AND
from fwego.contrib.database.fields.models import Field
from fwego.contrib.database.table.models import Table
from fwego.contrib.database.views.models import (
    FILTER_TYPES,
    SORT_ORDER_ASC,
    SORT_ORDER_CHOICES,
    View,
)
from fwego.core.formula.field import FormulaField
from fwego.core.integrations.models import Integration
from fwego.core.services.models import (
    SearchableServiceMixin,
    Service,
    ServiceFilter,
    ServiceSort,
)

User = get_user_model()


class LocalFwegoIntegration(Integration):
    """
    An integration for accessing the local fwego instance. Everything which is
    accessible by the associated user can be accessed with this integration.
    """

    authorized_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class LocalFwegoTableService(Service):
    table = models.ForeignKey(Table, null=True, default=None, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class LocalFwegoViewService(LocalFwegoTableService):
    view = models.ForeignKey(View, null=True, default=None, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class LocalFwegoFilterableServiceMixin(models.Model):
    """
    A mixin which can be applied to LocalFwego services to denote that they're
    filterable, and allows them to control their and/or filter operator type.
    """

    filter_type = models.CharField(
        max_length=3,
        choices=FILTER_TYPES,
        default=FILTER_TYPE_AND,
        help_text="Indicates whether all the rows should apply to all filters (AND) "
        "or to any filter (OR).",
    )

    class Meta:
        abstract = True


class LocalFwegoListRows(
    LocalFwegoViewService, LocalFwegoFilterableServiceMixin, SearchableServiceMixin
):
    """
    A model for the local fwego list rows service configuration data.
    """


class LocalFwegoAggregateRows(
    LocalFwegoViewService, LocalFwegoFilterableServiceMixin, SearchableServiceMixin
):
    """
    A model for the local fwego aggregate rows service configuration data.
    """

    field = models.ForeignKey(
        "database.Field",
        help_text="The aggregated field.",
        null=True,
        on_delete=models.SET_NULL,
    )
    aggregation_type = models.CharField(
        default="", blank=True, max_length=48, help_text="The field aggregation type."
    )


class LocalFwegoGetRow(
    LocalFwegoViewService, LocalFwegoFilterableServiceMixin, SearchableServiceMixin
):
    """
    A model for the local fwego get row service configuration data.
    """

    row_id = FormulaField()


class LocalFwegoUpsertRow(LocalFwegoTableService):
    """
    A model for the local fwego upsert row service configuration data.
    """

    row_id = FormulaField()


class LocalFwegoDeleteRow(LocalFwegoTableService):
    """
    A model for the local fwego delete row service configuration data.
    """

    row_id = FormulaField()


class LocalFwegoTableServiceRefinementManager(models.Manager):
    """
    Manager for the `LocalFwegoTableService` filter and sort models.
    Ensures that we exclude filters and sort with a trashed field.
    """

    use_in_migrations = True

    def get_queryset(self):
        return super().get_queryset().filter(field__trashed=False)


class LocalFwegoTableServiceFilter(ServiceFilter):
    """
    A service filter applicable to a `LocalFwegoTableService` integration service.
    """

    objects_and_trash = models.Manager()
    objects = LocalFwegoTableServiceRefinementManager()

    field = models.ForeignKey(
        "database.Field",
        help_text="The database Field, in the LocalFwegoTableService, "
        "which we would like to filter upon.",
        on_delete=models.CASCADE,
    )
    type = models.CharField(
        max_length=48,
        help_text="Indicates how the field's value must be compared to the filter's "
        "value. The filter is always in this order `field` `type` `value` "
        "(example: `field_1` `contains` `Test`).",
    )
    value = FormulaField(
        default="",
        blank=True,
        help_text="The filter value that must be compared to the field's value.",
    )
    value_is_formula = models.BooleanField(
        default=False,
        help_text="Indicates whether the value is a formula or not.",
    )
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"<LocalFwegoTableServiceFilter {self.field} {self.type} {self.value}>"

    class Meta:
        ordering = ("order", "id")


class LocalFwegoTableServiceSort(ServiceSort):
    """
    A service sort applicable to a `LocalFwegoTableService` integration service.
    """

    objects_and_trash = models.Manager()
    objects = LocalFwegoTableServiceRefinementManager()

    field = models.ForeignKey(
        "database.Field",
        help_text="The database Field, in the LocalFwegoTableService service, "
        "which we would like to sort upon.",
        on_delete=models.CASCADE,
    )
    order_by = models.CharField(
        max_length=4,
        choices=SORT_ORDER_CHOICES,
        help_text="Indicates the sort order direction. ASC (Ascending) is from A to Z "
        "and DESC (Descending) is from Z to A.",
        default=SORT_ORDER_ASC,
    )
    order = models.PositiveIntegerField()

    def __repr__(self):
        return f"<LocalFwegoTableServiceSort {self.field} {self.order_by}>"

    class Meta:
        ordering = ("order", "id")

    def get_order_by(self) -> OrderBy:
        """
        Responsible for returning the `OrderBy` object,
        configured based on the `field` and `order` values.
        """

        field_expr = F(self.field.db_column)

        if self.order_by == SORT_ORDER_ASC:
            field_order_by = field_expr.asc(nulls_first=True)
        else:
            field_order_by = field_expr.desc(nulls_last=True)

        return field_order_by


class LocalFwegoTableServiceFieldMappingManager(models.Manager):
    """
    Manager for the `LocalFwegoTableServiceFieldMapping` model.
    Ensures that we exclude mappings with trashed fields.
    """

    def get_queryset(self):
        return super().get_queryset().filter(field__trashed=False)


class LocalFwegoTableServiceFieldMapping(models.Model):
    """
    Responsible for mapping a `LocalFwegoTableService` subclass's field
    to a specific value, or formula.
    """

    objects_and_trash = models.Manager()
    objects = LocalFwegoTableServiceFieldMappingManager()

    field = models.ForeignKey(
        Field,
        on_delete=models.CASCADE,
        help_text="The Fwego field that this mapping relates to.",
    )
    enabled = models.BooleanField(
        null=True,  # TODO zdm remove me after v1.27
        default=True,
        help_text="Indicates if the field mapping is enabled. If it is disabled, "
        "we will not use the `value` when creating and updating rows.",
    )
    value = FormulaField(default="", help_text="The field mapping's value.")
    service = models.ForeignKey(
        Service,
        related_name="field_mappings",
        on_delete=models.CASCADE,
        help_text="The LocalFwego Service that this field mapping relates to.",
    )
