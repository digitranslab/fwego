import { Registerable } from '@fwego/modules/core/registry'
import RowEditFieldText from '@fwego/modules/database/components/row/RowEditFieldText'
import RowEditFieldLongText from '@fwego/modules/database/components/row/RowEditFieldLongText'
import RowEditFieldNumber from '@fwego/modules/database/components/row/RowEditFieldNumber'
import RowEditFieldDateReadOnly from '@fwego/modules/database/components/row/RowEditFieldDateReadOnly'
import GridViewFieldLongText from '@fwego/modules/database/components/view/grid/fields/GridViewFieldLongText'
import RowEditFieldBoolean from '@fwego/modules/database/components/row/RowEditFieldBoolean'
import FunctionalGridViewFieldLongText from '@fwego/modules/database/components/view/grid/fields/FunctionalGridViewFieldLongText'
import FunctionalGridViewFieldText from '@fwego/modules/database/components/view/grid/fields/FunctionalGridViewFieldText'
import FunctionalGridViewFieldBlank from '@fwego/modules/database/components/view/grid/fields/FunctionalGridViewFieldBlank'
import FunctionalGridViewFieldArray from '@fwego/modules/database/components/view/grid/fields/FunctionalGridViewFieldArray'
import FunctionalGridViewFieldButton from '@fwego/modules/database/components/view/grid/fields/FunctionalGridViewFieldButton'
import FunctionalGridViewFieldLinkURL from '@fwego/modules/database/components/view/grid/fields/FunctionalGridViewFieldLinkURL'
import GridViewFieldArray from '@fwego/modules/database/components/view/grid/fields/GridViewFieldArray'
import RowEditFieldSingleSelectReadOnly from '@fwego/modules/database/components/row/RowEditFieldSingleSelectReadOnly'
import RowEditFieldMultipleSelectReadOnly from '@fwego/modules/database/components/row/RowEditFieldMultipleSelectReadOnly'
import RowEditFieldArray from '@fwego/modules/database/components/row/RowEditFieldArray'
import RowEditFieldLinkURL from '@fwego/modules/database/components/row/RowEditFieldLinkURL'
import RowEditFieldButton from '@fwego/modules/database/components/row/RowEditFieldButton'
import RowEditFieldDurationReadOnly from '@fwego/modules/database/components/row/RowEditFieldDurationReadOnly.vue'
import FunctionalFormulaArrayItem from '@fwego/modules/database/components/formula/array/FunctionalFormulaArrayItem'
import FunctionalFormulaArrayDurationItem from '@fwego/modules/database/components/formula/array/FunctionalFormulaArrayDurationItem'
import FunctionalFormulaArrayNumberItem from '@fwego/modules/database/components/formula/array/FunctionalFormulaArrayNumberItem'
import FunctionalFormulaBooleanArrayItem from '@fwego/modules/database/components/formula/array/FunctionalFormulaBooleanArrayItem'
import FunctionalFormulaDateArrayItem from '@fwego/modules/database/components/formula/array/FunctionalFormulaDateArrayItem'
import FunctionalFormulaSingleSelectArrayItem from '@fwego/modules/database/components/formula/array/FunctionalFormulaSingleSelectArrayItem'
import FunctionalFormulaMultipleSelectArrayItem from '@fwego/modules/database/components/formula/array/FunctionalFormulaMultipleSelectArrayItem'
import FunctionalFormulaLinkArrayItem from '@fwego/modules/database/components/formula/array/FunctionalFormulaLinkArrayItem'
import FunctionalFormulaButtonArrayItem from '@fwego/modules/database/components/formula/array/FunctionalFormulaButtonArrayItem'
import RowCardFieldArray from '@fwego/modules/database/components/card/RowCardFieldArray'
import RowEditFieldBlank from '@fwego/modules/database/components/row/RowEditFieldBlank'
import RowCardFieldBlank from '@fwego/modules/database/components/card/RowCardFieldBlank'
import RowCardFieldLinkURL from '@fwego/modules/database/components/card/RowCardFieldLinkURL'
import RowCardFieldButton from '@fwego/modules/database/components/card/RowCardFieldButton'
import GridViewFieldButton from '@fwego/modules/database/components/view/grid/fields/GridViewFieldButton.vue'
import GridViewFieldLinkURL from '@fwego/modules/database/components/view/grid/fields/GridViewFieldLinkURL.vue'
import GridViewFieldText from '@fwego/modules/database/components/view/grid/fields/GridViewFieldText.vue'
import RowEditFieldFileReadOnly from '@fwego/modules/database/components/row/RowEditFieldFileReadOnly.vue'
import FunctionalGridViewSingleFile from '@fwego/modules/database/components/view/grid/fields/FunctionalGridViewSingleFile.vue'
import FunctionalFormulaFileArrayItem from '@fwego/modules/database/components/formula/array/FunctionalFormulaFileArrayItem.vue'
import SingleFileArrayModal from '@fwego/modules/database/components/view/grid/fields/SingleFileArrayModal.vue'
import GridViewSingleFile from '@fwego/modules/database/components/view/grid/fields/GridViewSingleFile.vue'
import RowEditSingleFileReadOnly from '@fwego/modules/database/components/row/RowEditSingleFileReadOnly.vue'
import RowCardFieldSingleFile from '@fwego/modules/database/components/card/RowCardFieldSingleFile.vue'
import RowEditFieldURL from '@fwego/modules/database/components/row/RowEditFieldURL.vue'
import FunctionalGridViewFieldURL from '@fwego/modules/database/components/view/grid/fields/FunctionalGridViewFieldURL.vue'
import GridViewFieldURL from '@fwego/modules/database/components/view/grid/fields/GridViewFieldURL.vue'
import RowCardFieldURL from '@fwego/modules/database/components/card/RowCardFieldURL.vue'
import FunctionalFormulaURLArrayItem from '@fwego/modules/database/components/formula/array/FunctionalFormulaURLArrayItem.vue'
import { mix } from '@fwego/modules/core/mixins'
import {
  hasEmptyValueFilterMixin,
  hasValueEqualFilterMixin,
  hasValueContainsFilterMixin,
  hasValueContainsWordFilterMixin,
  hasValueLengthIsLowerThanFilterMixin,
  hasSelectOptionIdEqualMixin,
  hasSelectOptionValueContainsFilterMixin,
  hasSelectOptionValueContainsWordFilterMixin,
  formulaArrayFilterMixin,
} from '@fwego/modules/database/arrayFilterMixins'
import _ from 'lodash'
import ViewFilterTypeBoolean from '@fwego/modules/database/components/view/ViewFilterTypeBoolean.vue'
import {
  genericHasAllValuesEqualFilter,
  genericHasValueContainsFilter,
} from '@fwego/modules/database/utils/fieldFilters'
import ViewFilterTypeSelectOptions from '@fwego/modules/database/components/view/ViewFilterTypeSelectOptions.vue'
import ViewFilterTypeDuration from '@fwego/modules/database/components/view/ViewFilterTypeDuration.vue'

