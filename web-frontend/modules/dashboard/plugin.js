import en from '@fwego/modules/dashboard/locales/en.json'
import fr from '@fwego/modules/dashboard/locales/fr.json'
import nl from '@fwego/modules/dashboard/locales/nl.json'
import de from '@fwego/modules/dashboard/locales/de.json'
import es from '@fwego/modules/dashboard/locales/es.json'
import it from '@fwego/modules/dashboard/locales/it.json'
import pl from '@fwego/modules/dashboard/locales/pl.json'
import ko from '@fwego/modules/dashboard/locales/ko.json'

import { DashboardApplicationType } from '@fwego/modules/dashboard/applicationTypes'
import dashboardApplicationStore from '@fwego/modules/dashboard/store/dashboardApplication'
import { FF_DASHBOARDS } from '@fwego/modules/core/plugins/featureFlags'

export default (context) => {
  const { app, isDev, store } = context

  // Allow locale file hot reloading in dev
  if (isDev && app.i18n) {
    const { i18n } = app
    i18n.mergeLocaleMessage('en', en)
    i18n.mergeLocaleMessage('fr', fr)
    i18n.mergeLocaleMessage('nl', nl)
    i18n.mergeLocaleMessage('de', de)
    i18n.mergeLocaleMessage('es', es)
    i18n.mergeLocaleMessage('it', it)
    i18n.mergeLocaleMessage('pl', pl)
    i18n.mergeLocaleMessage('ko', ko)
  }

  store.registerModule('dashboardApplication', dashboardApplicationStore)

  if (app.$featureFlagIsEnabled(FF_DASHBOARDS)) {
    app.$registry.register('application', new DashboardApplicationType(context))
  }
}
