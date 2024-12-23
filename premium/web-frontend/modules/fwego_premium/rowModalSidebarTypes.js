import { RowModalSidebarType } from '@fwego/modules/database/rowModalSidebarTypes'
import RowCommentsSidebar from '@fwego_premium/components/row_comments/RowCommentsSidebar'
import RowEditModalCommentNotificationMode from '@fwego_premium/components/row_comments/RowEditModalCommentNotificationMode'
import PremiumFeatures from '@fwego_premium/features'

export class CommentsRowModalSidebarType extends RowModalSidebarType {
  static getType() {
    return 'comments'
  }

  getName() {
    return this.app.i18n.t('rowCommentSidebar.name')
  }

  getComponent() {
    return RowCommentsSidebar
  }

  isDeactivated(database, table, readOnly) {
    return !this.app.$hasPermission(
      'database.table.list_comments',
      table,
      database.workspace.id
    )
  }

  isSelectedByDefault(database) {
    return this.app.$hasFeature(PremiumFeatures.PREMIUM, database.workspace.id)
  }

  getOrder() {
    return 0
  }

  getActionComponent(row) {
    // Return this component only if the row provides the metadata to show the
    // notification mode context properly.
    if (row._?.metadata) {
      return RowEditModalCommentNotificationMode
    }
  }
}
