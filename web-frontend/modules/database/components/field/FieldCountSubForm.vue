<template>
  <div>
    <FieldSelectThroughFieldSubForm
      :fields="allFieldsInTable"
      :database="database"
      :default-values="defaultValues"
    ></FieldSelectThroughFieldSubForm>
  </div>
</template>

<script>
import form from '@fwego/modules/core/mixins/form'
import fieldSubForm from '@fwego/modules/database/mixins/fieldSubForm'
import FieldSelectThroughFieldSubForm from '@fwego/modules/database/components/field/FieldSelectThroughFieldSubForm'

export default {
  name: 'FieldCountSubForm',
  components: { FieldSelectThroughFieldSubForm },
  mixins: [form, fieldSubForm],
  data() {
    return {
      allowedValues: [],
      values: {},
    }
  },
  validations: {},
}
</script>
