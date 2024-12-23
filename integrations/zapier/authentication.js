module.exports = {
  type: 'custom',
  test: {
    url: `{{bundle.authData.apiURL}}/api/database/tokens/check/`,
    method: 'GET',
    headers: { 'Authorization': 'Token {{bundle.authData.apiToken}}' },
  },
  fields: [
    {
      computed: false,
      key: 'apiToken',
      required: true,
      label: 'Fwego API token',
      type: 'string',
      helpText:
        'Please enter your Fwego API token. Can be found by clicking on your ' +
        'account in the top left corner -> Settings -> API tokens.'
    },
    {
      computed: false,
      key: 'apiURL',
      required: false,
      label: 'Fwego API URL',
      default: 'https://api.fwego.io',
      type: 'string',
      helpText:
        'Please enter your Fwego API URL. If you are using fwego.io, you ' +
        'can leave the default one.'
    },
  ],
  connectionLabel: 'Fwego API authentication',
  customConfig: {}
}
