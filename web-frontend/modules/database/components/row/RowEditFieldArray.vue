<template>
  <div class="control__elements">
    <FunctionalFormulaArrayItems
      class="row-edit-array-field"
      :field="field"
      :value="value"
      :selected="true"
    >
    </FunctionalFormulaArrayItems>
  </div>
</template>

<script>
import rowEditField from '@fwego/modules/database/mixins/rowEditField'
import FunctionalFormulaArrayItems from '@fwego/modules/database/components/formula/array/FunctionalFormulaArrayItems'

export default {
  name: 'RowEditFieldArray',
  components: {
    FunctionalFormulaArrayItems,
  },
  mixins: [rowEditField],
}
</script>
