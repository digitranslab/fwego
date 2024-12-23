import { NotificationType } from '@fwego/modules/core/notificationTypes'
import RowCommentMentionNotification from '@fwego_premium/components/row_comments/RowCommentMentionNotification'
import RowCommentNotification from '@fwego_premium/components/row_comments/RowCommentNotification'
import NotificationSenderInitialsIcon from '@fwego/modules/core/components/notifications/NotificationSenderInitialsIcon'

export class RowCommentMentionNotificationType extends NotificationType {
  static getType() {
    return 'row_comment_mention'
  }

  getIconComponent() {
    return NotificationSenderInitialsIcon
  }

  getContentComponent() {
    return RowCommentMentionNotification
  }

  getRoute(notificationData) {
    return {
      name: 'database-table-row',
      params: {
        databaseId: notificationData.database_id,
        tableId: notificationData.table_id,
        rowId: notificationData.row_id,
      },
    }
  }
}

export class RowCommentNotificationType extends NotificationType {
  static getType() {
    return 'row_comment'
  }

  getIconComponent() {
    return NotificationSenderInitialsIcon
  }

  getContentComponent() {
    return RowCommentNotification
  }

  getRoute(notificationData) {
    return {
      name: 'database-table-row',
      params: {
        databaseId: notificationData.database_id,
        tableId: notificationData.table_id,
        rowId: notificationData.row_id,
      },
    }
  }
}
