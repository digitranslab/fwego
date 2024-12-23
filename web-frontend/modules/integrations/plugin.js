import en from '@fwego/modules/integrations/locales/en.json'
import fr from '@fwego/modules/integrations/locales/fr.json'
import nl from '@fwego/modules/integrations/locales/nl.json'
import de from '@fwego/modules/integrations/locales/de.json'
import es from '@fwego/modules/integrations/locales/es.json'
import it from '@fwego/modules/integrations/locales/it.json'
import pl from '@fwego/modules/integrations/locales/pl.json'
import ko from '@fwego/modules/integrations/locales/ko.json'

import { LocalFwegoIntegrationType } from '@fwego/modules/integrations/integrationTypes'
import {
  LocalFwegoGetRowServiceType,
  LocalFwegoListRowsServiceType,
  LocalFwegoAggregateRowsServiceType,
} from '@fwego/modules/integrations/serviceTypes'

export default (context) => {
  const { app, isDev } = context

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

  app.$registry.register(
    'integration',
    new LocalFwegoIntegrationType(context)
  )

  app.$registry.register('service', new LocalFwegoGetRowServiceType(context))
  app.$registry.register(
    'service',
    new LocalFwegoListRowsServiceType(context)
  )
  app.$registry.register(
    'service',
    new LocalFwegoAggregateRowsServiceType(context)
  )
}
