<template>
  <DashboardHelp v-if="settings.show_fwego_help_request"></DashboardHelp>
</template>

<script>
import { mapGetters } from 'vuex'
import DashboardHelp from '@fwego/modules/core/components/dashboard/DashboardHelp'

export default {
  name: 'EnterpriseSettingsOverrideDashboardHelp',
  components: { DashboardHelp },
  computed: {
    ...mapGetters({
      settings: 'settings/get',
    }),
  },
}
</script>
