<template>
  <div class="control__elements">
    <div class="field-rating">
      <Rating
        :rating-style="field.style"
        :color="field.color"
        :value="value"
        :max-value="field.max_value"
        :read-only="readOnly"
        @update="update"
      />
    </div>
  </div>
</template>

<script>
import rowEditField from '@fwego/modules/database/mixins/rowEditField'

import Rating from '@fwego/modules/database/components/Rating'

export default {
  components: { Rating },
  mixins: [rowEditField],
  methods: {
    update(newValue) {
      this.$emit('update', newValue, this.value)
    },
  },
}
</script>
