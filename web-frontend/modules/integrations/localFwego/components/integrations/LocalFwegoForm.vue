<template>
  <div>
    <FormGroup :label="$t('localFwegoForm.user')" required small-label>
      <div class="local-fwego-form__user">
        <Presentation
          v-if="values.authorized_user"
          :title="values.authorized_user.first_name"
          :subtitle="values.authorized_user.username"
          :initials="values.authorized_user.first_name | nameAbbreviation"
          avatar-color="blue"
        />
        <div>{{ $t('localFwegoForm.userMessage') }}</div>
      </div>
    </FormGroup>
  </div>
</template>

<script>
import form from '@fwego/modules/core/mixins/form'

export default {
  mixins: [form],
  props: {
    application: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      values: {
        authorized_user: {},
      },
      allowedValues: ['authorized_user'],
    }
  },
}
</script>
