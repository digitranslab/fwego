const { unsupportedFwegoFieldTypes } = require('./constants')

/**
 * Fetches the fields of a table and converts them to an array with valid Zapier
 * field objects.
 */
const getRowInputValues = async (z, bundle) => {
  if (!bundle.inputData.tableID) {
    throw new Error('The `tableID` must be provided.')
  }

  const fieldsGetRequest = await z.request({
    url: `${bundle.authData.apiURL}/api/database/fields/table/${bundle.inputData.tableID}/`,
    method: 'GET',
    headers: {
      'Accept': 'application/json',
      'Authorization': `Token ${bundle.authData.apiToken}`,
    },
  })

  return fieldsGetRequest.json.map(v => {
    return mapFwegoFieldTypesToZapierTypes(v)
  })
}

/**
 * Fetches the fields and converts the input data to Fwego row compatible data.
 */
const prepareInputDataForFwego = async (z, bundle) => {
  if (!bundle.inputData.tableID) {
    throw new Error('The `tableID` must be provided.')
  }

  const fieldsGetRequest = await z.request({
    url: `${bundle.authData.apiURL}/api/database/fields/table/${bundle.inputData.tableID}/`,
    method: 'GET',
    headers: {
      'Accept': 'application/json',
      'Authorization': `Token ${bundle.authData.apiToken}`,
    },
  })

  let rowData = { id: bundle.inputData.rowID }
  fieldsGetRequest
    .json
    .filter(
      (fwegoField) =>
        fwegoField.read_only
          || !unsupportedFwegoFieldTypes.includes(fwegoField.type)
    )
    .filter((fwegoField) => bundle.inputData.hasOwnProperty(fwegoField.name))
    .forEach(fwegoField => {
      let value = bundle.inputData[fwegoField.name]

      if (fwegoField.type === 'multiple_collaborators') {
        value = value.map(id => {
          return { id }}
        )
      }

      rowData[fwegoField.name] = value
    })

  return rowData
}

/**
 * Converts the provided Fwego field type object to a Zapier compatible object.
 */
const mapFwegoFieldTypesToZapierTypes = (fwegoField) => {
  const zapType = {
    key: fwegoField.name,
    label: fwegoField.name,
    type: 'string'
  }

  if (fwegoField.type === 'long_text') {
    zapType.type = 'text'
  }

  if (fwegoField.type === 'boolean') {
    zapType.type = 'boolean'
  }

  if (fwegoField.type === 'number') {
    zapType.type = 'integer'

    if (fwegoField.number_decimal_places > 0) {
      zapType.type = 'float'
    }
  }

  if (fwegoField.type === 'boolean') {
    zapType.type = 'boolean'
  }

  if (fwegoField.type === 'rating') {
    zapType.type = 'integer'
  }

  if (['single_select', 'multiple_select'].includes(fwegoField.type)) {
    const choices = {}
    fwegoField.select_options.forEach(el => {
      choices[`${el.id}`] = el.value
    })
    zapType.type = 'string'
    zapType.choices = choices
  }

  if (fwegoField.type === 'multiple_select') {
    zapType.list = true
  }

  if (fwegoField.type === 'link_row') {
    zapType.type = 'integer'
    zapType.helpText = 'Provide row ids that you want to link to.'
    zapType.list = true
  }

  if (fwegoField.type === 'multiple_collaborators') {
    zapType.type = 'integer'
    zapType.helpText = 'Provide user ids that you want to link to.'
    zapType.list = true
  }

  if (fwegoField.type === 'date' && !fwegoField.date_include_time) {
    zapType.type = 'date'
    zapType.helpText =
      'the date fields accepts a date in ISO format (e.g. 2020-01-01)'
  }

  if (fwegoField.type === 'date' && fwegoField.date_include_time) {
    zapType.type = 'datetime'
    zapType.helpText =
      'the date fields accepts date and time in ISO format (e.g. 2020-01-01 12:00)'
  }

  if (
    fwegoField.read_only
    || unsupportedFwegoFieldTypes.includes(fwegoField.type)
  ) {
    // Read only and the file field are not supported.
    return
  }

  return zapType
}

module.exports = {
  getRowInputValues,
  prepareInputDataForFwego,
  mapFwegoFieldTypesToZapierTypes,
}
