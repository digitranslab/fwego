import { ViewDecoratorType } from '@fwego/modules/database/viewDecorators'
import PremiumModal from '@fwego_premium/components/PremiumModal'

import {
  GridViewType,
  GalleryViewType,
} from '@fwego/modules/database/viewTypes'

import { CalendarViewType, KanbanViewType, TimelineViewType } from './viewTypes'

import leftBorderDecoratorImage from '@fwego_premium/assets/images/leftBorderDecorator.svg'
import backgroundDecoratorImage from '@fwego_premium/assets/images/backgroundDecorator.svg'

import LeftBorderColorViewDecorator from '@fwego_premium/components/views/LeftBorderColorViewDecorator'
import BackgroundColorViewDecorator from '@fwego_premium/components/views/BackgroundColorViewDecorator'
import PremiumFeatures from '@fwego_premium/features'

export class LeftBorderColorViewDecoratorType extends ViewDecoratorType {
  static getType() {
    return 'left_border_color'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('viewDecoratorType.leftBorderColor')
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('viewDecoratorType.leftBorderColorDescription')
  }

  getImage() {
    return leftBorderDecoratorImage
  }

  getPlace() {
    return 'first_cell'
  }

  getDeactivatedText() {
    const { i18n } = this.app
    return i18n.t('viewDecoratorType.onlyForPremium')
  }

  getDeactivatedClickModal() {
    return PremiumModal
  }

  isDeactivated(workspaceId) {
    return !this.app.$hasFeature(PremiumFeatures.PREMIUM, workspaceId)
  }

  canAdd({ view }) {
    const { i18n } = this.app

    if (view.decorations.some(({ type }) => type === this.getType())) {
      return [false, i18n.t('viewDecoratorType.onlyOneDecoratorPerView')]
    }
    return [true]
  }

  getComponent(workspaceId) {
    if (!this.isDeactivated(workspaceId)) {
      return LeftBorderColorViewDecorator
    }

    return null
  }

  isCompatible(view) {
    const { store } = this.app

    return (
      [
        GridViewType.getType(),
        GalleryViewType.getType(),
        KanbanViewType.getType(),
        CalendarViewType.getType(),
        TimelineViewType.getType(),
      ].includes(view.type) && !store.getters['page/view/public/getIsPublic']
    )
  }
}

export class BackgroundColorViewDecoratorType extends ViewDecoratorType {
  static getType() {
    return 'background_color'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('viewDecoratorType.backgroundColor')
  }

  getDescription() {
    const { i18n } = this.app
    return i18n.t('viewDecoratorType.backgroundColorDescription')
  }

  getImage() {
    return backgroundDecoratorImage
  }

  getPlace() {
    return 'wrapper'
  }

  getComponent(workspaceId) {
    if (!this.isDeactivated(workspaceId)) {
      return BackgroundColorViewDecorator
    }

    return null
  }

  isCompatible(view) {
    const { store } = this.app

    return (
      [
        GridViewType.getType(),
        GalleryViewType.getType(),
        KanbanViewType.getType(),
        CalendarViewType.getType(),
        TimelineViewType.getType(),
      ].includes(view.type) && !store.getters['page/view/public/getIsPublic']
    )
  }

  getDeactivatedText() {
    const { i18n } = this.app
    return i18n.t('viewDecoratorType.onlyForPremium')
  }

  getDeactivatedClickModal() {
    return PremiumModal
  }

  isDeactivated(workspaceId) {
    return !this.app.$hasFeature(PremiumFeatures.PREMIUM, workspaceId)
  }

  canAdd({ view }) {
    const { i18n } = this.app

    if (view.decorations.some(({ type }) => type === this.getType())) {
      return [false, i18n.t('viewDecoratorType.onlyOneDecoratorPerView')]
    }
    return [true]
  }
}
