import { ErrorPageType } from '@fwego/modules/core/errorPageTypes'
import PublicSiteErrorPage from '@fwego/modules/builder/components/PublicSiteErrorPage'

export class PublicSiteErrorPageType extends ErrorPageType {
  getComponent() {
    return PublicSiteErrorPage
  }

  isApplicable() {
    return this.app.context.route.name === 'application-builder-page'
  }

  static getType() {
    return 'publicSite'
  }

  getOrder() {
    return 10
  }
}
