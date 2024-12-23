<template functional>
  <div class="card-text">
    {{ $options.methods.formatNumberValue(props.field, props.value) }}
  </div>
</template>

<script>
import numberField from '@fwego/modules/database/mixins/numberField'

export default {
  height: 16,
  mixins: [numberField],
}
</script>
