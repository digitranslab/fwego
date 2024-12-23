from django.contrib.postgres.fields import ArrayField
from django.db.models import Func, IntegerField, TextField


class FwegoTableRowCount(Func):
    function = "get_fwego_table_row_count"
    output_field = IntegerField()
    arity = 1


class FwegoTableFileUniques(Func):
    template = "(SELECT UNNEST(%(function)s(%(expressions)s)))"
    function = "get_distinct_fwego_table_file_uniques"
    output_field = ArrayField(TextField())
    arity = 1
