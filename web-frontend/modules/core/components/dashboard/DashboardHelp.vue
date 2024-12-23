<template>
  <Alert
    v-if="displayAlert"
    type="blank"
    close-button
    position="bottom"
    :width="396"
    @close="handleAlertClose"
  >
    <template #image
      ><img
        src="@fwego/modules/core/assets/images/dashboard_alert_image.png"
        srcset="
          @fwego/modules/core/assets/images/dashboard_alert_image@2x.png 2x
        "
      />
    </template>
    <template #title
      ><h4>{{ $t('dashboard.alertTitle') }}</h4></template
    >
    <p>{{ $t('dashboard.alertText') }}</p>
    <template #actions>
      <Button
        tag="a"
        href="https://github.com/digitranslab/fwego"
        target="_blank"
        rel="noopener noreferrer"
        type="secondary"
        icon="fwego-icon-gitlab"
      >
        {{ $t('dashboard.starOnGitlab') }}</Button
      >
      <ButtonIcon
        v-tooltip="$t('dashboard.shareOnTwitter')"
        tag="a"
        tooltip-position="top"
        :href="`https://twitter.com/intent/tweet?url=https://fwego.io&hashtags=opensource,nocode,database,fwego&text=${encodeURI(
          $t('dashboard.tweetContent')
        )}`"
        target="_blank"
        rel="noopener noreferrer"
        icon="fwego-icon-twitter"
      ></ButtonIcon>
      <ButtonIcon
        v-tooltip="$t('dashboard.shareOnReddit')"
        tag="a"
        tooltip-position="top"
        icon="fwego-icon-reddit"
        :href="
          'https://www.reddit.com/submit?url=https://fwego.io&title=' +
          encodeURI($t('dashboard.redditTitle'))
        "
        target="_blank"
        rel="noopener noreferrer"
      ></ButtonIcon>
      <ButtonIcon
        v-tooltip="$t('dashboard.shareOnFacebook')"
        tag="a"
        tooltip-position="top"
        icon="fwego-icon-facebook"
        href="https://www.facebook.com/sharer/sharer.php?u=https://fwego.io"
        target="_blank"
        rel="noopener noreferrer"
      ></ButtonIcon>
      <ButtonIcon
        v-tooltip="$t('dashboard.shareOnLinkedIn')"
        tag="a"
        tooltip-position="top"
        icon="fwego-icon-linkedin"
        href="https://www.linkedin.com/sharing/share-offsite/?url=https://fwego.io"
        target="_blank"
        rel="noopener noreferrer"
      ></ButtonIcon>
    </template>
  </Alert>
</template>

<script>
const helpDisplayCookieName = 'fwego_dashboard_alert_closed'

export default {
  name: 'DashboardHelp',
  data() {
    return {
      showAlert: true,
    }
  },
  computed: {
    displayAlert() {
      return this.showAlert && !this.$cookies.get(helpDisplayCookieName)
    },
  },
  methods: {
    handleAlertClose() {
      this.showAlert = false
      this.$cookies.set(helpDisplayCookieName, true, {
        path: '/',
        maxAge: 60 * 60 * 24 * 182, // 6 months
      })
    },
  },
}
</script>
