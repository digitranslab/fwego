import abc
from typing import Generic, TypeVar

from fwego.contrib.database.formula.ast import tree

Y = TypeVar("Y")
X = TypeVar("X")


class FwegoFormulaASTVisitor(abc.ABC, Generic[Y, X]):
    @abc.abstractmethod
    def visit_string_literal(self, string_literal: "tree.FwegoStringLiteral[Y]") -> X:
        pass

    @abc.abstractmethod
    def visit_function_call(self, function_call: "tree.FwegoFunctionCall[Y]") -> X:
        pass

    @abc.abstractmethod
    def visit_int_literal(self, int_literal: "tree.FwegoIntegerLiteral[Y]") -> X:
        pass

    @abc.abstractmethod
    def visit_field_reference(
        self, field_reference: "tree.FwegoFieldReference[Y]"
    ) -> X:
        pass

    @abc.abstractmethod
    def visit_decimal_literal(
        self, decimal_literal: "tree.FwegoDecimalLiteral[Y]"
    ) -> X:
        pass

    @abc.abstractmethod
    def visit_boolean_literal(
        self, boolean_literal: "tree.FwegoBooleanLiteral[Y]"
    ) -> X:
        pass
