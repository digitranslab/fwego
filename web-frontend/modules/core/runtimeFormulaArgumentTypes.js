export class FwegoRuntimeFormulaArgumentType {
  /**
   * This function tests if a given value is compatible with its type
   * @param value -  The value being tests
   * @returns {boolean} - If the value is of a valid type
   */
  test(value) {
    return true
  }

  /**
   * This function allows you to parse any given value to its type. This can be useful
   * if the argument is of the wrong type but can be parsed to the correct type.
   *
   * This can also be used to transform the data before it gets to the function call.
   *
   * @param value - The value that is being parsed
   * @returns {*} - The parsed value
   */
  parse(value) {
    return value
  }
}

export class NumberFwegoRuntimeFormulaArgumentType extends FwegoRuntimeFormulaArgumentType {
  test(value) {
    return !isNaN(value)
  }

  parse(value) {
    return parseFloat(value)
  }
}

export class TextFwegoRuntimeFormulaArgumentType extends FwegoRuntimeFormulaArgumentType {
  test(value) {
    return typeof value.toString === 'function'
  }

  parse(value) {
    return value.toString()
  }
}
