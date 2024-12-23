<template>
  <div class="control__elements">
    <div class="field-date-read-only-timestamp">
      {{ getDate(field, value)
      }}<template v-if="field.date_include_time"
        >&nbsp;{{ getTime(field, value) }}</template
      >
    </div>
  </div>
</template>

<script>
import rowEditField from '@fwego/modules/database/mixins/rowEditField'
import readOnlyDateField from '@fwego/modules/database/mixins/readOnlyDateField'

export default {
  mixins: [rowEditField, readOnlyDateField],
}
</script>
