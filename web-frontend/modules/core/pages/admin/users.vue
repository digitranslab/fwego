<template>
  <UsersAdminTable></UsersAdminTable>
</template>

<script>
import UsersAdminTable from '@fwego/modules/core/components/admin/users/UsersAdminTable'

export default {
  components: { UsersAdminTable },
  layout: 'app',
  middleware: 'staff',
}
</script>
