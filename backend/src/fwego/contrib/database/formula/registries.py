from fwego.core.formula.parser.exceptions import FormulaFunctionTypeDoesNotExist
from fwego.core.registry import Registry


class FwegoFormulaFunctionRegistry(Registry):
    name = "formula_function"
    does_not_exist_exception_class = FormulaFunctionTypeDoesNotExist


formula_function_registry = FwegoFormulaFunctionRegistry()
