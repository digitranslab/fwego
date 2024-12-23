import { FwegoPlugin } from '@fwego/modules/core/plugins'
import Impersonate from '@fwego_premium/components/sidebar/Impersonate'
import HighestLicenseTypeBadge from '@fwego_premium/components/sidebar/HighestLicenseTypeBadge'
import FwegoLogoShareLinkOption from '@fwego_premium/components/views/FwegoLogoShareLinkOption'

export class PremiumPlugin extends FwegoPlugin {
  static getType() {
    return 'premium'
  }

  getImpersonateComponent() {
    return Impersonate
  }

  getHighestLicenseTypeBadge() {
    return HighestLicenseTypeBadge
  }

  getAdditionalShareLinkOptions() {
    return [FwegoLogoShareLinkOption]
  }

  hasFeature(feature, forSpecificWorkspace) {
    return this.app.$licenseHandler.hasFeature(feature, forSpecificWorkspace)
  }

  /**
   * A hook to provide different action buttons to the premium features modal.
   */
  getPremiumModalButtonsComponent() {
    return null
  }
}
