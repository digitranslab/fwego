<template>
  <RowEditFieldSingleSelect
    :read-only="true"
    :field="field"
    :value="value"
    :workspace-id="workspaceId"
  >
  </RowEditFieldSingleSelect>
</template>

<script>
import RowEditFieldSingleSelect from '@fwego/modules/database/components/row/RowEditFieldSingleSelect'
import baseField from '@fwego/modules/database/mixins/baseField'

export default {
  name: 'RowEditFieldSingleSelectReadOnly',
  components: { RowEditFieldSingleSelect },
  mixins: [baseField],
}
</script>