export class FwegoFormulaTypeDefinition extends Registerable {
  getIconClass() {
    throw new Error(
      'Not implemented error. This method should return the types icon.'
    )
  }

  getRowEditFieldComponent(field) {
    throw new Error(
      'Not implemented error. This method should return the types row edit component.'
    )
  }

  /**
   * Returns optionally input component for a field / filter type combination
   * @returns {null}
   */
  getFilterInputComponent(field, filterType) {
    return null
  }

  getRowEditArrayFieldComponent() {
    return null
  }

  getFunctionalGridViewFieldComponent() {
    return this.app.$registry
      .get('field', this.getFieldType())
      .getFunctionalGridViewFieldComponent()
  }

  getGridViewFieldComponent() {
    return this.app.$registry
      .get('field', this.getFieldType())
      .getGridViewFieldComponent()
  }

  getFieldType() {
    throw new Error(
      'Not implemented error. This method should return the types corresponding' +
        ' Fwego field type that should be used for things like sort indicators etc.'
    )
  }

  getSortOrder() {
    throw new Error(
      'Not implemented error. This method should return a number indicating how it ' +
        'should be sorted compared to other formula types when displayed.'
    )
  }

  getDocsResponseExample(field) {
    return this.app.$registry
      .get('field', this.getFieldType())
      .getDocsResponseExample(field)
  }

