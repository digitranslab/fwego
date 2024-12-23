import { FwegoPlugin } from '@fwego/modules/core/plugins'
import ChatwootSupportSidebarWorkspace from '@fwego_enterprise/components/ChatwootSupportSidebarWorkspace'
import AuditLogSidebarWorkspace from '@fwego_enterprise/components/AuditLogSidebarWorkspace'
import MemberRolesDatabaseContextItem from '@fwego_enterprise/components/member-roles/MemberRolesDatabaseContextItem'
import MemberRolesTableContextItem from '@fwego_enterprise/components/member-roles/MemberRolesTableContextItem'
import EnterpriseFeatures from '@fwego_enterprise/features'
import SnapshotModalWarning from '@fwego_enterprise/components/SnapshotModalWarning'
import EnterpriseSettings from '@fwego_enterprise/components/EnterpriseSettings'
import EnterpriseSettingsOverrideDashboardHelp from '@fwego_enterprise/components/EnterpriseSettingsOverrideDashboardHelp'
import EnterpriseLogo from '@fwego_enterprise/components/EnterpriseLogo'
import { DatabaseApplicationType } from '@fwego/modules/database/applicationTypes'
import ExportWorkspaceModalWarning from '@fwego_enterprise/components/ExportWorkspaceModalWarning.vue'

export class EnterprisePlugin extends FwegoPlugin {
  static getType() {
    return 'enterprise'
  }

  getSidebarWorkspaceComponents(workspace) {
    const sidebarItems = []
    if (!this.app.$config.FWEGO_DISABLE_SUPPORT) {
      sidebarItems.push(ChatwootSupportSidebarWorkspace)
    }
    sidebarItems.push(AuditLogSidebarWorkspace)
    return sidebarItems
  }

  getAdditionalApplicationContextComponents(workspace, application) {
    const additionalComponents = []
    const hasReadRolePermission = this.app.$hasPermission(
      'application.read_role',
      application,
      workspace.id
    )
    if (
      hasReadRolePermission &&
      application.type === DatabaseApplicationType.getType()
    ) {
      additionalComponents.push(MemberRolesDatabaseContextItem)
    }
    return additionalComponents
  }

  getAdditionalTableContextComponents(workspace, table) {
    if (
      this.app.$hasPermission('database.table.read_role', table, workspace.id)
    ) {
      return [MemberRolesTableContextItem]
    } else {
      return []
    }
  }

  getExtraSnapshotModalComponents(workspace) {
    const rbacSupport = this.app.$hasFeature(
      EnterpriseFeatures.RBAC,
      workspace.id
    )
    return rbacSupport ? SnapshotModalWarning : null
  }

  getExtraExportWorkspaceModalComponents(workspace) {
    const rbacSupport = this.app.$hasFeature(
      EnterpriseFeatures.RBAC,
      workspace.id
    )
    return rbacSupport ? ExportWorkspaceModalWarning : null
  }

  getSettingsPageComponents() {
    return [EnterpriseSettings]
  }

  getDashboardHelpComponents() {
    if (this.app.$hasFeature(EnterpriseFeatures.ENTERPRISE_SETTINGS)) {
      return [EnterpriseSettingsOverrideDashboardHelp]
    } else {
      return []
    }
  }

  getLogoComponent() {
    if (this.app.$hasFeature(EnterpriseFeatures.ENTERPRISE_SETTINGS)) {
      return EnterpriseLogo
    } else {
      return null
    }
  }

  getLogoComponentOrder() {
    return 100
  }

  /**
   * This method can be used to hide certain features in `EnterpriseFeatures.vue`.
   * If the array contains `[EnterpriseFeatures.RBAC]`, for example, then that entry
   * will be hidden in the features.
   */
  getVisuallyHiddenFeatures() {
    return []
  }
}
