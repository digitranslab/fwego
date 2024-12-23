import { Registerable } from '@fwego/modules/core/registry'

export class FwegoFunctionDefinition extends Registerable {
  getDescription() {
    throw new Error(
      'Not implemented error. This method should return the functions description.'
    )
  }

  getSyntaxUsage() {
    throw new Error(
      'Not implemented error. This method should return a string showing the syntax ' +
        'of the function.'
    )
  }

  getExamples() {
    throw new Error(
      'Not implemented error. This method should return list of strings showing ' +
        'example usage of the function.'
    )
  }

  getFormulaType() {
    throw new Error(
      'Not implemented error. This method should return the fwego formula type ' +
        'string of the function.'
    )
  }

  isOperator() {
    return false
  }

  getOperator() {
    return ''
  }

  isRollupCompatible(targetFieldType) {
    return false
  }
}

export class FwegoUpper extends FwegoFunctionDefinition {
  static getType() {
    return 'upper'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.upperDescription')
  }

  getSyntaxUsage() {
    return ['upper(text)']
  }

  getExamples() {
    return ["upper('a') = 'A'"]
  }

  getFormulaType() {
    return 'text'
  }
}
export class FwegoLower extends FwegoFunctionDefinition {
  static getType() {
    return 'lower'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.lowerDescription')
  }

  getSyntaxUsage() {
    return ['lower(text)']
  }

