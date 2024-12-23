/**
 * This file can be used in combination with intellij idea so the @fwego path
 * resolves.
 *
 * Intellij IDEA: Preferences -> Languages & Frameworks -> JavaScript -> Webpack ->
 * webpack configuration file
 */

const path = require('path')

module.exports = {
  resolve: {
    extensions: ['.js', '.json', '.vue', '.ts'],
    root: path.resolve(__dirname),
    alias: {
      '@fwego': path.resolve(__dirname),
      '@fwego_premium': path.resolve(
        __dirname,
        '../premium/web-frontend/modules/fwego_premium'
      ),
      '@fwego_premium_test': path.resolve(
        __dirname,
        '../premium/web-frontend/test'
      ),
      '@fwego_enterprise': path.resolve(
        __dirname,
        '../enterprise/web-frontend/modules/fwego_enterprise'
      ),
      '@fwego_enterprise_test': path.resolve(
        __dirname,
        '../enterprise/web-frontend/test'
      ),
      '@fwego_test_cases': path.resolve(__dirname, '../tests/cases'),
    },
  },
}
