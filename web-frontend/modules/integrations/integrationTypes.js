import { IntegrationType } from '@fwego/modules/core/integrationTypes'
import LocalFwegoForm from '@fwego/modules/integrations/localFwego/components/integrations/LocalFwegoForm'
import localFwegoIntegration from '@fwego/modules/integrations/localFwego/assets/images/localFwegoIntegration.svg'

export class LocalFwegoIntegrationType extends IntegrationType {
  static getType() {
    return 'local_fwego'
  }

  get name() {
    return this.app.i18n.t('integrationType.localFwego')
  }

  get image() {
    return localFwegoIntegration
  }

  getSummary(integration) {
    if (!integration.authorized_user) {
      return this.app.i18n.t('localFwegoIntegrationType.localFwegoNoUser')
    }

    return this.app.i18n.t('localFwegoIntegrationType.localFwegoSummary', {
      name: integration.authorized_user.first_name,
      username: integration.authorized_user.username,
    })
  }

  get formComponent() {
    return LocalFwegoForm
  }

  get warning() {
    return this.app.i18n.t('localFwegoIntegrationType.localFwegoWarning')
  }

  getDefaultValues() {
    const user = this.app.store.getters['auth/getUserObject']
    return {
      authorized_user: { username: user.username, first_name: user.first_name },
    }
  }

  getOrder() {
    return 10
  }
}
