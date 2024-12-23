import { TestApp } from '@fwego/test/helpers/testApp'
import { RuntimeFunctionCollection } from '@fwego/modules/core/functionCollection'
import { ToTipTapVisitor } from '@fwego/modules/core/formula/tiptap/toTipTapVisitor'
import parseFwegoFormula from '@fwego/modules/core/formula/parser/parser'
import testCases from '@fwego_test_cases/tip_tap_visitor_cases.json'

describe('toTipTapVisitor', () => {
  let testApp = null
  beforeAll(() => {
    testApp = new TestApp()
  })

  testCases.forEach(({ formula, content }) => {
    it(`should return the expected formula for ${formula}`, () => {
      const functionCollection = new RuntimeFunctionCollection(
        testApp.store.$registry
      )
      // We don't want to test empty formula
      if (formula) {
        const tree = parseFwegoFormula(formula)
        const result = new ToTipTapVisitor(functionCollection).visit(tree)
        expect(result).toEqual(content)
      }
    })
  })
})
