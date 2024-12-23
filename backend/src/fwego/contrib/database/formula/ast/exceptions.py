from django.conf import settings

from fwego.core.formula.parser.exceptions import FwegoFormulaException


class InvalidStringLiteralProvided(FwegoFormulaException):
    pass


class InvalidIntLiteralProvided(FwegoFormulaException):
    pass


class InvalidDecimalLiteralProvided(FwegoFormulaException):
    pass


class UnknownFieldReference(FwegoFormulaException):
    def __init__(self, unknown_field_name):
        super().__init__(
            f"there is no field called {unknown_field_name} but the "
            f"formula contained a reference to it"
        )


class TooLargeStringLiteralProvided(FwegoFormulaException):
    def __init__(self):
        super().__init__(
            f"an embedded string in the formula over the "
            f"maximum length of {settings.MAX_FORMULA_STRING_LENGTH} "
        )
