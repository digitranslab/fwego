<template>
  <MembersTable :workspace="workspace" />
</template>

<script>
import MembersTable from '@fwego/modules/core/components/settings/members/MembersTable'

export default {
  name: 'Members',
  components: { MembersTable },
  props: {
    workspace: {
      type: Object,
      required: true,
    },
  },
}
</script>