  getExamples() {
    return ["lower('A') = 'a'"]
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoSplitPart extends FwegoFunctionDefinition {
  static getType() {
    return 'split_part'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.splitPartDescription')
  }

  getSyntaxUsage() {
    return ['split_part(text, delimiter, position)']
  }

  getExamples() {
    return ["split_part('John, Jane, Michael', ', ', 2) = 'Jane'"]
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoConcat extends FwegoFunctionDefinition {
  static getType() {
    return 'concat'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.concatDescription')
  }

  getSyntaxUsage() {
    return ['concat(any, any, ...)']
  }

  getExamples() {
    return ["concat('A', 1, 1=2) = 'A1false'"]
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoAdd extends FwegoFunctionDefinition {
  static getType() {
    return 'add'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.addDescription')
  }

  getSyntaxUsage() {
    return [
      'number + number',
      'text + text',
      'date + duration',
      'duration + duration',
      'duration + date',
      'add(number, number)',
    ]
  }

  getExamples() {
    return ['1+1 = 2', "'a' + 'b' = 'ab'"]
  }

  getFormulaType() {
    return 'special'
  }

  isOperator() {
    return true
  }

  getOperator() {
    return '+'
  }
}

export class FwegoMinus extends FwegoFunctionDefinition {
  static getType() {
    return 'minus'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.minusDescription')
  }

  getSyntaxUsage() {
    return [
      'number - number',
      'minus(number, number)',
      'date - date',
      'date - duration',
      'duration - duration',
    ]
  }

  getExamples() {
    return ['3-1 = 2']
  }

  getFormulaType() {
    return 'special'
  }

  isOperator() {
    return true
  }

  getOperator() {
    return '-'
  }
}

export class FwegoMultiply extends FwegoFunctionDefinition {
  static getType() {
    return 'multiply'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.multiplyDescription')
  }

  getSyntaxUsage() {
    return [
      'number * number',
      'multiply(number, number)',
      'multiply(duration, number)',
      'multiply(number, duration)',
    ]
  }

  getExamples() {
    return ['2*5 = 10']
  }

  getFormulaType() {
    return 'number'
  }

  isOperator() {
    return true
  }

  getOperator() {
    return '*'
  }
}

export class FwegoDivide extends FwegoFunctionDefinition {
  static getType() {
    return 'divide'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.divideDescription')
  }

  getSyntaxUsage() {
    return [
      'number / number',
      'divide(number, number)',
      'divide(duration, number)',
    ]
  }

  getExamples() {
    return ['10/2 = 5']
  }

  getFormulaType() {
    return 'number'
  }

  isOperator() {
    return true
  }

  getOperator() {
    return '/'
  }
}

export class FwegoEqual extends FwegoFunctionDefinition {
  static getType() {
    return 'equal'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.equalDescription')
  }

  getSyntaxUsage() {
    return ['any = any', 'equal(any, any)']
  }

  getExamples() {
    return ['1=1', "'a' = 'a'"]
  }

  getFormulaType() {
    return 'boolean'
  }

  isOperator() {
    return true
  }

  getOperator() {
    return '='
  }
}

export class FwegoHasOption extends FwegoFunctionDefinition {
  static getType() {
    return 'has_option'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.hasOptionDescription')
  }

  getSyntaxUsage() {
    return [
      'has_option(multiple select, text)',
      'has_option(lookup(link row, single select), text)',
    ]
  }

  getExamples() {
    return [
      "has_option(field('multiple select'), 'option_a')",
      "has_option(lookup(field('link row'), field('single select')), 'option_a')",
    ]
  }

  getFormulaType() {
    return 'boolean'
  }

  isOperator() {
    return true
  }
}

export class FwegoIf extends FwegoFunctionDefinition {
  static getType() {
    return 'if'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.ifDescription')
  }

  getSyntaxUsage() {
    return ['if(bool, any, any)']
  }

  getExamples() {
    return ["if(field('text field') = 'on', 'it is on', 'it is off')"]
  }

  getFormulaType() {
    return 'boolean'
  }
}

export class FwegoToText extends FwegoFunctionDefinition {
  static getType() {
    return 'totext'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.toTextDescription')
  }

  getSyntaxUsage() {
    return ['totext(any)']
  }

  getExamples() {
    return ["totext(10) = '10'"]
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoDatetimeFormat extends FwegoFunctionDefinition {
  static getType() {
    return 'datetime_format'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.datetimeFormatDescription')
  }

  getSyntaxUsage() {
    return ['datetime_format(date, text)']
  }

  getExamples() {
    return ["datetime_format(field('date field'), 'YYYY')"]
  }

  getFormulaType() {
    return 'date'
  }
}

export class FwegoDatetimeFormatTz extends FwegoFunctionDefinition {
  static getType() {
    return 'datetime_format_tz'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.datetimeFormatTzDescription')
  }

  getSyntaxUsage() {
    return ['datetime_format_tz(date, text, text)']
  }

  getExamples() {
    return [
      "datetime_format_tz(field('date field'), 'YYYY-MM-DD HH24:MI', 'Europe/Amsterdam')",
    ]
  }

  getFormulaType() {
    return 'date'
  }
}

export class FwegoEncodeUri extends FwegoFunctionDefinition {
  static getType() {
    return 'encode_uri'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.encodeUriDescription')
  }

  getSyntaxUsage() {
    return ['encode_uri(text)']
  }

  getExamples() {
    return [
      "encode_uri('http://example.com/wiki/Señor') = 'http://example.com/wiki/Se%c3%b1or'",
    ]
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoEncodeUriComponent extends FwegoFunctionDefinition {
  static getType() {
    return 'encode_uri_component'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.encodeUriComponentDescription')
  }

  getSyntaxUsage() {
    return ['encode_uri_component(text)']
  }

  getExamples() {
    return ["encode_uri_component('Hello World') = 'Hello%20World'"]
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoToNumber extends FwegoFunctionDefinition {
  static getType() {
    return 'tonumber'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.toNumberDescription')
  }

  getSyntaxUsage() {
    return ['tonumber(text)']
  }

  getExamples() {
    return ["tonumber('10') = 10"]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoField extends FwegoFunctionDefinition {
  static getType() {
    return 'field'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.fieldDescription')
  }

  getSyntaxUsage() {
    return ["field('a field name')"]
  }

  getExamples() {
    return ["field('my text field') = 'flag'"]
  }

  getFormulaType() {
    return 'special'
  }
}

export class FwegoLookup extends FwegoFunctionDefinition {
  static getType() {
    return 'lookup'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.lookupDescription')
  }

  getSyntaxUsage() {
    return ["lookup('a link row field name', 'field name in other the table')"]
  }

  getExamples() {
    return [
      "lookup('link row field', 'first name') = lookup('link row field', 'last name')",
    ]
  }

  getFormulaType() {
    return 'special'
  }
}

export class FwegoIsBlank extends FwegoFunctionDefinition {
  static getType() {
    return 'isblank'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.isBlankDescription')
  }

  getSyntaxUsage() {
    return ['isblank(any)']
  }

  getExamples() {
    return ["isblank('10') "]
  }

  getFormulaType() {
    return 'boolean'
  }
}

export class FwegoDurationToSeconds extends FwegoFunctionDefinition {
  static getType() {
    return 'toseconds'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.durationToSecondsDescription')
  }

  getSyntaxUsage() {
    return ['toseconds(duration)']
  }

  getExamples() {
    return ["toseconds(duration('10 minutes'))"]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoSecondsToDuration extends FwegoFunctionDefinition {
  static getType() {
    return 'toduration'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.secondsToDurationDescription')
  }

  getSyntaxUsage() {
    return ['toduration(number)']
  }

  getExamples() {
    return ['toduration(60)']
  }

  getFormulaType() {
    return 'duration'
  }
}

export class FwegoIsNull extends FwegoFunctionDefinition {
  static getType() {
    return 'is_null'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.isNullDescription')
  }

  getSyntaxUsage() {
    return ['is_null(any)']
  }

  getExamples() {
    return ["is_null('10') "]
  }

  getFormulaType() {
    return 'boolean'
  }
}

export class FwegoT extends FwegoFunctionDefinition {
  static getType() {
    return 't'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.tDescription')
  }

  getSyntaxUsage() {
    return ['t(any)']
  }

  getExamples() {
    return ['t(10)']
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoNot extends FwegoFunctionDefinition {
  static getType() {
    return 'not'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.notDescription')
  }

  getSyntaxUsage() {
    return ['not(boolean)']
  }

  getExamples() {
    return ['not(true) = false', 'not(10=2) = true']
  }

  getFormulaType() {
    return 'boolean'
  }
}

export class FwegoGreaterThan extends FwegoFunctionDefinition {
  static getType() {
    return 'greater_than'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.greaterThanDescription')
  }

  getSyntaxUsage() {
    return ['any > any']
  }

  getExamples() {
    return [
      '1 > 2 = false',
      "if(field('a') > field('b'), 'a is bigger', 'b is bigger or equal')",
    ]
  }

  getFormulaType() {
    return 'boolean'
  }

  isOperator() {
    return true
  }

  getOperator() {
    return '>'
  }
}

export class FwegoGreaterThanOrEqual extends FwegoFunctionDefinition {
  static getType() {
    return 'greater_than_or_equal'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.greaterThanOrEqualDescription')
  }

  getSyntaxUsage() {
    return ['any >= any']
  }

  getExamples() {
    return [
      '1 >= 1 = true',
      "if(field('a') >= field('b'), 'a is bigger or equal', 'b is smaller')",
    ]
  }

  getFormulaType() {
    return 'boolean'
  }

  isOperator() {
    return true
  }

  getOperator() {
    return '>='
  }
}

export class FwegoLessThan extends FwegoFunctionDefinition {
  static getType() {
    return 'less_than'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.lessThanDescription')
  }

  getSyntaxUsage() {
    return ['any < any']
  }

  getExamples() {
    return [
      '2 < 1 = false',
      "if(field('a') < field('b'), 'a is smaller', 'b is bigger or equal')",
    ]
  }

  getFormulaType() {
    return 'boolean'
  }

  isOperator() {
    return true
  }

  getOperator() {
    return '<'
  }
}

export class FwegoLessThanOrEqual extends FwegoFunctionDefinition {
  static getType() {
    return 'less_than_or_equal'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.lessThanOrEqualDescription')
  }

  getSyntaxUsage() {
    return ['any <= any']
  }

  getExamples() {
    return [
      '1 <= 1 = true',
      "if(field('a') <= field('b'), 'a smaller', 'b is greater than or equal')",
    ]
  }

  getFormulaType() {
    return 'boolean'
  }

  isOperator() {
    return true
  }

  getOperator() {
    return '<='
  }
}

export class FwegoNow extends FwegoFunctionDefinition {
  static getType() {
    return 'now'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.nowDescription')
  }

  getSyntaxUsage() {
    return ['now()']
  }

  getExamples() {
    return ['now() > todate("2021-12-12 13:00:00", "YYYY-MM-DD HH24:MI:SS")']
  }

  getFormulaType() {
    return 'date'
  }
}

export class FwegoToday extends FwegoFunctionDefinition {
  static getType() {
    return 'today'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.todayDescription')
  }

  getSyntaxUsage() {
    return ['today()']
  }

  getExamples() {
    return ['today() > todate("2021-12-12", "YYYY-MM-DD")']
  }

  getFormulaType() {
    return 'date'
  }
}

export class FwegoToDate extends FwegoFunctionDefinition {
  static getType() {
    return 'todate'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.toDateDescription')
  }

  getSyntaxUsage() {
    return ['todate(text, text)']
  }

  getExamples() {
    return ["todate('20210101', 'YYYYMMDD')"]
  }

  getFormulaType() {
    return 'date'
  }
}

export class FwegoToDateTz extends FwegoFunctionDefinition {
  static getType() {
    return 'todate_tz'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.toDateTzDescription')
  }

  getSyntaxUsage() {
    return ['todate_tz(text, text, text)']
  }

  getExamples() {
    return ["todate_tz('20210101', 'YYYYMMDD', 'Europe/Amsterdam')"]
  }

  getFormulaType() {
    return 'date'
  }
}

export class FwegoDay extends FwegoFunctionDefinition {
  static getType() {
    return 'day'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.dayDescription')
  }

  getSyntaxUsage() {
    return ['day(date)']
  }

  getExamples() {
    return ["day(todate('20210101', 'YYYYMMDD')) = 1"]
  }

  getFormulaType() {
    return 'date'
  }
}

export class FwegoDateDiff extends FwegoFunctionDefinition {
  static getType() {
    return 'date_diff'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.dateDiffDescription')
  }

  getSyntaxUsage() {
    return ['date_diff(text, date, date)']
  }

  getExamples() {
    return [
      "date_diff('yy', todate('2000-01-01', 'YYYY-MM-DD'), todate('2020-01-01'," +
        " 'YYYY-MM-DD')) = 20",
    ]
  }

  getFormulaType() {
    return 'date'
  }
}

export class FwegoAnd extends FwegoFunctionDefinition {
  static getType() {
    return 'and'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.andDescription')
  }

  getSyntaxUsage() {
    return ['and(boolean, boolean)']
  }

  getExamples() {
    return [
      'and(true, false) = false',
      'true && true = true',
      "and(field('first test'), field('second test'))",
    ]
  }

  getFormulaType() {
    return 'boolean'
  }

  getOperator() {
    return '&&'
  }
}

export class FwegoOr extends FwegoFunctionDefinition {
  static getType() {
    return 'or'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.orDescription')
  }

  getSyntaxUsage() {
    return ['or(boolean, boolean)']
  }

  getExamples() {
    return [
      'or(true, false) = true',
      'and(true, true) = true',
      "or(field('first test'), field('second test'))",
    ]
  }

  getFormulaType() {
    return 'boolean'
  }
}

export class FwegoDateInterval extends FwegoFunctionDefinition {
  static getType() {
    return 'date_interval'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.dateIntervalDescription')
  }

  getSyntaxUsage() {
    return ['date_interval(text)']
  }

  getExamples() {
    return ["date_interval('1 year')", "date_interval('2 seconds')"]
  }

  getFormulaType() {
    return 'duration'
  }
}

export class FwegoReplace extends FwegoFunctionDefinition {
  static getType() {
    return 'replace'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.replaceDescription')
  }

  getSyntaxUsage() {
    return ['replace(text, text, text)']
  }

  getExamples() {
    return ['replace("test a b c test", "test", "1") = "1 a b c 1"']
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoSearch extends FwegoFunctionDefinition {
  static getType() {
    return 'search'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.searchDescription')
  }

  getSyntaxUsage() {
    return ['search(text, text)']
  }

  getExamples() {
    return [
      'search("test a b c test", "test") = 1',
      'search("none", "test") = 0',
    ]
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoRowId extends FwegoFunctionDefinition {
  static getType() {
    return 'row_id'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.rowIdDescription')
  }

  getSyntaxUsage() {
    return ['row_id()']
  }

  getExamples() {
    return ['concat("Row ", row_id())']
  }

  getFormulaType() {
    return 'special'
  }
}

export class FwegoLength extends FwegoFunctionDefinition {
  static getType() {
    return 'length'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.lengthDescription')
  }

  getSyntaxUsage() {
    return ['length(text)']
  }

  getExamples() {
    return ['length("abc") = 3']
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoReverse extends FwegoFunctionDefinition {
  static getType() {
    return 'reverse'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.reverseDescription')
  }

  getSyntaxUsage() {
    return ['reverse(text)']
  }

  getExamples() {
    return ['reverse("abc") = "cba"']
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoNotEqual extends FwegoFunctionDefinition {
  static getType() {
    return 'not_equal'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.notEqualDescription')
  }

  getSyntaxUsage() {
    return ['any != any', 'not_equal(any, any)']
  }

  getExamples() {
    return ['1!=2', "'a' != 'b'"]
  }

  getFormulaType() {
    return 'boolean'
  }

  isOperator() {
    return true
  }

  getOperator() {
    return '!='
  }
}

export class FwegoCount extends FwegoFunctionDefinition {
  static getType() {
    return 'count'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.countDescription')
  }

  getSyntaxUsage() {
    return ['count(array)']
  }

  getExamples() {
    return ["count(field('my link row field'))"]
  }

  getFormulaType() {
    return 'array'
  }

  isRollupCompatible(targetFieldType) {
    return true
  }
}

export class FwegoContains extends FwegoFunctionDefinition {
  static getType() {
    return 'contains'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.containsDescription')
  }

  getSyntaxUsage() {
    return ['contains(text,text)']
  }

  getExamples() {
    return ['contains("test", "e") = true']
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoLeft extends FwegoFunctionDefinition {
  static getType() {
    return 'left'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.leftDescription')
  }

  getSyntaxUsage() {
    return ['left(text, number)']
  }

  getExamples() {
    return [
      'left("abcde", 2) = "ab"',
      'left("abcde", -2) = "abc"',
      'when_empty(left("abcd", 1/0), "error") = "error"',
    ]
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoRight extends FwegoFunctionDefinition {
  static getType() {
    return 'right'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.rightDescription')
  }

  getSyntaxUsage() {
    return ['right(text, number)']
  }

  getExamples() {
    return [
      'right("abcde", 2) = "de"',
      'right("abcde", -2) = "cde"',
      'when_empty(right("abcd", 1/0), "error") = "error"',
    ]
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoTrim extends FwegoFunctionDefinition {
  static getType() {
    return 'trim'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.trimDescription')
  }

  getSyntaxUsage() {
    return ['trim(text)']
  }

  getExamples() {
    return ['trim("   abc   ") = "abc"']
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoRegexReplace extends FwegoFunctionDefinition {
  static getType() {
    return 'regex_replace'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.regexReplaceDescription')
  }

  getSyntaxUsage() {
    return ['regex_replace(text, regex text, replacement text)']
  }

  getExamples() {
    return ['regex_replace("abc", "a", "1") = "1bc"']
  }

  getFormulaType() {
    return 'text'
  }
}

export class FwegoLink extends FwegoFunctionDefinition {
  static getType() {
    return 'link'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.linkDescription')
  }

  getSyntaxUsage() {
    return ['link(text, text)']
  }

  getExamples() {
    return ["link('http://your-text-here.com', 'label')"]
  }

  getFormulaType() {
    return 'link'
  }
}

export class FwegoButton extends FwegoFunctionDefinition {
  static getType() {
    return 'button'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.buttonDescription')
  }

  getSyntaxUsage() {
    return ['button(text, text)']
  }

  getExamples() {
    return ["button('http://your-text-here.com', 'your-label')"]
  }

  getFormulaType() {
    return 'link'
  }
}

export class FwegoGetLinkUrl extends FwegoFunctionDefinition {
  static getType() {
    return 'get_link_url'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.getLinkUrlDescription')
  }

  getSyntaxUsage() {
    return ['get_link_url(link)']
  }

  getExamples() {
    return [
      "get_link_url(field('formula link field')) = 'http://your-text-here.com'",
    ]
  }

  getFormulaType() {
    return 'link'
  }
}

export class FwegoGetLinkLabel extends FwegoFunctionDefinition {
  static getType() {
    return 'get_link_label'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.getLinkLabelDescription')
  }

  getSyntaxUsage() {
    return ['get_link_label(button)']
  }

  getExamples() {
    return ["get_link_label(field('formula button field')) = 'your-label'"]
  }

  getFormulaType() {
    return 'link'
  }
}

export class FwegoGreatest extends FwegoFunctionDefinition {
  static getType() {
    return 'greatest'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.greatestDescription')
  }

  getSyntaxUsage() {
    return ['greatest(number, number)']
  }

  getExamples() {
    return ['greatest(1,2) = 2']
  }

  getFormulaType() {
    return 'number'
  }
}
export class FwegoRound extends FwegoFunctionDefinition {
  static getType() {
    return 'round'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.roundDescription')
  }

  getSyntaxUsage() {
    return ['round(number, number)']
  }

  getExamples() {
    return [
      'round(1.12345,2) = 1.12',
      'round(1234.5678, -2) = 1200',
      'round(1234.11111, 2.999) = 1234.11',
      'round(1234.11111, 1/0) = NaN',
      'round(1234.11111, tonumber("invalid number")) = NaN',
    ]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoPower extends FwegoFunctionDefinition {
  static getType() {
    return 'power'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.powerDescription')
  }

  getSyntaxUsage() {
    return ['power(number, number)']
  }

  getExamples() {
    return [
      'power(3, 2) = 9',
      'power(25, 0.5) = 5.0',
      'power(-2.001, 3) = -8.012',
      'power(1/0, 2) = NaN',
      'power(1234.11111, 1/0) = NaN',
      'power(1234.11111, tonumber("invalid number")) = NaN',
    ]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoLog extends FwegoFunctionDefinition {
  static getType() {
    return 'log'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.logDescription')
  }

  getSyntaxUsage() {
    return ['log(number, number)']
  }

  getExamples() {
    return [
      'log(3, 9) = 2',
      'log(125.000, 5) = 0.333',
      'log(-8.000, 3) = NaN',
      'log(1/0, -2) = NaN',
      'log(1234.11111, 1/0) = NaN',
      'log(1234.11111, tonumber("invalid number")) = NaN',
    ]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoMod extends FwegoFunctionDefinition {
  static getType() {
    return 'mod'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.modDescription')
  }

  getSyntaxUsage() {
    return ['mod(number, number)']
  }

  getExamples() {
    return [
      'mod(5, 2) = 1',
      'mod(5, 1.5) = 0.5',
      'mod(-5.001, 1.5) = -0.501',
      'mod(-3, 2) = -1',
      'mod(3, -2) = 1',
      'mod(-3, -2) = -1',
      'mod(1, 0) = NaN',
      'mod(4, tonumber("invalid number")) = NaN',
    ]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoAbs extends FwegoFunctionDefinition {
  static getType() {
    return 'abs'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.absDescription')
  }

  getSyntaxUsage() {
    return ['abs(number)']
  }

  getExamples() {
    return [
      'abs(1.49) = 1.49',
      'abs(1.51) = 1.51',
      'abs(-1.51) = 1.51',
      'abs(-1.49) = 1.49',
      'abs(1/0) = NaN',
      'abs(tonumber("invalid")) = NaN',
    ]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoExp extends FwegoFunctionDefinition {
  static getType() {
    return 'exp'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.expDescription')
  }

  getSyntaxUsage() {
    return ['exp(number)']
  }

  getExamples() {
    return [
      'exp(1.000) = 2.718',
      'exp(0) = 1',
      'exp(-1.00) = 0.37',
      'exp(1/0) = NaN',
      'exp(tonumber("invalid")) = NaN',
    ]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoEven extends FwegoFunctionDefinition {
  static getType() {
    return 'even'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.evenDescription')
  }

  getSyntaxUsage() {
    return ['even(number)']
  }

  getExamples() {
    return [
      'even(2) = true',
      'even(2.5) = false',
      'even(5) = false',
      'even(1/0) = false',
      'even(tonumber("invalid")) = false',
    ]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoOdd extends FwegoFunctionDefinition {
  static getType() {
    return 'odd'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.oddDescription')
  }

  getSyntaxUsage() {
    return ['odd(number)']
  }

  getExamples() {
    return [
      'odd(2) = false',
      'odd(2.5) = false',
      'odd(5) = true',
      'odd(1/0) = false',
      'odd(tonumber("invalid")) = false',
    ]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoLn extends FwegoFunctionDefinition {
  static getType() {
    return 'ln'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.lnDescription')
  }

  getSyntaxUsage() {
    return ['ln(number)']
  }

  getExamples() {
    return [
      'ln(2.718) = 1.000',
      'ln(9.0) = 2.2',
      'ln(2.00) = 0.69',
      'ln(-1) = NaN',
      'ln(1/0) = NaN',
      'ln(tonumber("invalid")) = NaN',
    ]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoSign extends FwegoFunctionDefinition {
  static getType() {
    return 'sign'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.signDescription')
  }

  getSyntaxUsage() {
    return ['sign(number)']
  }

  getExamples() {
    return [
      'sign(2.1234) = 1',
      'sign(-9.0) = -1',
      'sign(0) = 0',
      'sign(1/0) = NaN',
      'sign(tonumber("invalid")) = NaN',
    ]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoSqrt extends FwegoFunctionDefinition {
  static getType() {
    return 'sqrt'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.sqrtDescription')
  }

  getSyntaxUsage() {
    return ['sqrt(number)']
  }

  getExamples() {
    return [
      'sqrt(9) = 3',
      'sqrt(2.00) = 1.41',
      'sqrt(-4) = NaN',
      'sqrt(1/0) = NaN',
      'sqrt(tonumber("invalid")) = NaN',
    ]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoFloor extends FwegoFunctionDefinition {
  static getType() {
    return 'floor'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.floorDescription')
  }

  getSyntaxUsage() {
    return ['floor(number)']
  }

  getExamples() {
    return [
      'floor(1.49) = 1',
      'floor(1.51) = 1',
      'floor(-1.51) = -2',
      'floor(-1.49) = -2',
      'floor(1/0) = NaN',
      'floor(tonumber("invalid")) = NaN',
    ]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoCeil extends FwegoFunctionDefinition {
  static getType() {
    return 'ceil'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.ceilDescription')
  }

  getSyntaxUsage() {
    return ['ceil(number)']
  }

  getExamples() {
    return [
      'ceil(1.49) = 2',
      'ceil(1.51) = 2',
      'ceil(-1.51) = -1',
      'ceil(-1.49) = -1',
      'ceil(1/0) = NaN',
      'ceil(tonumber("invalid")) = NaN',
    ]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoTrunc extends FwegoFunctionDefinition {
  static getType() {
    return 'trunc'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.truncDescription')
  }

  getSyntaxUsage() {
    return ['trunc(number)']
  }

  getExamples() {
    return [
      'trunc(1.49) = 1',
      'trunc(1.51) = 1',
      'trunc(-1.51) = -1',
      'trunc(-1.49) = -1',
      'trunc(1/0) = NaN',
      'trunc(tonumber("invalid")) = NaN',
    ]
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoIsNaN extends FwegoFunctionDefinition {
  static getType() {
    return 'is_nan'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.isNanDescription')
  }

  getSyntaxUsage() {
    return ['is_nan(number)']
  }

  getExamples() {
    return ['is_nan(1 / 0) = true', 'is_nan(1) = false']
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoWhenNaN extends FwegoFunctionDefinition {
  static getType() {
    return 'when_nan'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.whenNanDescription')
  }

  getSyntaxUsage() {
    return ['when_nan(number, fallback)']
  }

  getExamples() {
    return ['when_nan(1 / 0, 4) = 4', 'when_nan(1, 4) = 1']
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoLeast extends FwegoFunctionDefinition {
  static getType() {
    return 'least'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.leastDescription')
  }

  getSyntaxUsage() {
    return ['least(number, number)']
  }

  getExamples() {
    return ['least(1,2) = 1']
  }

  getFormulaType() {
    return 'number'
  }
}

export class FwegoMonth extends FwegoFunctionDefinition {
  static getType() {
    return 'month'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.monthDescription')
  }

  getSyntaxUsage() {
    return ['month(date)']
  }

  getExamples() {
    return ['month(todate("2021-12-12", "YYYY-MM-DD")) = 12']
  }

  getFormulaType() {
    return 'date'
  }
}

export class FwegoYear extends FwegoFunctionDefinition {
  static getType() {
    return 'year'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.yearDescription')
  }

  getSyntaxUsage() {
    return ['year(date)']
  }

  getExamples() {
    return ['year(field("my date"))']
  }

  getFormulaType() {
    return 'date'
  }
}

export class FwegoSecond extends FwegoFunctionDefinition {
  static getType() {
    return 'second'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.secondDescription')
  }

  getSyntaxUsage() {
    return ['second(date)']
  }

  getExamples() {
    return ['second(field("dates")) == 2']
  }

  getFormulaType() {
    return 'date'
  }
}
export class FwegoWhenEmpty extends FwegoFunctionDefinition {
  static getType() {
    return 'when_empty'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.whenEmptyDescription')
  }

  getSyntaxUsage() {
    return ['when_empty(any, same type as the first)']
  }

  getExamples() {
    return ['when_empty(field("a"), "default")']
  }

  getFormulaType() {
    return 'special'
  }
}

export class FwegoAny extends FwegoFunctionDefinition {
  static getType() {
    return 'any'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.anyDescription')
  }

  getSyntaxUsage() {
    return ['any(boolean values from a lookup() or field())']
  }

  getExamples() {
    return ['any(field("my lookup") = "test")']
  }

  getFormulaType() {
    return 'array'
  }

  isRollupCompatible(targetFieldType) {
    return true
  }
}

export class FwegoEvery extends FwegoFunctionDefinition {
  static getType() {
    return 'every'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.everyDescription')
  }

  getSyntaxUsage() {
    return ['every(boolean values from a lookup() or field())']
  }

  getExamples() {
    return ['every(field("my lookup") = "test")']
  }

  getFormulaType() {
    return 'array'
  }

  isRollupCompatible(targetFieldType) {
    return true
  }
}

export class FwegoMax extends FwegoFunctionDefinition {
  static getType() {
    return 'max'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.maxDescription')
  }

  getSyntaxUsage() {
    return ['max(numbers/text/date from a lookup() or field())']
  }

  getExamples() {
    return [
      'max(lookup("link field", "number field"))',
      'max(lookup("link field", "date field"))',
      'max(field("lookup field"))',
      'max(field("link field with text primary field"))',
    ]
  }

  getFormulaType() {
    return 'array'
  }

  isRollupCompatible(targetFieldType) {
    return true
  }
}

export class FwegoMin extends FwegoFunctionDefinition {
  static getType() {
    return 'min'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.minDescription')
  }

  getSyntaxUsage() {
    return ['min(numbers/test/dates from a lookup() or field())']
  }

  getExamples() {
    return [
      'min(lookup("link field", "number field"))',
      'min(lookup("link field", "date field"))',
      'min(field("lookup field"))',
      'min(field("link field with text primary field"))',
    ]
  }

  getFormulaType() {
    return 'array'
  }

  isRollupCompatible(targetFieldType) {
    return true
  }
}

export class FwegoJoin extends FwegoFunctionDefinition {
  static getType() {
    return 'join'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.joinDescription')
  }

  getSyntaxUsage() {
    return ['join(text from lookup() or field(), text)']
  }

  getExamples() {
    return [
      'join(lookup("link field", "number field"), "_")',
      'join(field("lookup field"), field("different lookup field"))',
      'join(field("link field with text primary field"), ",")',
    ]
  }

  getFormulaType() {
    return 'array'
  }
}

export class FwegoStddevPop extends FwegoFunctionDefinition {
  static getType() {
    return 'stddev_pop'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.stddevPopDescription')
  }

  getSyntaxUsage() {
    return ['stddev_pop(numbers from lookup() or field())']
  }

  getExamples() {
    return [
      'stddev_pop(lookup("link field", "number field"))',
      'stddev_pop(field("lookup field"))',
      'stddev_pop(field("link field with number primary field"))',
    ]
  }

  getFormulaType() {
    return 'array'
  }

  isRollupCompatible(targetFieldType) {
    return true
  }
}

export class FwegoStddevSample extends FwegoFunctionDefinition {
  static getType() {
    return 'stddev_sample'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.stddevSampleDescription')
  }

  getSyntaxUsage() {
    return ['stddev_sample(numbers from lookup() or field())']
  }

  getExamples() {
    return [
      'stddev_sample(lookup("link field", "number field"))',
      'stddev_sample(field("lookup field"))',
      'stddev_sample(field("link field with number primary field"))',
    ]
  }

  getFormulaType() {
    return 'array'
  }

  isRollupCompatible(targetFieldType) {
    return true
  }
}

export class FwegoVarianceSample extends FwegoFunctionDefinition {
  static getType() {
    return 'variance_sample'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.varianceSampleDescription')
  }

  getSyntaxUsage() {
    return ['variance_sample(numbers from lookup() or field())']
  }

  getExamples() {
    return [
      'variance_sample(lookup("link field", "number field"))',
      'variance_sample(field("lookup field"))',
      'variance_sample(field("link field with number primary field"))',
    ]
  }

  getFormulaType() {
    return 'array'
  }

  isRollupCompatible(targetFieldType) {
    return true
  }
}

export class FwegoVariancePop extends FwegoFunctionDefinition {
  static getType() {
    return 'variance_pop'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.variancePopDescription')
  }

  getSyntaxUsage() {
    return ['variance_pop(numbers from lookup() or field())']
  }

  getExamples() {
    return [
      'variance_pop(lookup("link field", "number field"))',
      'variance_pop(field("lookup field"))',
      'variance_pop(field("link field with number primary field"))',
    ]
  }

  getFormulaType() {
    return 'array'
  }

  isRollupCompatible(targetFieldType) {
    return true
  }
}

export class FwegoAvg extends FwegoFunctionDefinition {
  static getType() {
    return 'avg'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.avgDescription')
  }

  getSyntaxUsage() {
    return ['avg(numbers from lookup() or field())']
  }

  getExamples() {
    return [
      'avg(lookup("link field", "number field"))',
      'avg(field("lookup field"))',
      'avg(field("link field with number primary field"))',
    ]
  }

  getFormulaType() {
    return 'array'
  }

  isRollupCompatible(targetFieldType) {
    return true
  }
}

export class FwegoSum extends FwegoFunctionDefinition {
  static getType() {
    return 'sum'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.sumDescription')
  }

  getSyntaxUsage() {
    return ['sum(numbers from lookup() or field())']
  }

  getExamples() {
    return [
      'sum(lookup("link field", "number field"))',
      'sum(field("lookup field"))',
      'sum(field("link field with number primary field"))',
    ]
  }

  getFormulaType() {
    return 'array'
  }

  isRollupCompatible(targetFieldType) {
    return true
  }
}

export class FwegoFilter extends FwegoFunctionDefinition {
  static getType() {
    return 'filter'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.filterDescription')
  }

  getSyntaxUsage() {
    return [
      'filter(an expression involving lookup() or field(a link/lookup field),' +
        ' boolean)',
    ]
  }

  getExamples() {
    return [
      'sum(filter(lookup("link field", "number field"), lookup("link field", "number' +
        ' field") > 10))',
      'filter(field("lookup field"), contains(field("lookup field"), "a"))',
      'filter(field("link field") + "a", length(field("link field")) > 10")',
    ]
  }

  getFormulaType() {
    return 'array'
  }
}

export class FwegoGetFileVisibleName extends FwegoFunctionDefinition {
  static getType() {
    return 'get_file_visible_name'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.getFileVisibleNameDescription')
  }

  getSyntaxUsage() {
    return ['get_file_visible_name(a file)']
  }

  getExamples() {
    return ['get_file_visible_name(index(field("File field"), 0))']
  }

  getFormulaType() {
    return 'single_file'
  }
}
export class FwegoGetFileMimeType extends FwegoFunctionDefinition {
  static getType() {
    return 'get_file_mime_type'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.getFileMimeTypeDescription')
  }

  getSyntaxUsage() {
    return ['get_file_mime_type(a file)']
  }

  getExamples() {
    return ['get_file_mime_type(index(field("File field"), 0))']
  }

  getFormulaType() {
    return 'single_file'
  }
}

export class FwegoGetFileCount extends FwegoFunctionDefinition {
  static getType() {
    return 'get_file_count'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.getFileCountDescription')
  }

  getSyntaxUsage() {
    return ['get_file_count(a file field)']
  }

  getExamples() {
    return ['get_file_count(field("File field"))']
  }

  getFormulaType() {
    return 'array'
  }
}
export class FwegoGetFileSize extends FwegoFunctionDefinition {
  static getType() {
    return 'get_file_size'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.getFileSizeDescription')
  }

  getSyntaxUsage() {
    return ['get_file_size(a file)']
  }

  getExamples() {
    return ['get_file_size(index(field("File field"), 0))']
  }

  getFormulaType() {
    return 'single_file'
  }
}
export class FwegoGetImageWidth extends FwegoFunctionDefinition {
  static getType() {
    return 'get_image_width'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.getImageWidthDescription')
  }

  getSyntaxUsage() {
    return ['get_image_width(a file)']
  }

  getExamples() {
    return ['get_image_width(index(field("File field"), 0))']
  }

  getFormulaType() {
    return 'single_file'
  }
}
export class FwegoGetImageHeight extends FwegoFunctionDefinition {
  static getType() {
    return 'get_image_height'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.getImageHeightDescription')
  }

  getSyntaxUsage() {
    return ['get_image_height(a file)']
  }

  getExamples() {
    return ['get_image_height(index(field("File field"), 0))']
  }

  getFormulaType() {
    return 'single_file'
  }
}
export class FwegoIsImage extends FwegoFunctionDefinition {
  static getType() {
    return 'is_image'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.getIsImageDescription')
  }

  getSyntaxUsage() {
    return ['is_image(a file)']
  }

  getExamples() {
    return ['is_image(index(field("File field"), 0))']
  }

  getFormulaType() {
    return 'single_file'
  }
}
export class FwegoIndex extends FwegoFunctionDefinition {
  static getType() {
    return 'index'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.indexDescription')
  }

  getSyntaxUsage() {
    return ['index(a file field, a number)']
  }

  getExamples() {
    return ['index(field("File field"), 0)']
  }

  getFormulaType() {
    return 'special'
  }
}

export class FwegoToUrl extends FwegoFunctionDefinition {
  static getType() {
    return 'tourl'
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('formulaFunctions.getToUrlDescription')
  }

  getSyntaxUsage() {
    return ['to_url(any)']
  }

  getExamples() {
    return ['to_url("www.fwego.io")']
  }

  getFormulaType() {
    return 'url'
  }
}