  getDocsDataType(field) {
    return this.app.$registry
      .get('field', this.getFieldType())
      .getDocsDataType(field)
  }

  prepareValueForCopy(field, value) {
    return this.app.$registry
      .get('field', this.getFieldType())
      .prepareValueForCopy(field, value)
  }

  parseInputValue(field, value) {
    return this.app.$registry
      .get('field', this.getFieldType())
      .parseInputValue(field, value)
  }

  getCardComponent() {
    return this.app.$registry
      .get('field', this.getFieldType())
      .getCardComponent()
  }

  getFunctionalFieldArrayComponent() {
    return FunctionalFormulaArrayItem
  }

  getCanSortInView(field) {
    return true
  }

  canBeSortedWhenInArray(field) {
    return false
  }

  getItemIsInNestedValueObjectWhenInArray() {
    return true
  }

  /**
   * The extra modal is a component that can be opened by emitting the `show` event up.
   */
  getExtraModal() {
    return null
  }

  getSort(name, order, field) {
    const underlyingFieldType = this.app.$registry.get(
      'field',
      this.getFieldType()
    )
    return underlyingFieldType.getSort(name, order, field)
  }

  _mapFormulaTypeToFieldType(formulaType) {
    return this.app.$registry.get('formula_type', formulaType).getFieldType()
  }

  getSortIndicator(field) {
    const underlyingFieldType = this.app.$registry.get(
      'field',
      this._mapFormulaTypeToFieldType(field.formula_type)
    )
    return underlyingFieldType.getSortIndicator()
  }

  mapToSortableArray(element) {
    return this.getItemIsInNestedValueObjectWhenInArray()
      ? element.value
      : element
  }

  toHumanReadableString(field, value) {
    const underlyingFieldType = this.app.$registry.get(
      'field',
      this.getFieldType()
    )
    return underlyingFieldType.toHumanReadableString(field, value)
  }

  canRepresentDate() {
    return false
  }

  canGroupByInView() {
    return false
  }

  canRepresentFiles(field) {
    return false
  }
}

export class FwegoFormulaTextType extends mix(
  hasEmptyValueFilterMixin,
  hasValueEqualFilterMixin,
  hasValueContainsFilterMixin,
  hasValueContainsWordFilterMixin,
  hasValueLengthIsLowerThanFilterMixin,
  FwegoFormulaTypeDefinition
) {
  static getType() {
    return 'text'
  }

  getFieldType() {
    return 'text'
  }

  getIconClass() {
    return 'iconoir-text'
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldLongText
  }

  getGridViewFieldComponent() {
    return GridViewFieldLongText
  }

  getFunctionalGridViewFieldComponent() {
    return FunctionalGridViewFieldLongText
  }

  getSortOrder() {
    return 1
  }

  canBeSortedWhenInArray(field) {
    return true
  }

  canGroupByInView() {
    return true
  }
}

export class FwegoFormulaCharType extends mix(
  hasEmptyValueFilterMixin,
  hasValueEqualFilterMixin,
  hasValueContainsFilterMixin,
  hasValueContainsWordFilterMixin,
  hasValueLengthIsLowerThanFilterMixin,
  FwegoFormulaTypeDefinition
) {
  static getType() {
    return 'char'
  }

  getFieldType() {
    return 'text'
  }

  getIconClass() {
    return 'iconoir-text'
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldText
  }

  getFunctionalGridViewFieldComponent() {
    return FunctionalGridViewFieldText
  }

  getSortOrder() {
    return 1
  }

  canBeSortedWhenInArray(field) {
    return true
  }

  canGroupByInView() {
    return true
  }
}

export class FwegoFormulaNumberType extends FwegoFormulaTypeDefinition {
  static getType() {
    return 'number'
  }

  getFieldType() {
    return 'number'
  }

  getIconClass() {
    return 'fwego-icon-hashtag'
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldNumber
  }

  getFunctionalFieldArrayComponent() {
    return FunctionalFormulaArrayNumberItem
  }

