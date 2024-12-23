from antlr4 import CommonTokenStream, InputStream
from antlr4.BufferedTokenStream import BufferedTokenStream
from antlr4.error.ErrorListener import ErrorListener

from fwego.core.formula.parser.exceptions import FwegoFormulaSyntaxError
from fwego.core.formula.parser.generated.FwegoFormula import FwegoFormula
from fwego.core.formula.parser.generated.FwegoFormulaLexer import (
    FwegoFormulaLexer,
)


class FwegoFormulaErrorListener(ErrorListener):
    """
    A custom error listener as ANTLR's default error listen does not raise an
    exception if a syntax error is found in a parse tree.
    """

    # noinspection PyPep8Naming
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        msg = msg.replace("<EOF>", "the end of the formula")
        message = f"Invalid syntax at line {line}, col {column}: {msg}"
        raise FwegoFormulaSyntaxError(message)


def get_token_stream_for_formula(formula: str) -> BufferedTokenStream:
    lexer = FwegoFormulaLexer(InputStream(formula))
    stream = BufferedTokenStream(lexer)
    stream.lazyInit()
    stream.fill()
    return stream


def get_parse_tree_for_formula(formula: str):
    """
    WARNING: This function is directly used by migration code. Please ensure
    backwards compatibility .
    """

    lexer = FwegoFormulaLexer(InputStream(formula))
    stream = CommonTokenStream(lexer)
    parser = FwegoFormula(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(FwegoFormulaErrorListener())
    return parser.root()


# noinspection DuplicatedCode
def convert_string_literal_token_to_string(string_literal, is_single_q):
    literal_without_outer_quotes = string_literal[1:-1]
    quote = "'" if is_single_q else '"'
    return literal_without_outer_quotes.replace("\\" + quote, quote)


def convert_string_to_string_literal_token(string, is_single_q):
    quote = "'" if is_single_q else '"'
    escaped = string.replace(quote, "\\" + quote)
    return quote + escaped + quote
