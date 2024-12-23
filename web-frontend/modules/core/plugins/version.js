const pkg = require('../package.json')

export default (context, inject) => {
  inject('fwegoVersion', pkg.version)
}