  getSortOrder() {
    return 2
  }

  canBeSortedWhenInArray(field) {
    return true
  }

  canGroupByInView() {
    return true
  }
}

export class FwegoFormulaBooleanType extends FwegoFormulaTypeDefinition {
  static getType() {
    return 'boolean'
  }

  getFieldType() {
    return 'boolean'
  }

  getIconClass() {
    return 'fwego-icon-circle-checked'
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldBoolean
  }

  getSortOrder() {
    return 3
  }

  getFunctionalFieldArrayComponent() {
    return FunctionalFormulaBooleanArrayItem
  }

  canBeSortedWhenInArray(field) {
    return true
  }

  canGroupByInView() {
    return true
  }

  getFilterInputComponent(field, filterType) {
    return ViewFilterTypeBoolean
  }

  getHasAllValuesEqualFilterFunction(field) {
    return (cellValue, filterValue) => {
      const parsedValue = this.parseInputValue(field, filterValue)
      return genericHasAllValuesEqualFilter(cellValue, parsedValue)
    }
  }

  getHasValueContainsFilterFunction(field) {
    return (cellValue, filterValue) => {
      const parsedValue = this.parseInputValue(field, filterValue)
      return genericHasValueContainsFilter(cellValue, parsedValue)
    }
  }

  getHasValueEqualFilterFunction(field) {
    return this.app.$registry
      .get('field', this.getFieldType())
      .getHasValueEqualFilterFunction(field)
  }

  parseInputValue(field, filterValue) {
    if (filterValue === '') {
      return false
    }
    return super.parseInputValue(field, filterValue)
  }
}

export class FwegoFormulaDateType extends FwegoFormulaTypeDefinition {
  static getType() {
    return 'date'
  }

  getFieldType() {
    return 'date'
  }

  getIconClass() {
    return 'iconoir-calendar'
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldDateReadOnly
  }

  getSortOrder() {
    return 4
  }

  getFunctionalFieldArrayComponent() {
    return FunctionalFormulaDateArrayItem
  }

  canRepresentDate() {
    return true
  }

  canBeSortedWhenInArray(field) {
    return true
  }

  mapToSortableArray(element) {
    return element.value
  }

  canGroupByInView() {
    return true
  }
}

export class FwegoFormulaDurationType extends FwegoFormulaTypeDefinition {
  static getType() {
    return 'duration'
  }

  getFieldType() {
    return 'duration'
  }

  getIconClass() {
    return 'iconoir-clock-rotate-right'
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldDurationReadOnly
  }

  getFilterInputComponent(field, filterType) {
    return ViewFilterTypeDuration
  }

  getSortOrder() {
    return 5
  }

  canGroupByInView() {
    return true
  }

  getFunctionalFieldArrayComponent() {
    return FunctionalFormulaArrayDurationItem
  }

  canBeSortedWhenInArray(field) {
    return true
  }
}

// Deprecated, use FwegoFormulaDurationType instead.
export class FwegoFormulaDateIntervalType extends FwegoFormulaTypeDefinition {
  static getType() {
    return 'date_interval'
  }

  getFieldType() {
    return 'text'
  }

  getIconClass() {
    return 'fwego-icon-history'
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldText
  }

  getGridViewFieldComponent() {
    return GridViewFieldText
  }

  getFunctionalGridViewFieldComponent() {
    return FunctionalGridViewFieldText
  }

  getSortOrder() {
    return 5
  }

  canGroupByInView() {
    return true
  }
}

// This type only exists in the frontend and only is referenced by a few weird frontend
// function defs which we want to show as a 'special' type in the GUI.
export class FwegoFormulaSpecialType extends FwegoFormulaTypeDefinition {
  static getType() {
    return 'special'
  }

  getFieldType() {
    return 'text'
  }

  getIconClass() {
    return 'fwego-icon-formula'
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldText
  }

  getFunctionalGridViewFieldComponent() {
    return FunctionalGridViewFieldText
  }

  getSortOrder() {
    return 6
  }
}

export class FwegoFormulaInvalidType extends FwegoFormulaTypeDefinition {
  static getType() {
    return 'invalid'
  }

