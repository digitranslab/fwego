import parseFwegoFormula from '@fwego/modules/core/formula/parser/parser'
import { FwegoFormulaParserError } from '@fwego/modules/core/formula/parser/errors'

describe('Fwego Formula Tests', () => {
  const validFormulas = ["lower('test')", "upper('test')"]
  const invalidFormulas = [
    ['a', FwegoFormulaParserError],
    ['12ssda3', FwegoFormulaParserError],
  ]

  test.each(validFormulas)(
    'valid fwego formulas do not raise a parser error',
    (value) => {
      expect(parseFwegoFormula(value)).toBeTruthy()
    }
  )

  test.each(invalidFormulas)(
    'invalid fwego formulas raise a parser error',
    (value, exception) => {
      expect(() => parseFwegoFormula(value)).toThrow(exception)
    }
  )
})
