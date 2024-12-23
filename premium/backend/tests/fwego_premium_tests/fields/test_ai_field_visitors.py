import pytest
from fwego_premium.fields.visitors import replace_field_id_references

from fwego.core.formula import FwegoFormulaSyntaxError


@pytest.mark.field_ai
def test_replace_field_id_references():
    assert (
        replace_field_id_references("get('fields.field_1')", {1: 2})
        == "get('fields.field_2')"
    )


@pytest.mark.field_ai
def test_replace_multiple_field_id_references():
    assert (
        replace_field_id_references(
            "concat(get('fields.field_1'),get('fields.field_12'))", {1: 2, 3: 4, 12: 13}
        )
        == "concat(get('fields.field_2'),get('fields.field_13'))"
    )


@pytest.mark.field_ai
def test_field_id_references_invalid_id():
    with pytest.raises(KeyError):
        replace_field_id_references("get('fields.field_1')", {})


@pytest.mark.field_ai
def test_field_id_references_invalid_formula():
    with pytest.raises(FwegoFormulaSyntaxError):
        replace_field_id_references("get('fields.field_1'))", {})
