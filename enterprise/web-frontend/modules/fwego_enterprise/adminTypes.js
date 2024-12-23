import { AdminType } from '@fwego/modules/core/adminTypes'
import EnterpriseFeatures from '@fwego_enterprise/features'
import EnterpriseModal from '@fwego_enterprise/components/EnterpriseModal'

class EnterpriseAdminType extends AdminType {
  getDeactivatedModal() {
    return EnterpriseModal
  }
}

export class AuthProvidersType extends EnterpriseAdminType {
  static getType() {
    return 'auth-providers'
  }

  getIconClass() {
    return 'iconoir-log-in'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('adminType.Authentication')
  }

  getRouteName() {
    return 'admin-auth-providers'
  }

  getOrder() {
    return 100
  }

  isDeactivated() {
    return !this.app.$hasFeature(EnterpriseFeatures.SSO)
  }
}

export class AuditLogType extends EnterpriseAdminType {
  static getType() {
    return 'audit-log'
  }

  getIconClass() {
    return 'fwego-icon-history'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('adminType.AuditLog')
  }

  getRouteName() {
    return 'admin-audit-log'
  }

  getOrder() {
    return 110
  }

  isDeactivated() {
    return !this.app.$hasFeature(EnterpriseFeatures.AUDIT_LOG)
  }
}
