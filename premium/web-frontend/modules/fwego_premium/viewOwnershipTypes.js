import { ViewOwnershipType } from '@fwego/modules/database/viewOwnershipTypes'
import PremiumFeatures from '@fwego_premium/features'
import PremiumModal from '@fwego_premium/components/PremiumModal'
import ViewOwnershipMenuLink from '@fwego_premium/components/views/ViewOwnershipMenuLink'

export class PersonalViewOwnershipType extends ViewOwnershipType {
  static getType() {
    return 'personal'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('viewOwnershipType.personal')
  }

  getFeatureName() {
    const { i18n } = this.app
    return i18n.t('premiumFeatures.personalViews')
  }

  getIconClass() {
    return 'iconoir-lock'
  }

  isDeactivated(workspaceId) {
    return !this.app.$hasFeature(PremiumFeatures.PREMIUM, workspaceId)
  }

  getDeactivatedText() {
    return this.app.i18n.t('premium.deactivated')
  }

  getDeactivatedModal() {
    return PremiumModal
  }

  getListViewTypeSort() {
    return 40
  }

  /**
   * Returns the component that should be used in the menu for changing the
   * ownership type for the view.
   */
  getChangeOwnershipTypeMenuItemComponent() {
    return ViewOwnershipMenuLink
  }

  userCanTryCreate(table, workspaceId) {
    return this.app.$hasPermission(
      'database.table.create_and_use_personal_view',
      table,
      workspaceId
    )
  }
}
