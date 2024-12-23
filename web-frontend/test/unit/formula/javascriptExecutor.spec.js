import parseFwegoFormula from '@fwego/modules/core/formula/parser/parser'
import JavascriptExecutor from '@fwego/modules/core/formula/parser/javascriptExecutor'
import {
  VALID_FORMULA_TESTS,
  INVALID_FORMULA_TESTS,
} from '@fwego_test_cases/formula_runtime_cases'
import { TestApp } from '@fwego/test/helpers/testApp'

describe('JavascriptExecutor', () => {
  let testApp = null
  beforeAll(() => {
    testApp = new TestApp()
  })

  test.each(VALID_FORMULA_TESTS)(
    'should correctly resolve the formula %s',
    ({ formula, result, context }) => {
      const tree = parseFwegoFormula(formula)
      expect(
        new JavascriptExecutor(
          {
            get(name) {
              return testApp.store.$registry.get('runtimeFormulaFunction', name)
            },
          },
          context
        ).visit(tree)
      ).toEqual(result)
    }
  )

  test.each(INVALID_FORMULA_TESTS)(
    'should correctly raise an error for formula %s',
    ({ formula, context }) => {
      const tree = parseFwegoFormula(formula)
      expect(() =>
        new JavascriptExecutor(
          {
            get(name) {
              return testApp.store.$registry.get('runtimeFormulaFunction', name)
            },
          },
          context
        ).visit(tree)
      ).toThrow()
    }
  )
})
