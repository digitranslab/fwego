import en from '@fwego/modules/builder/locales/en.json'
import fr from '@fwego/modules/builder/locales/fr.json'
import nl from '@fwego/modules/builder/locales/nl.json'
import de from '@fwego/modules/builder/locales/de.json'
import es from '@fwego/modules/builder/locales/es.json'
import it from '@fwego/modules/builder/locales/it.json'
import pl from '@fwego/modules/builder/locales/pl.json'
import ko from '@fwego/modules/builder/locales/ko.json'
import {
  GeneralBuilderSettingsType,
  DomainsBuilderSettingsType,
  IntegrationsBuilderSettingsType,
  ThemeBuilderSettingsType,
  UserSourcesBuilderSettingsType,
} from '@fwego/modules/builder/builderSettingTypes'

import pageStore from '@fwego/modules/builder/store/page'
import elementStore from '@fwego/modules/builder/store/element'
import domainStore from '@fwego/modules/builder/store/domain'
import publicBuilderStore from '@fwego/modules/builder/store/publicBuilder'
import dataSourceStore from '@fwego/modules/builder/store/dataSource'
import pageParameterStore from '@fwego/modules/builder/store/pageParameter'
import dataSourceContentStore from '@fwego/modules/builder/store/dataSourceContent'
import elementContentStore from '@fwego/modules/builder/store/elementContent'
import themeStore from '@fwego/modules/builder/store/theme'
import workflowActionStore from '@fwego/modules/builder/store/workflowAction'
import formDataStore from '@fwego/modules/builder/store/formData'

import { registerRealtimeEvents } from '@fwego/modules/builder/realtime'
import {
  HeadingElementType,
  ImageElementType,
  TextElementType,
  LinkElementType,
  InputTextElementType,
  ColumnElementType,
  ButtonElementType,
  TableElementType,
  FormContainerElementType,
  ChoiceElementType,
  CheckboxElementType,
  DateTimePickerElementType,
  IFrameElementType,
  RepeatElementType,
  RecordSelectorElementType,
  HeaderElementType,
  FooterElementType,
} from '@fwego/modules/builder/elementTypes'
import {
  DesktopDeviceType,
  SmartphoneDeviceType,
  TabletDeviceType,
} from '@fwego/modules/builder/deviceTypes'
import { DuplicatePageJobType } from '@fwego/modules/builder/jobTypes'
import { BuilderApplicationType } from '@fwego/modules/builder/applicationTypes'
import { PublicSiteErrorPageType } from '@fwego/modules/builder/errorPageTypes'
import {
  DataSourcesPageHeaderItemType,
  ElementsPageHeaderItemType,
  SettingsPageHeaderItemType,
} from '@fwego/modules/builder/pageHeaderItemTypes'
import {
  EventsPageSidePanelType,
  GeneralPageSidePanelType,
  StylePageSidePanelType,
  VisibilityPageSidePanelType,
} from '@fwego/modules/builder/pageSidePanelTypes'
import {
  CustomDomainType,
  SubDomainType,
} from '@fwego/modules/builder/domainTypes'
import {
  PagePageSettingsType,
  PageVisibilitySettingsType,
} from '@fwego/modules/builder/pageSettingsTypes'
import {
  TextPathParamType,
  NumericPathParamType,
} from '@fwego/modules/builder/pathParamTypes'

import {
  PreviewPageActionType,
  PublishPageActionType,
} from '@fwego/modules/builder/pageActionTypes'

import {
  PageParameterDataProviderType,
  DataSourceDataProviderType,
  CurrentRecordDataProviderType,
  FormDataProviderType,
  PreviousActionDataProviderType,
  UserDataProviderType,
  DataSourceContextDataProviderType,
} from '@fwego/modules/builder/dataProviderTypes'

import {
  ColorThemeConfigBlockType,
  TypographyThemeConfigBlockType,
  ButtonThemeConfigBlockType,
  LinkThemeConfigBlockType,
  ImageThemeConfigBlockType,
  PageThemeConfigBlockType,
  InputThemeConfigBlockType,
  TableThemeConfigBlockType,
} from '@fwego/modules/builder/themeConfigBlockTypes'
import {
  CreateRowWorkflowActionType,
  NotificationWorkflowActionType,
  OpenPageWorkflowActionType,
  UpdateRowWorkflowActionType,
  LogoutWorkflowActionType,
  RefreshDataSourceWorkflowActionType,
  DeleteRowWorkflowActionType,
} from '@fwego/modules/builder/workflowActionTypes'

