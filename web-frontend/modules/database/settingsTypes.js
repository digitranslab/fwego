import { SettingsType } from '@fwego/modules/core/settingsTypes'
import APITokenSettings from '@fwego/modules/database/components/settings/APITokenSettings'

export class APITokenSettingsType extends SettingsType {
  static getType() {
    return 'tokens'
  }

  getIconClass() {
    return 'iconoir-key-alt-plus'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('settingType.tokens')
  }

  getComponent() {
    return APITokenSettings
  }
}
