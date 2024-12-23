r"""
The database formula module can parse, type and generate Django expressions given a
Fwego Formula string like:

```fwego_formula
CONCAT(UPPER(LOWER('test')), "test\"", 'test\'") -- evaluates to `testtest"test'`
```

This module consists of 4 sub modules which are responsible for:
    1. parser: taking a raw Fwego Formula string input, syntax checking it, parsing
       it and converting it to the internal Fwego Expression format.
    2. ast: the definition of the internal Fwego Expression abstract syntax tree (
       AST). Essentially a graph which can be used to represent a Fwego Formula
       neatly and perform operations over.
    3. types: given an Fwego Expression figures out the type of it. Or more
       specifically what postgres database column type should be used to store the
       result of the Fwego Expression.
    4. expression_generator: takes a typed Fwego Expression and generates a Django
       Expression object which calculates the result of executing the formula.

Also you can find the grammar definitions for the Fwego Formula language may be found
in the
root folder formula_lang along with the scripts to generate the antlr4 parser found in
fwego.contrib.formula.parser.generated .

The abstract syntax tree abstraction is used to decouple the specifics of the antlr4
parser from the specifics of turning a Fwego formula into generated SQL. It lets us
separate the various concerns cleanly but also provides future extensibility. For
example we could create another parser module which takes an another formula language
different from the Fwego Formula language, but generates a Fwego Formula AST
allowing use of that language in Fwego easily.
"""

from fwego.contrib.database.formula.ast.tree import FwegoExpression
from fwego.contrib.database.formula.handler import FormulaHandler
from fwego.contrib.database.formula.operations import TypeFormulaOperationType
from fwego.contrib.database.formula.types.exceptions import (
    InvalidFormulaType,
    get_invalid_field_and_table_formula_error,
)
from fwego.contrib.database.formula.types.formula_type import (
    FwegoFormulaInvalidType,
    FwegoFormulaType,
)
from fwego.contrib.database.formula.types.formula_types import (
    FWEGO_FORMULA_ARRAY_TYPE_CHOICES,
    FWEGO_FORMULA_TYPE_ALLOWED_FIELDS,
    FWEGO_FORMULA_TYPE_CHOICES,
    FWEGO_FORMULA_TYPE_REQUEST_SERIALIZER_FIELD_NAMES,
    FWEGO_FORMULA_TYPE_SERIALIZER_FIELD_NAMES,
    FwegoFormulaArrayType,
    FwegoFormulaBooleanType,
    FwegoFormulaCharType,
    FwegoFormulaDateType,
    FwegoFormulaLinkType,
    FwegoFormulaMultipleSelectType,
    FwegoFormulaNumberType,
    FwegoFormulaSingleSelectType,
    FwegoFormulaTextType,
    literal,
)

__all__ = [
    FormulaHandler,
    FwegoExpression,
    FwegoFormulaType,
    FwegoFormulaInvalidType,
    FwegoFormulaTextType,
    FwegoFormulaNumberType,
    FwegoFormulaCharType,
    FwegoFormulaLinkType,
    FwegoFormulaDateType,
    FwegoFormulaBooleanType,
    FwegoFormulaArrayType,
    FwegoFormulaSingleSelectType,
    FwegoFormulaMultipleSelectType,
    FWEGO_FORMULA_TYPE_ALLOWED_FIELDS,
    FWEGO_FORMULA_TYPE_SERIALIZER_FIELD_NAMES,
    FWEGO_FORMULA_TYPE_REQUEST_SERIALIZER_FIELD_NAMES,
    FWEGO_FORMULA_TYPE_CHOICES,
    FWEGO_FORMULA_ARRAY_TYPE_CHOICES,
    literal,
    TypeFormulaOperationType,
    InvalidFormulaType,
    get_invalid_field_and_table_formula_error,
]
