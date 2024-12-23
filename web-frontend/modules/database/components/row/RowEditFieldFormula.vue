<template>
  <component :is="getComponent(field)" v-bind="$props" read-only></component>
</template>

<script>
import rowEditField from '@fwego/modules/database/mixins/rowEditField'
import RowEditFieldDateReadOnly from '@fwego/modules/database/components/row/RowEditFieldDateReadOnly'
import RowEditFieldLongText from '@fwego/modules/database/components/row/RowEditFieldLongText'
import RowEditFieldText from '@fwego/modules/database/components/row/RowEditFieldText'
import RowEditFieldBoolean from '@fwego/modules/database/components/row/RowEditFieldBoolean'
import RowEditFieldNumber from '@fwego/modules/database/components/row/RowEditFieldNumber'
import RowEditFieldSingleSelectReadOnly from '@fwego/modules/database/components/row/RowEditFieldSingleSelectReadOnly'
import RowEditFieldBlank from '@fwego/modules/database/components/row/RowEditFieldBlank'
import RowEditFieldArray from '@fwego/modules/database/components/row/RowEditFieldArray'

export default {
  name: 'RowEditFieldFormula',
  components: {
    RowEditFieldDateReadOnly,
    RowEditFieldText,
    RowEditFieldLongText,
    RowEditFieldBoolean,
    RowEditFieldNumber,
    RowEditFieldBlank,
    RowEditFieldArray,
    RowEditFieldSingleSelectReadOnly,
  },
  mixins: [rowEditField],
  methods: {
    getComponent(field) {
      const formulaType = this.$registry.get('formula_type', field.formula_type)
      return formulaType.getRowEditFieldComponent(field)
    },
  },
}
</script>
