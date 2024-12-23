from fwego.contrib.builder.formula_property_extractor import FormulaFieldVisitor
from fwego.core.formula.parser.exceptions import FwegoFormulaSyntaxError
from fwego.core.formula.parser.parser import get_parse_tree_for_formula
from fwego.core.registry import InstanceWithFormulaMixin
from fwego.core.utils import merge_dicts_no_duplicates


class BuilderInstanceWithFormulaMixin(InstanceWithFormulaMixin):
    def extract_formula_properties(self, instance, **kwargs):
        result = {}

        for formula in self.formula_generator(instance):
            if not formula:
                continue

            try:
                tree = get_parse_tree_for_formula(formula)
            except FwegoFormulaSyntaxError:
                continue

            result = merge_dicts_no_duplicates(
                result, FormulaFieldVisitor(**kwargs).visit(tree)
            )

        return result
