<template>
  <div ref="cell" class="grid-view__cell">
    <div class="grid-field-button">
      <Button
        v-if="isValid(value)"
        tag="a"
        size="tiny"
        type="secondary"
        rel="nofollow noopener noreferrer"
        :href="value && value.url"
        target="_blank"
      >
        {{ getLabelOrURL(value) }}
      </Button>
      <Button v-else type="secondary" tag="a" disabled>
        {{ getLabelOrURL(value) }}
      </Button>
    </div>
  </div>
</template>

<script>
import gridField from '@fwego/modules/database/mixins/gridField'
import gridFieldInput from '@fwego/modules/database/mixins/gridFieldInput'
import linkURLField from '@fwego/modules/database/mixins/linkURLField'
export default {
  name: 'GridViewFieldButton',
  mixins: [gridField, gridFieldInput, linkURLField],
}
</script>
