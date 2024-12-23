<template>
  <form @submit.prevent>
    <LocalFwegoServiceForm
      enable-row-id
      :default-values="defaultValues.service"
      @values-changed="
        values.service = { ...workflowAction.service, ...$event }
      "
    ></LocalFwegoServiceForm>
  </form>
</template>

<script>
import form from '@fwego/modules/core/mixins/form'
import LocalFwegoServiceForm from '@fwego/modules/integrations/localFwego/components/services/LocalFwegoServiceForm'

export default {
  name: 'DeleteRowWorkflowActionForm',
  components: {
    LocalFwegoServiceForm,
  },
  mixins: [form],
  inject: ['builder'],
  props: {
    workflowAction: {
      type: Object,
      required: false,
      default: null,
    },
  },
  data() {
    return {
      allowedValues: ['service'],
      values: {
        service: {},
      },
    }
  },
}
</script>
