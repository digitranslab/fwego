from django.urls import re_path

from fwego.contrib.database.api.formula.views import TypeFormulaView

app_name = "fwego.contrib.database.api.export"

urlpatterns = [
    re_path(
        r"(?P<table_id>[0-9]+)/type/$",
        TypeFormulaView.as_view(),
        name="type_formula",
    ),
]
