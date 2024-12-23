from typing import Any

from fwego.core.formula.parser.exceptions import (
    FwegoFormulaException,
    FwegoFormulaSyntaxError,
    MaximumFormulaSizeError,
)
from fwego.core.formula.parser.generated.FwegoFormula import FwegoFormula
from fwego.core.formula.parser.generated.FwegoFormulaVisitor import (
    FwegoFormulaVisitor,
)
from fwego.core.formula.types import FormulaContext, FunctionCollection

__all__ = [
    FwegoFormulaException,
    MaximumFormulaSizeError,
    FwegoFormulaVisitor,
    FwegoFormula,
    FwegoFormulaSyntaxError,
]

from fwego.core.formula.parser.parser import get_parse_tree_for_formula
from fwego.core.formula.parser.python_executor import FwegoPythonExecutor


def resolve_formula(
    formula: str, functions: FunctionCollection, formula_context: FormulaContext
) -> Any:
    """
    Helper to resolve a formula given the formula_context.

    :param formula: the formula itself.
    :param formula_context: A dict like object that contains the data that can
        be accessed in from the formulas.
    :return: the formula result.
    """

    # If we receive a blank formula string, don't attempt to parse it.
    if not formula:
        return ""

    tree = get_parse_tree_for_formula(formula)
    return FwegoPythonExecutor(functions, formula_context).visit(tree)
