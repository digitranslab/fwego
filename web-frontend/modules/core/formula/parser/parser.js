import antlr4 from 'antlr4'
import FwegoFormulaLexer from '@fwego/modules/core/formula/parser/generated/FwegoFormulaLexer'
import FwegoFormula from '@fwego/modules/core/formula/parser/generated/FwegoFormula'
import { FwegoFormulaParserError } from '@fwego/modules/core/formula/parser/errors'

/**
 * Attempts to parse an input string into a Fwego Formula. If it fails a
 * FwegoFormulaParserError will be raised.
 *
 * @param formula
 * @return {*} The resulting antlr4 parse tree of the formula
 */
export default function parseFwegoFormula(formula) {
  const chars = new antlr4.InputStream(formula)
  const lexer = new FwegoFormulaLexer(chars)
  const tokens = new antlr4.CommonTokenStream(lexer)
  const parser = new FwegoFormula(tokens)
  parser.removeErrorListeners()
  // noinspection JSUnusedLocalSymbols
  parser.addErrorListener({
    syntaxError: (recognizer, offendingSymbol, line, column, msg, err) => {
      throw new FwegoFormulaParserError(offendingSymbol, line, column, msg)
    },
  })
  parser.buildParseTrees = true
  return parser.root()
}

export function getTokenStreamForFormula(formula) {
  const chars = new antlr4.InputStream(formula)
  const lexer = new FwegoFormulaLexer(chars)
  const stream = new antlr4.CommonTokenStream(lexer)
  stream.lazyInit()
  stream.fill()
  return stream
}