import {
  BooleanCollectionFieldType,
  TextCollectionFieldType,
  LinkCollectionFieldType,
  ButtonCollectionFieldType,
  TagsCollectionFieldType,
  ImageCollectionFieldType,
} from '@fwego/modules/builder/collectionFieldTypes'

import {
  InterFontFamilyType,
  ArialFontFamilyType,
  VerdanaFontFamilyType,
  TahomaFontFamilyType,
  TrebuchetMSFontFamilyType,
  TimesNewRomanFontFamilyType,
  GeorgiaFontFamilyType,
  GaramondFontFamilyType,
  CourierNewFontFamilyType,
  BrushScriptMTFontFamilyType,
} from '@fwego/modules/builder/fontFamilyTypes'

export default (context) => {
  const { store, app, isDev } = context

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

  registerRealtimeEvents(app.$realtime)

  store.registerModule('page', pageStore)
  store.registerModule('element', elementStore)
  store.registerModule('domain', domainStore)
  store.registerModule('publicBuilder', publicBuilderStore)
  store.registerModule('dataSource', dataSourceStore)
  store.registerModule('pageParameter', pageParameterStore)
  store.registerModule('dataSourceContent', dataSourceContentStore)
  store.registerModule('elementContent', elementContentStore)
  store.registerModule('theme', themeStore)
  store.registerModule('workflowAction', workflowActionStore)
  store.registerModule('formData', formDataStore)

  app.$registry.registerNamespace('builderSettings')
  app.$registry.registerNamespace('element')
  app.$registry.registerNamespace('device')
  app.$registry.registerNamespace('pageHeaderItem')
  app.$registry.registerNamespace('domain')
  app.$registry.registerNamespace('pageSettings')
  app.$registry.registerNamespace('pathParamType')
  app.$registry.registerNamespace('builderDataProvider')
  app.$registry.registerNamespace('themeConfigBlock')
  app.$registry.registerNamespace('fontFamily')

  app.$registry.register('application', new BuilderApplicationType(context))
  app.$registry.register('job', new DuplicatePageJobType(context))

  app.$registry.register(
    'builderSettings',
    new GeneralBuilderSettingsType(context)
  )
  app.$registry.register(
    'builderSettings',
    new IntegrationsBuilderSettingsType(context)
  )
  app.$registry.register(
    'builderSettings',
    new ThemeBuilderSettingsType(context)
  )
  app.$registry.register(
    'builderSettings',
    new DomainsBuilderSettingsType(context)
  )

  app.$registry.register(
    'builderSettings',
    new UserSourcesBuilderSettingsType(context)
  )

  app.$registry.register('errorPage', new PublicSiteErrorPageType(context))

  app.$registry.register('element', new HeadingElementType(context))
  app.$registry.register('element', new TextElementType(context))
  app.$registry.register('element', new ImageElementType(context))
  app.$registry.register('element', new IFrameElementType(context))
  app.$registry.register('element', new LinkElementType(context))
  app.$registry.register('element', new ButtonElementType(context))
  app.$registry.register('element', new TableElementType(context))
  app.$registry.register('element', new ColumnElementType(context))
  app.$registry.register('element', new HeaderElementType(context))
  app.$registry.register('element', new FooterElementType(context))
  app.$registry.register('element', new FormContainerElementType(context))
  app.$registry.register('element', new InputTextElementType(context))
  app.$registry.register('element', new ChoiceElementType(context))
  app.$registry.register('element', new CheckboxElementType(context))
  app.$registry.register('element', new DateTimePickerElementType(context))
  app.$registry.register('element', new RecordSelectorElementType(context))
  app.$registry.register('element', new RepeatElementType(context))

  app.$registry.register('device', new DesktopDeviceType(context))
  app.$registry.register('device', new TabletDeviceType(context))
  app.$registry.register('device', new SmartphoneDeviceType(context))

  app.$registry.register(
    'pageHeaderItem',
    new ElementsPageHeaderItemType(context)
  )
  app.$registry.register(
    'pageHeaderItem',
    new DataSourcesPageHeaderItemType(context)
  )
  app.$registry.register(
    'pageHeaderItem',
    new SettingsPageHeaderItemType(context)
  )
  app.$registry.register('pageSidePanel', new GeneralPageSidePanelType(context))
  app.$registry.register('pageSidePanel', new StylePageSidePanelType(context))
  app.$registry.register(
    'pageSidePanel',
    new VisibilityPageSidePanelType(context)
  )
  app.$registry.register('pageSidePanel', new EventsPageSidePanelType(context))

  app.$registry.register('domain', new CustomDomainType(context))
  app.$registry.register('domain', new SubDomainType(context))

  app.$registry.register('pageSettings', new PagePageSettingsType(context))
  app.$registry.register(
    'pageSettings',
    new PageVisibilitySettingsType(context)
  )

  app.$registry.register('pathParamType', new TextPathParamType(context))
  app.$registry.register('pathParamType', new NumericPathParamType(context))

  app.$registry.register('pageAction', new PublishPageActionType(context))
  app.$registry.register('pageAction', new PreviewPageActionType(context))

  app.$registry.register(
    'builderDataProvider',
    new UserDataProviderType(context)
  )
  app.$registry.register(
    'builderDataProvider',
    new CurrentRecordDataProviderType(context)
  )
  app.$registry.register(
    'builderDataProvider',
    new DataSourceDataProviderType(context)
  )
  app.$registry.register(
    'builderDataProvider',
    new DataSourceContextDataProviderType(context)
  )
  app.$registry.register(
    'builderDataProvider',
    new PageParameterDataProviderType(context)
  )
  app.$registry.register(
    'builderDataProvider',
    new FormDataProviderType(context)
  )
  app.$registry.register(
    'builderDataProvider',
    new PreviousActionDataProviderType(context)
  )
  app.$registry.register(
    'themeConfigBlock',
    new ColorThemeConfigBlockType(context)
  )
  app.$registry.register(
    'themeConfigBlock',
    new TypographyThemeConfigBlockType(context)
  )
  app.$registry.register(
    'themeConfigBlock',
    new ButtonThemeConfigBlockType(context)
  )
  app.$registry.register(
    'themeConfigBlock',
    new LinkThemeConfigBlockType(context)
  )
  app.$registry.register(
    'themeConfigBlock',
    new ImageThemeConfigBlockType(context)
  )
  app.$registry.register(
    'themeConfigBlock',
    new PageThemeConfigBlockType(context)
  )
  app.$registry.register(
    'themeConfigBlock',
    new InputThemeConfigBlockType(context)
  )
  app.$registry.register(
    'themeConfigBlock',
    new TableThemeConfigBlockType(context)
  )

  app.$registry.register(
    'workflowAction',
    new NotificationWorkflowActionType(context)
  )
  app.$registry.register(
    'workflowAction',
    new OpenPageWorkflowActionType(context)
  )
  app.$registry.register(
    'workflowAction',
    new LogoutWorkflowActionType(context)
  )
  app.$registry.register(
    'workflowAction',
    new RefreshDataSourceWorkflowActionType(context)
  )
  app.$registry.register(
    'workflowAction',
    new CreateRowWorkflowActionType(context)
  )
  app.$registry.register(
    'workflowAction',
    new UpdateRowWorkflowActionType(context)
  )
  app.$registry.register(
    'workflowAction',
    new DeleteRowWorkflowActionType(context)
  )

  app.$registry.register(
    'collectionField',
    new BooleanCollectionFieldType(context)
  )
  app.$registry.register(
    'collectionField',
    new TextCollectionFieldType(context)
  )
  app.$registry.register(
    'collectionField',
    new LinkCollectionFieldType(context)
  )
  app.$registry.register(
    'collectionField',
    new TagsCollectionFieldType(context)
  )
  app.$registry.register(
    'collectionField',
    new ButtonCollectionFieldType(context)
  )
  app.$registry.register(
    'collectionField',
    new ImageCollectionFieldType(context)
  )

  app.$registry.register('fontFamily', new InterFontFamilyType(context))
  app.$registry.register('fontFamily', new ArialFontFamilyType(context))
  app.$registry.register('fontFamily', new VerdanaFontFamilyType(context))
  app.$registry.register('fontFamily', new TahomaFontFamilyType(context))
  app.$registry.register('fontFamily', new TrebuchetMSFontFamilyType(context))
  app.$registry.register('fontFamily', new TimesNewRomanFontFamilyType(context))
  app.$registry.register('fontFamily', new GeorgiaFontFamilyType(context))
  app.$registry.register('fontFamily', new GaramondFontFamilyType(context))
  app.$registry.register('fontFamily', new CourierNewFontFamilyType(context))
  app.$registry.register('fontFamily', new BrushScriptMTFontFamilyType(context))
}
