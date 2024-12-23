import { RuntimeFunctionCollection } from '@fwego/modules/core/functionCollection'
import { TestApp } from '@fwego/test/helpers/testApp'
import { FromTipTapVisitor } from '@fwego/modules/core/formula/tiptap/fromTipTapVisitor'
import testCases from '@fwego_test_cases/tip_tap_visitor_cases.json'

describe('fromTipTapVisitor', () => {
  let testApp = null
  beforeAll(() => {
    testApp = new TestApp()
  })

  testCases.forEach(({ formula, content }) => {
    it('should return the expected formula', () => {
      const functionCollection = new RuntimeFunctionCollection(
        testApp.store.$registry
      )
      const result = new FromTipTapVisitor(functionCollection).visit(content)
      expect(result).toEqual(formula)
    })
  })
})
