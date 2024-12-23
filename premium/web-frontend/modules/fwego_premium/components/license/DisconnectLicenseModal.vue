<template>
  <Modal>
    <h2 class="box__title">
      {{ $t('disconnectLicenseModal.disconnectLicense') }}
    </h2>
    <Error :error="error"></Error>
    <div>
      <i18n path="disconnectLicenseModal.disconnectDescription" tag="p">
        <template #contact>
          <a href="https://fwego.io/contact" target="_blank"
            >fwego.io/contact</a
          >
        </template>
      </i18n>
      <div class="actions">
        <div class="align-right">
          <Button
            type="danger"
            size="large"
            :disabled="loading"
            :loading="loading"
            @click="disconnectLicense()"
          >
            {{ $t('disconnectLicenseModal.disconnectLicense') }}</Button
          >
        </div>
      </div>
    </div>
  </Modal>
</template>

<script>
import modal from '@fwego/modules/core/mixins/modal'
import error from '@fwego/modules/core/mixins/error'
import LicenseService from '@fwego_premium/services/license'

export default {
  name: 'DisconnectLicenseModal',
  mixins: [modal, error],
  props: {
    license: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      loading: false,
    }
  },
  methods: {
    async disconnectLicense() {
      this.hideError()
      this.loading = true

      try {
        await LicenseService(this.$client).disconnect(this.license.id)
        await this.$nuxt.$router.push({ name: 'admin-licenses' })
      } catch (error) {
        this.handleError(error)
      }

      this.loading = false
    },
  },
}
</script>
