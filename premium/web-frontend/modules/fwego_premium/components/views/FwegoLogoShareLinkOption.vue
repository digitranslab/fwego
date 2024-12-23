<template>
  <div
    v-tooltip="tooltipText"
    class="view-sharing__option"
    :class="{ 'view-sharing__option--disabled': !hasPremiumFeatures }"
    @click="click"
  >
    <SwitchInput
      small
      :value="!view.show_logo"
      :disabled="!hasPremiumFeatures"
      @input="update"
    >
      <img src="@fwego/modules/core/static/img/fwego-icon.svg" />
      <span>
        {{ $t('shareLinkOptions.fwegoLogo.label') }}
      </span>
      <i v-if="!hasPremiumFeatures" class="deactivated-label iconoir-lock" />
    </SwitchInput>

    <PremiumModal
      v-if="!hasPremiumFeatures"
      ref="premiumModal"
      :workspace="workspace"
      :name="$t('shareLinkOptions.fwegoLogo.premiumModalName')"
    ></PremiumModal>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import ViewPremiumService from '@fwego_premium/services/view'
import { notifyIf } from '@fwego/modules/core/utils/error'
import PremiumModal from '@fwego_premium/components/PremiumModal'
import PremiumFeatures from '@fwego_premium/features'

export default {
  name: 'FwegoLogoShareLinkOption',
  components: { PremiumModal },

  props: {
    view: {
      type: Object,
      required: true,
    },
  },
  computed: {
    ...mapGetters({
      additionalUserData: 'auth/getAdditionalUserData',
    }),
    workspace() {
      return this.$store.getters['application/get'](this.view.table.database_id)
        .workspace
    },
    hasPremiumFeatures() {
      return this.$hasFeature(PremiumFeatures.PREMIUM, this.workspace.id)
    },
    tooltipText() {
      if (this.hasPremiumFeatures) {
        return null
      } else {
        return this.$t('premium.deactivated')
      }
    },
  },
  methods: {
    async update(value) {
      const showLogo = !value
      try {
        // We are being optimistic that the request will succeed.
        this.$emit('update-view', { ...this.view, show_logo: showLogo })
        await ViewPremiumService(this.$client).update(this.view.id, {
          show_logo: showLogo,
        })
      } catch (error) {
        // In case it didn't we will roll back the change.
        this.$emit('update-view', { ...this.view, show_logo: !showLogo })
        notifyIf(error, 'view')
      }
    },
    click() {
      if (!this.hasPremiumFeatures) {
        this.$refs.premiumModal.show()
      }
    },
  },
}
</script>
