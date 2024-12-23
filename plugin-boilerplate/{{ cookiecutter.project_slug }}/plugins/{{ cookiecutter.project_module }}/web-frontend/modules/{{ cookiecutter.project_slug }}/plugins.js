import { FwegoPlugin } from '@fwego/modules/core/plugins'

export class PluginNamePlugin extends FwegoPlugin {
  static getType() {
    return '{{ cookiecutter.project_slug }}'
  }
}
