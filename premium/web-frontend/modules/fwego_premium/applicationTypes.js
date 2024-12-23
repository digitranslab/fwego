import { DatabaseApplicationType } from '@fwego/modules/database/applicationTypes'
import GridViewRowExpandButtonWithCommentCount from '@fwego_premium/components/row_comments/GridViewRowExpandButtonWithCommentCount'

export class PremiumDatabaseApplicationType extends DatabaseApplicationType {
  getRowExpandButtonComponent() {
    return GridViewRowExpandButtonWithCommentCount
  }
}