  getFieldType() {
    return 'text'
  }

  getIconClass() {
    return 'iconoir-warning-triangle'
  }

  getCardComponent() {
    return RowCardFieldBlank
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldBlank
  }

  getFunctionalGridViewFieldComponent() {
    return FunctionalGridViewFieldBlank
  }

  getSortOrder() {
    return 9
  }

  getCanSortInView(field) {
    return false
  }
}

export class FwegoFormulaArrayType extends mix(
  formulaArrayFilterMixin,
  FwegoFormulaTypeDefinition
) {
  static getType() {
    return 'array'
  }

  getFieldType(field) {
    return 'text'
  }

  parseInputValue(field, value) {
    return this.getSubType(field)?.parseInputValue(field, value)
  }

  getIconClass() {
    return 'iconoir-list'
  }

  getCardComponent() {
    return RowCardFieldArray
  }

  getRowEditFieldComponent(field) {
    const arrayOverride =
      this.getSubType(field)?.getRowEditArrayFieldComponent()
    if (arrayOverride) {
      return arrayOverride
    } else {
      return RowEditFieldArray
    }
  }

  getFilterInputComponent(field, filterType) {
    return this.getSubType(field)?.getFilterInputComponent(field, filterType)
  }

  getFunctionalGridViewFieldComponent() {
    return FunctionalGridViewFieldArray
  }

  getGridViewFieldComponent() {
    return GridViewFieldArray
  }

  getSortOrder() {
    return 7
  }

  prepareValueForCopy(field, value) {
    const subType = this.getSubType(field)
    return value
      .map((v) => {
        return subType.prepareValueForCopy(
          field,
          subType.getItemIsInNestedValueObjectWhenInArray() ? v.value : v
        )
      })
      .join(', ')
  }

  getDocsResponseExample(field) {
    if (field.array_formula_type != null) {
      const subType = this.getSubType(field)
      const value = this.app.$registry
        .get('formula_type', field.array_formula_type)
        .getDocsResponseExample(field)
      if (subType.getItemIsInNestedValueObjectWhenInArray()) {
        return [{ id: 0, value }]
      } else {
        return [value]
      }
    } else {
      return null
    }
  }

  getDocsDataType(field) {
    return 'array'
  }

  getCanSortInView(field) {
    const subType = this.getSubType(field)
    return subType.canBeSortedWhenInArray(field)
  }

  canRepresentFiles(field) {
    const subType = this.getSubType(field)
    return subType.canRepresentFiles(field)
  }

  getSort(name, order, field) {
    const subType = this.getSubType(field)

    const innerSortFunction = subType.getSort(name, order, field)

    return (a, b) => {
      const valuesA = a[name].map(subType.mapToSortableArray.bind(subType))
      const valuesB = b[name].map(subType.mapToSortableArray.bind(subType))

      for (let i = 0; i < Math.max(valuesA.length, valuesB.length); i++) {
        let compared = 0

        const isAdefined = valuesA[i] || valuesA[i] === ''
        const isBdefined = valuesB[i] || valuesB[i] === ''

        if (isAdefined && isBdefined) {
          compared = innerSortFunction(
            { [name]: valuesA[i] },
            { [name]: valuesB[i] }
          )
        } else if (
          isAdefined &&
          (valuesB[i] === undefined || valuesB[i] === false)
        ) {
          compared = order === 'ASC' ? 1 : -1
        } else if (
          isBdefined &&
          (valuesA[i] === undefined || valuesA[i] === false)
        ) {
          compared = order === 'ASC' ? -1 : 1
        } else if (isAdefined && valuesB[i] === null) {
          compared = order === 'ASC' ? -1 : 1
        } else if (isBdefined && valuesA[i] === null) {
          compared = order === 'ASC' ? 1 : -1
        } else if (valuesA[i] === null && valuesB[i] === undefined) {
          compared = order === 'ASC' ? 1 : -1
        } else if (valuesA[i] === undefined && valuesB[i] === null) {
          compared = order === 'ASC' ? -1 : 1
        } else if (valuesA[i] === false && valuesB[i] !== false) {
          compared = order === 'ASC' ? 1 : -1
        } else if (valuesA[i] !== false && valuesB[i] === false) {
          compared = order === 'ASC' ? -1 : 1
        }

        if (compared !== 0) {
          return compared
        }
      }
    }
  }

  getSortIndicator(field) {
    const underlyingFieldType = this.app.$registry.get(
      'field',
      this._mapFormulaTypeToFieldType(field.array_formula_type)
    )
    return underlyingFieldType.getSortIndicator()
  }

  toHumanReadableString(field, value) {
    const subType = this.getSubType(field)
    return value
      .map((v) => {
        return subType.toHumanReadableString(
          field,
          subType.getItemIsInNestedValueObjectWhenInArray() ? v.value : v
        )
      })
      .join(', ')
  }

  canGroupByInView() {
    return false
  }
}

