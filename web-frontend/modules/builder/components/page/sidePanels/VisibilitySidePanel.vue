<template>
  <VisibilityForm
    ref="panelForm"
    :default-values="defaultValues"
    @values-changed="onChange($event)"
  />
</template>

<script>
import elementSidePanel from '@fwego/modules/builder/mixins/elementSidePanel'
import VisibilityForm from '@fwego/modules/builder/components/elements/components/forms/VisibilityForm'
export default {
  name: 'VisibilitySidePanel',
  components: { VisibilityForm },
  mixins: [elementSidePanel],
  data() {
    return {}
  },
}
</script>
