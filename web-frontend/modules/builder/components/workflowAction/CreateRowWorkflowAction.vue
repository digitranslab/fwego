<template>
  <UpsertRowWorkflowActionForm
    :workflow-action="workflowAction"
    :default-values="defaultValues.service"
    @values-changed="values.service = { ...workflowAction.service, ...$event }"
  >
  </UpsertRowWorkflowActionForm>
</template>

<script>
import UpsertRowWorkflowActionForm from '@fwego/modules/integrations/localFwego/components/services/LocalFwegoUpsertRowServiceForm'
import form from '@fwego/modules/core/mixins/form'

export default {
  name: 'CreateRowWorkflowAction',
  components: { UpsertRowWorkflowActionForm },
  mixins: [form],
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
