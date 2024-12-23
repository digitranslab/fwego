import { Registerable } from '@fwego/modules/core/registry'
import NotificationSenderInitialsIcon from '@fwego/modules/core/components/notifications/NotificationSenderInitialsIcon'
import WorkspaceInvitationCreatedNotification from '@fwego/modules/core/components/notifications/WorkspaceInvitationCreatedNotification'
import WorkspaceInvitationAcceptedNotification from '@fwego/modules/core/components/notifications/WorkspaceInvitationAcceptedNotification'
import WorkspaceInvitationRejectedNotification from '@fwego/modules/core/components/notifications/WorkspaceInvitationRejectedNotification'
import FwegoVersionUpgradeNotification from '@fwego/modules/core/components/notifications/FwegoVersionUpgradeNotification'
import NotificationImgIcon from '@fwego/modules/core/components/notifications/NotificationImgIcon'
import FwegoIcon from '@fwego/modules/core/static/img/logoOnly.svg'

export class NotificationType extends Registerable {
  getIconComponent() {
    throw new Error('getIconComponent not implemented')
  }

  getContentComponent() {
    throw new Error('getContentComponent not implemented')
  }

  getIconComponentProps() {
    return {}
  }

  /**
   * Should return the nuxt route of the page where to redirect to if the user clicks
   * on the notification. Note that the backend also uses this to create a link in
   * external communication like the email, and if anything changes in this method,
   * the `safe_route_data_parameters` then might need to be updated as well. If
   * `null` is returned, it means that the notification is not clickable.
   */
  getRoute(notificationData) {
    return null
  }
}

export class WorkspaceInvitationCreatedNotificationType extends NotificationType {
  static getType() {
    return 'workspace_invitation_created'
  }

  getIconComponent() {
    return NotificationSenderInitialsIcon
  }

  getContentComponent() {
    return WorkspaceInvitationCreatedNotification
  }
}

export class WorkspaceInvitationAcceptedNotificationType extends NotificationType {
  static getType() {
    return 'workspace_invitation_accepted'
  }

  getIconComponent() {
    return NotificationSenderInitialsIcon
  }

  getContentComponent() {
    return WorkspaceInvitationAcceptedNotification
  }
}

export class WorkspaceInvitationRejectedNotificationType extends NotificationType {
  static getType() {
    return 'workspace_invitation_rejected'
  }

  getIconComponent() {
    return NotificationSenderInitialsIcon
  }

  getContentComponent() {
    return WorkspaceInvitationRejectedNotification
  }
}

export class FwegoVersionUpgradeNotificationType extends NotificationType {
  static getType() {
    return 'fwego_version_upgrade'
  }

  getIconComponent() {
    return NotificationImgIcon
  }

  getIconComponentProps() {
    return { icon: FwegoIcon }
  }

  getContentComponent() {
    return FwegoVersionUpgradeNotification
  }
}
