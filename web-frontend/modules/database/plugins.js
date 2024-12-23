import { FwegoPlugin } from '@fwego/modules/core/plugins'
import DatabaseDashboardResourceLinks from '@fwego/modules/database/components/dashboard/DatabaseDashboardResourceLinks'

export class DatabasePlugin extends FwegoPlugin {
  static getType() {
    return 'database'
  }

  getDashboardResourceLinksComponent() {
    return DatabaseDashboardResourceLinks
  }
}