export class FwegoFormulaFileType extends FwegoFormulaTypeDefinition {
  static getType() {
    return 'single_file'
  }

  getFieldType() {
    return 'file'
  }

  getIconClass() {
    return 'iconoir-empty-page'
  }

  getRowEditArrayFieldComponent() {
    return RowEditFieldFileReadOnly
  }

  getRowEditFieldComponent(field) {
    return RowEditSingleFileReadOnly
  }

  getItemIsInNestedValueObjectWhenInArray() {
    return false
  }

  getFunctionalGridViewFieldComponent() {
    return FunctionalGridViewSingleFile
  }

  getGridViewFieldComponent() {
    return GridViewSingleFile
  }

  getFunctionalFieldArrayComponent() {
    return FunctionalFormulaFileArrayItem
  }

  getExtraModal() {
    return SingleFileArrayModal
  }

  getSortOrder() {
    return 11
  }

  getCanSortInView(field) {
    return false
  }

  canBeSortedWhenInArray(field) {
    return false
  }

  canGroupByInView() {
    return false
  }

  getDocsResponseExample(field) {
    return {
      url: 'https://files.fwego.io/user_files/VXotniBOVm8tbstZkKsMKbj2Qg7KmPvn_39d354a76abe56baaf569ad87d0333f58ee4bf3eed368e3b9dc736fd18b09dfd.png',
      thumbnails: {
        tiny: {
          url: 'https://files.fwego.io/media/thumbnails/tiny/VXotniBOVm8tbstZkKsMKbj2Qg7KmPvn_39d354a76abe56baaf569ad87d0333f58ee4bf3eed368e3b9dc736fd18b09dfd.png',
          width: 21,
          height: 21,
        },
        small: {
          url: 'https://files.fwego.io/media/thumbnails/small/VXotniBOVm8tbstZkKsMKbj2Qg7KmPvn_39d354a76abe56baaf569ad87d0333f58ee4bf3eed368e3b9dc736fd18b09dfd.png',
          width: 48,
          height: 48,
        },
      },
      name: 'VXotniBOVm8tbstZkKsMKbj2Qg7KmPvn_39d354a76abe56baaf569ad87d0333f58ee4bf3eed368e3b9dc736fd18b09dfd.png',
      size: 229940,
      mime_type: 'image/png',
      is_image: true,
      image_width: 1280,
      image_height: 585,
      uploaded_at: '2020-11-17T12:16:10.035234+00:00',
    }
  }

  getDocsDataType(field) {
    return 'single_file'
  }

  prepareValueForCopy(field, value) {
    return `${value?.visible_name} (${value?.url})`
  }

  getCardComponent() {
    return RowCardFieldSingleFile
  }

  toHumanReadableString(field, value) {
    return value?.visible_name || ''
  }

  canRepresentFiles(field) {
    return true
  }
}

