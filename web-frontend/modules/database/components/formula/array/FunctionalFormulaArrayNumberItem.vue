<template functional>
  <div v-if="props.value !== null" class="array-field__item">
    <div class="array-field__ellipsis">
      {{ $options.methods.formatNumberValue(props.field, props.value) }}
    </div>
  </div>
</template>

<script>
import numberField from '@fwego/modules/database/mixins/numberField'
export default {
  name: 'FunctionalFormulaArrayNumberItem',
  mixins: [numberField],
}
</script>
