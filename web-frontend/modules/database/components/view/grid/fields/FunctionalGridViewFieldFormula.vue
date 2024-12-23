<template functional>
  <component
    :is="$options.methods.getComponent(props.field, parent.$registry)"
    v-if="$options.methods.getComponent(props.field, parent.$registry)"
    :field="props.field"
    :value="props.value"
  ></component>
  <div v-else class="grid-view__cell cell-error">Unknown Field Type</div>
</template>
<script>
import FunctionalGridViewFieldBoolean from '@fwego/modules/database/components/view/grid/fields/FunctionalGridViewFieldBoolean'
import FunctionalGridViewFieldDate from '@fwego/modules/database/components/view/grid/fields/FunctionalGridViewFieldDate'
import FunctionalGridViewFieldNumber from '@fwego/modules/database/components/view/grid/fields/FunctionalGridViewFieldNumber'
import FunctionalGridViewFieldText from '@fwego/modules/database/components/view/grid/fields/FunctionalGridViewFieldText'
import FunctionalGridViewSingleFile from '@fwego/modules/database/components/view/grid/fields/FunctionalGridViewSingleFile'

export default {
  name: 'FunctionalGridViewFieldFormula',
  components: {
    FunctionalGridViewFieldDate,
    FunctionalGridViewFieldText,
    FunctionalGridViewFieldBoolean,
    FunctionalGridViewFieldNumber,
    FunctionalGridViewSingleFile,
  },
  methods: {
    getComponent(field, $registry) {
      const formulaType = $registry.get('formula_type', field.formula_type)
      return formulaType.getFunctionalGridViewFieldComponent()
    },
  },
}
</script>
