import { ApplicationType } from '@fwego/modules/core/applicationTypes'
import ApplicationContext from '@fwego/modules/dashboard/components/application/ApplicationContext'
import DashboardForm from '@fwego/modules/dashboard/components/form/DashboardForm'
import SidebarComponentDashboard from '@fwego/modules/dashboard/components/sidebar/SidebarComponentDashboard'

export class DashboardApplicationType extends ApplicationType {
  static getType() {
    return 'dashboard'
  }

  getIconClass() {
    return 'fwego-icon-dashboard'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('applicationType.dashboard')
  }

  getNamePlural() {
    const { i18n } = this.app
    return i18n.t('applicationType.dashboards')
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('applicationType.dashboardDesc')
  }

  getDefaultName() {
    const { i18n } = this.app
    return i18n.t('applicationType.dashboardDefaultName')
  }

  supportsTrash() {
    return false
  }

  getApplicationContextComponent() {
    return ApplicationContext
  }

  getApplicationFormComponent() {
    return DashboardForm
  }

  getSidebarComponent() {
    return SidebarComponentDashboard
  }

  delete(application, { $router }) {
    $router.push({ name: 'dashboard' })
  }

  async select(application, { $router }) {
    try {
      await $router.push({
        name: 'dashboard-application',
        params: {
          dashboardId: application.id,
        },
      })
    } catch (error) {
      if (error.name !== 'NavigationDuplicated') {
        throw error
      }
    }
  }

  isBeta() {
    return true
  }

  getOrder() {
    return 80
  }
}