export class FwegoFormulaSingleSelectType extends mix(
  hasEmptyValueFilterMixin,
  hasSelectOptionIdEqualMixin,
  hasSelectOptionValueContainsFilterMixin,
  hasSelectOptionValueContainsWordFilterMixin,
  FwegoFormulaTypeDefinition
) {
  static getType() {
    return 'single_select'
  }

  getFieldType() {
    return 'single_select'
  }

  getIconClass() {
    return 'fwego-icon-single-select'
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldSingleSelectReadOnly
  }

  getFunctionalFieldArrayComponent() {
    return FunctionalFormulaSingleSelectArrayItem
  }

  getFilterInputComponent(field, filterType) {
    return ViewFilterTypeSelectOptions
  }

  getSortOrder() {
    return 8
  }

  getCanSortInView(field) {
    return true
  }

  canBeSortedWhenInArray(field) {
    return true
  }

  mapToSortableArray(element) {
    return element.value
  }

  canGroupByInView() {
    return false
  }
}

export class FwegoFormulaMultipleSelectType extends FwegoFormulaTypeDefinition {
  static getType() {
    return 'multiple_select'
  }

  getFieldType() {
    return 'multiple_select'
  }

  getIconClass() {
    return 'fwego-icon-multiple-select'
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldMultipleSelectReadOnly
  }

  getFunctionalFieldArrayComponent() {
    return FunctionalFormulaMultipleSelectArrayItem
  }

  getSortOrder() {
    return 8
  }

  getCanSortInView(field) {
    return false
  }

  canBeSortedWhenInArray(field) {
    return false
  }

  mapToSortableArray(element) {
    return element.value
  }

  canGroupByInView() {
    return false
  }
}

export class FwegoFormulaLinkType extends FwegoFormulaTypeDefinition {
  static getType() {
    return 'link'
  }

  getFieldType() {
    return 'text'
  }

  getIconClass() {
    return 'iconoir-link'
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldLinkURL
  }

  getFunctionalGridViewFieldComponent() {
    return FunctionalGridViewFieldLinkURL
  }

  getGridViewFieldComponent() {
    return GridViewFieldLinkURL
  }

  getSortOrder() {
    return 10
  }

  getFunctionalFieldArrayComponent() {
    return FunctionalFormulaLinkArrayItem
  }

  toHumanReadableString(field, value) {
    if (value?.label) {
      return `${value.label} (${value.url})`
    } else {
      return value.url
    }
  }

  getCardComponent() {
    return RowCardFieldLinkURL
  }

  prepareValueForCopy(field, value) {
    return this.toHumanReadableString(field, value)
  }

  getCanSortInView(field) {
    return false
  }

  canGroupByInView() {
    return false
  }
}

export class FwegoFormulaURLType extends mix(
  hasEmptyValueFilterMixin,
  hasValueEqualFilterMixin,
  hasValueContainsFilterMixin,
  hasValueContainsWordFilterMixin,
  hasValueLengthIsLowerThanFilterMixin,
  FwegoFormulaTypeDefinition
) {
  static getType() {
    return 'url'
  }

  getFieldType() {
    return 'url'
  }

  getIconClass() {
    return 'iconoir-link'
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldURL
  }

  getFunctionalGridViewFieldComponent() {
    return FunctionalGridViewFieldURL
  }

  getGridViewFieldComponent() {
    return GridViewFieldURL
  }

  getSortOrder() {
    return 10
  }

  getFunctionalFieldArrayComponent() {
    return FunctionalFormulaURLArrayItem
  }

  toHumanReadableString(field, value) {
    if (_.isString(value)) {
      return value
    }
    if (value?.label) {
      return `${value.label} (${value.url})`
    } else {
      return value.url
    }
  }

  getCardComponent() {
    return RowCardFieldURL
  }

  prepareValueForCopy(field, value) {
    return this.toHumanReadableString(field, value)
  }

  getCanSortInView(field) {
    return false
  }

  canGroupByInView() {
    return false
  }
}

export class FwegoFormulaButtonType extends FwegoFormulaLinkType {
  static getType() {
    return 'button'
  }

  getRowEditFieldComponent(field) {
    return RowEditFieldButton
  }

  getFunctionalGridViewFieldComponent() {
    return FunctionalGridViewFieldButton
  }

  getGridViewFieldComponent() {
    return GridViewFieldButton
  }

  getCardComponent() {
    return RowCardFieldButton
  }

  getFunctionalFieldArrayComponent() {
    return FunctionalFormulaButtonArrayItem
  }
}
