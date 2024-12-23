import {
  FieldType,
  FormulaFieldType,
} from '@fwego/modules/database/fieldTypes'

import GridViewFieldAI from '@fwego_premium/components/views/grid/fields/GridViewFieldAI'
import FunctionalGridViewFieldAI from '@fwego_premium/components/views/grid/fields/FunctionalGridViewFieldAI'
import RowEditFieldAI from '@fwego_premium/components/row/RowEditFieldAI'
import FieldAISubForm from '@fwego_premium/components/field/FieldAISubForm'
import FormulaFieldAI from '@fwego_premium/components/field/FormulaFieldAI'
import GridViewFieldAIGenerateValuesContextItem from '@fwego_premium/components/views/grid/fields/GridViewFieldAIGenerateValuesContextItem'
import PremiumModal from '@fwego_premium/components/PremiumModal'
import PremiumFeatures from '@fwego_premium/features'

export class AIFieldType extends FieldType {
  static getType() {
    return 'ai'
  }

  getIconClass() {
    return 'iconoir-magic-wand'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('premiumFieldType.ai')
  }

  getIsReadOnly() {
    return true
  }

  getGridViewFieldComponent() {
    return GridViewFieldAI
  }

  getFunctionalGridViewFieldComponent() {
    return FunctionalGridViewFieldAI
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldAI
  }

  getFormComponent() {
    return FieldAISubForm
  }

  getCardComponent(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getCardComponent(field)
  }

  getRowHistoryEntryComponent(field) {
    return null
  }

  getFormViewFieldComponents(field) {
    return {}
  }

  getEmptyValue(field) {
    return null
  }

  getCardValueHeight(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getCardValueHeight(field)
  }

  getSort(name, order, field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getSort(name, order, field)
  }

  getCanSortInView(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getCanSortInView(field)
  }

  getDocsDataType(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getDocsDataType(field)
  }

  getDocsDescription(field) {
    const { i18n } = this.app
    return i18n.t('premiumFieldType.aiDescription')
  }

  getDocsRequestExample(field) {
    return 'read only'
  }

  getDocsResponseExample(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getDocsResponseExample(field)
  }

  prepareValueForCopy(field, value) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .prepareValueForCopy(field, value)
  }

  getContainsFilterFunction(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getContainsFilterFunction(field)
  }

  getContainsWordFilterFunction(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getContainsWordFilterFunction(field)
  }

  toHumanReadableString(field, value) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .toHumanReadableString(field, value)
  }

  getSortIndicator(field, registry) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getSortIndicator(field, registry)
  }

  canRepresentDate(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .canRepresentDate(field)
  }

  getCanGroupByInView(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getCanGroupByInView(field)
  }

  parseInputValue(field, value) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .parseInputValue(field, value)
  }

  canRepresentFiles(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .canRepresentFiles(field)
  }

  getHasEmptyValueFilterFunction(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getHasEmptyValueFilterFunction(field)
  }

  getHasValueContainsFilterFunction(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getHasValueContainsFilterFunction(field)
  }

  getHasValueContainsWordFilterFunction(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getHasValueContainsWordFilterFunction(field)
  }

  getHasValueLengthIsLowerThanFilterFunction(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getHasValueLengthIsLowerThanFilterFunction(field)
  }

  getGroupByComponent(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getGroupByComponent(field)
  }

  getGroupByIndicator(field, registry) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getGroupByIndicator(field, registry)
  }

  getRowValueFromGroupValue(field, value) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getRowValueFromGroupValue(field, value)
  }

  getGroupValueFromRowValue(field, value) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .getGroupValueFromRowValue(field, value)
  }

  isEqual(field, value1, value2) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .isEqual(field, value1, value2)
  }

  canBeReferencedByFormulaField(field) {
    return this.app.$registry
      .get('aiFieldOutputType', field.ai_output_type)
      .getFwegoFieldType()
      .canBeReferencedByFormulaField(field)
  }

  getGridViewContextItemsOnCellsSelection(field) {
    return [GridViewFieldAIGenerateValuesContextItem]
  }

  isEnabled(workspace) {
    return Object.values(workspace.generative_ai_models_enabled).some(
      (models) => models.length > 0
    )
  }

  isDeactivated(workspaceId) {
    return !this.app.$hasFeature(PremiumFeatures.PREMIUM, workspaceId)
  }

  getDeactivatedClickModal(workspaceId) {
    return PremiumModal
  }
}

export class PremiumFormulaFieldType extends FormulaFieldType {
  getAdditionalFormInputComponents() {
    return [FormulaFieldAI]
  }
}
