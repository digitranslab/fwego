<template>
  <WorkspacesAdminTable></WorkspacesAdminTable>
</template>

<script>
import WorkspacesAdminTable from '@fwego/modules/core/components/admin/workspaces/WorkspacesAdminTable'

export default {
  components: { WorkspacesAdminTable },
  layout: 'app',
  middleware: 'staff',
}
</script>
