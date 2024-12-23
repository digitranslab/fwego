<template>
  <RowEditFieldFile
    :read-only="true"
    :field="field"
    :value="value"
    :workspace-id="workspaceId"
  >
  </RowEditFieldFile>
</template>

<script>
import baseField from '@fwego/modules/database/mixins/baseField'
import RowEditFieldFile from '@fwego/modules/database/components/row/RowEditFieldFile.vue'

export default {
  components: { RowEditFieldFile },
  mixins: [baseField],
}
</script>
