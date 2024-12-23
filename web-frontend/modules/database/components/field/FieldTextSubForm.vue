<template>
  <FormGroup>
    <FormInput
      ref="text_default"
      v-model="values.text_default"
      type="text"
      :placeholder="$t('fieldTextSubForm.placeholder')"
    ></FormInput>
  </FormGroup>
</template>

<script>
import form from '@fwego/modules/core/mixins/form'

import fieldSubForm from '@fwego/modules/database/mixins/fieldSubForm'

export default {
  name: 'FieldTextSubForm',
  mixins: [form, fieldSubForm],
  data() {
    return {
      allowedValues: ['text_default'],
      values: {
        text_default: '',
      },
    }
  },
  methods: {
    isFormValid() {
      return true
    },
  },
}
</script>
