import { DatabaseApplicationType } from '@fwego/modules/database/applicationTypes'
import { DuplicateTableJobType } from '@fwego/modules/database/jobTypes'
import {
  GridViewType,
  GalleryViewType,
  FormViewType,
} from '@fwego/modules/database/viewTypes'
import {
  TextFieldType,
  LongTextFieldType,
  URLFieldType,
  EmailFieldType,
  LinkRowFieldType,
  NumberFieldType,
  RatingFieldType,
  BooleanFieldType,
  DateFieldType,
  LastModifiedFieldType,
  LastModifiedByFieldType,
  FileFieldType,
  SingleSelectFieldType,
  MultipleSelectFieldType,
  PhoneNumberFieldType,
  CreatedOnFieldType,
  CreatedByFieldType,
  DurationFieldType,
  FormulaFieldType,
  CountFieldType,
  RollupFieldType,
  LookupFieldType,
  MultipleCollaboratorsFieldType,
  UUIDFieldType,
  AutonumberFieldType,
  PasswordFieldType,
} from '@fwego/modules/database/fieldTypes'
import {
  EqualViewFilterType,
  NotEqualViewFilterType,
  ContainsViewFilterType,
  FilenameContainsViewFilterType,
  FilesLowerThanViewFilterType,
  HasFileTypeViewFilterType,
  ContainsNotViewFilterType,
  LengthIsLowerThanViewFilterType,
  HigherThanViewFilterType,
  HigherThanOrEqualViewFilterType,
  LowerThanViewFilterType,
  LowerThanOrEqualViewFilterType,
  IsEvenAndWholeViewFilterType,
  SingleSelectEqualViewFilterType,
  SingleSelectNotEqualViewFilterType,
  SingleSelectIsAnyOfViewFilterType,
  SingleSelectIsNoneOfViewFilterType,
  BooleanViewFilterType,
  EmptyViewFilterType,
  NotEmptyViewFilterType,
  LinkRowHasFilterType,
  LinkRowHasNotFilterType,
  MultipleSelectHasFilterType,
  MultipleSelectHasNotFilterType,
  MultipleCollaboratorsHasFilterType,
  MultipleCollaboratorsHasNotFilterType,
  LinkRowContainsFilterType,
  LinkRowNotContainsFilterType,
  ContainsWordViewFilterType,
  DoesntContainWordViewFilterType,
  UserIsFilterType,
  UserIsNotFilterType,
  DateIsEqualMultiStepViewFilterType,
  DateIsBeforeMultiStepViewFilterType,
  DateIsOnOrBeforeMultiStepViewFilterType,
  DateIsAfterMultiStepViewFilterType,
  DateIsOnOrAfterMultiStepViewFilterType,
  DateIsWithinMultiStepViewFilterType,
  DateIsNotEqualMultiStepViewFilterType,
  // Deprecated date filter types
  DateEqualViewFilterType,
  DateNotEqualViewFilterType,
  DateEqualsTodayViewFilterType,
  DateBeforeTodayViewFilterType,
  DateAfterTodayViewFilterType,
  DateWithinDaysViewFilterType,
  DateWithinWeeksViewFilterType,
  DateWithinMonthsViewFilterType,
  DateEqualsDaysAgoViewFilterType,
  DateEqualsMonthsAgoViewFilterType,
  DateEqualsYearsAgoViewFilterType,
  DateEqualsCurrentWeekViewFilterType,
  DateEqualsCurrentMonthViewFilterType,
  DateEqualsCurrentYearViewFilterType,
  DateBeforeViewFilterType,
  DateBeforeOrEqualViewFilterType,
  DateAfterDaysAgoViewFilterType,
  DateAfterViewFilterType,
  DateAfterOrEqualViewFilterType,
  DateEqualsDayOfMonthViewFilterType,
} from '@fwego/modules/database/viewFilters'
import {
  HasValueEqualViewFilterType,
  HasEmptyValueViewFilterType,
  HasNotEmptyValueViewFilterType,
  HasNotValueEqualViewFilterType,
  HasValueContainsViewFilterType,
  HasNotValueContainsViewFilterType,
  HasValueContainsWordViewFilterType,
  HasNotValueContainsWordViewFilterType,
  HasValueLengthIsLowerThanViewFilterType,
  HasAllValuesEqualViewFilterType,
  HasAnySelectOptionEqualViewFilterType,
  HasNoneSelectOptionEqualViewFilterType,
} from '@fwego/modules/database/arrayViewFilters'
import {
  CSVImporterType,
  PasteImporterType,
  XMLImporterType,
  JSONImporterType,
} from '@fwego/modules/database/importerTypes'
import {
  ICalCalendarDataSyncType,
  PostgreSQLDataSyncType,
} from '@fwego/modules/database/dataSyncTypes'
import {
  RowsCreatedWebhookEventType,
  RowsUpdatedWebhookEventType,
  RowsDeletedWebhookEventType,
  FieldCreatedWebhookEventType,
  FieldUpdatedWebhookEventType,
  FieldDeletedWebhookEventType,
  ViewCreatedWebhookEventType,
  ViewUpdatedWebhookEventType,
  ViewDeletedWebhookEventType,
} from '@fwego/modules/database/webhookEventTypes'
import {
  ImageFilePreview,
  AudioFilePreview,
  VideoFilePreview,
  PDFBrowserFilePreview,
  GoogleDocFilePreview,
} from '@fwego/modules/database/filePreviewTypes'
import { APITokenSettingsType } from '@fwego/modules/database/settingsTypes'

import tableStore from '@fwego/modules/database/store/table'
import viewStore from '@fwego/modules/database/store/view'
import fieldStore from '@fwego/modules/database/store/field'
import gridStore from '@fwego/modules/database/store/view/grid'
import galleryStore from '@fwego/modules/database/store/view/gallery'
import formStore from '@fwego/modules/database/store/view/form'
import rowModal from '@fwego/modules/database/store/rowModal'
import publicStore from '@fwego/modules/database/store/view/public'
import rowModalNavigationStore from '@fwego/modules/database/store/rowModalNavigation'
import rowHistoryStore from '@fwego/modules/database/store/rowHistory'

import { registerRealtimeEvents } from '@fwego/modules/database/realtime'
import { CSVTableExporterType } from '@fwego/modules/database/exporterTypes'
import {
  FwegoAdd,
  FwegoAnd,
  FwegoConcat,
  FwegoDateDiff,
  FwegoDateInterval,
  FwegoDatetimeFormat,
  FwegoDatetimeFormatTz,
  FwegoDay,
  FwegoDivide,
  FwegoEncodeUri,
  FwegoEncodeUriComponent,
  FwegoEqual,
  FwegoHasOption,
  FwegoField,
  FwegoSearch,
  FwegoGreaterThan,
  FwegoGreaterThanOrEqual,
  FwegoIf,
  FwegoIsBlank,
  FwegoIsNull,
  FwegoDurationToSeconds,
  FwegoSecondsToDuration,
  FwegoLessThan,
  FwegoLessThanOrEqual,
  FwegoLower,
  FwegoSplitPart,
  FwegoMinus,
  FwegoMultiply,
  FwegoNot,
  FwegoOr,
  FwegoReplace,
  FwegoRowId,
  FwegoT,
  FwegoNow,
  FwegoToday,
  FwegoToDateTz,
  FwegoToDate,
  FwegoToNumber,
  FwegoToText,
  FwegoUpper,
  FwegoReverse,
  FwegoLength,
  FwegoNotEqual,
  FwegoLookup,
  FwegoSum,
  FwegoAvg,
  FwegoVariancePop,
  FwegoVarianceSample,
  FwegoStddevSample,
  FwegoStddevPop,
  FwegoJoin,
  FwegoCount,
  FwegoMin,
  FwegoMax,
  FwegoEvery,
  FwegoAny,
  FwegoWhenEmpty,
  FwegoSecond,
  FwegoYear,
  FwegoMonth,
  FwegoLeast,
  FwegoGreatest,
  FwegoRegexReplace,
  FwegoLink,
  FwegoTrim,
  FwegoRight,
  FwegoLeft,
  FwegoContains,
  FwegoFilter,
  FwegoTrunc,
  FwegoIsNaN,
  FwegoWhenNaN,
  FwegoEven,
  FwegoOdd,
  FwegoCeil,
  FwegoFloor,
  FwegoAbs,
  FwegoExp,
  FwegoLn,
  FwegoSign,
  FwegoSqrt,
  FwegoRound,
  FwegoLog,
  FwegoPower,
  FwegoMod,
  FwegoButton,
  FwegoGetLinkUrl,
  FwegoGetLinkLabel,
  FwegoIsImage,
  FwegoGetImageHeight,
  FwegoGetImageWidth,
  FwegoGetFileSize,
  FwegoGetFileMimeType,
  FwegoGetFileVisibleName,
  FwegoIndex,
  FwegoGetFileCount,
  FwegoToUrl,
} from '@fwego/modules/database/formula/functions'
import {
  FwegoFormulaArrayType,
  FwegoFormulaBooleanType,
  FwegoFormulaButtonType,
  FwegoFormulaCharType,
  FwegoFormulaLinkType,
  FwegoFormulaDateIntervalType, // Deprecated
  FwegoFormulaDurationType,
  FwegoFormulaDateType,
  FwegoFormulaInvalidType,
  FwegoFormulaNumberType,
  FwegoFormulaSingleSelectType,
  FwegoFormulaMultipleSelectType,
  FwegoFormulaSpecialType,
  FwegoFormulaTextType,
  FwegoFormulaFileType,
  FwegoFormulaURLType,
} from '@fwego/modules/database/formula/formulaTypes'
import {
  EmptyCountViewAggregationType,
  NotEmptyCountViewAggregationType,
  CheckedCountViewAggregationType,
  NotCheckedCountViewAggregationType,
  EmptyPercentageViewAggregationType,
  NotEmptyPercentageViewAggregationType,
  CheckedPercentageViewAggregationType,
  NotCheckedPercentageViewAggregationType,
  UniqueCountViewAggregationType,
  MinViewAggregationType,
  MaxViewAggregationType,
  EarliestDateViewAggregationType,
  LatestDateViewAggregationType,
  SumViewAggregationType,
  AverageViewAggregationType,
  StdDevViewAggregationType,
  VarianceViewAggregationType,
  MedianViewAggregationType,
} from '@fwego/modules/database/viewAggregationTypes'
import { FormViewFormModeType } from '@fwego/modules/database/formViewModeTypes'
import { CollaborativeViewOwnershipType } from '@fwego/modules/database/viewOwnershipTypes'
import { DatabasePlugin } from '@fwego/modules/database/plugins'
import {
  CollaboratorAddedToRowNotificationType,
  FormSubmittedNotificationType,
  UserMentionInRichTextFieldNotificationType,
} from '@fwego/modules/database/notificationTypes'
import { HistoryRowModalSidebarType } from '@fwego/modules/database/rowModalSidebarTypes'
import { FieldsDataProviderType } from '@fwego/modules/database/dataProviderTypes'

import {
  DatabaseOnboardingType,
  DatabaseScratchTrackOnboardingType,
  DatabaseImportOnboardingType,
  DatabaseScratchTrackFieldsOnboardingType,
} from '@fwego/modules/database/onboardingTypes'

import en from '@fwego/modules/database/locales/en.json'
import fr from '@fwego/modules/database/locales/fr.json'
import nl from '@fwego/modules/database/locales/nl.json'
import de from '@fwego/modules/database/locales/de.json'
import es from '@fwego/modules/database/locales/es.json'
import it from '@fwego/modules/database/locales/it.json'
import pl from '@fwego/modules/database/locales/pl.json'
import ko from '@fwego/modules/database/locales/ko.json'
import {
  DatabaseScratchTrackCampaignFieldsOnboardingType,
  DatabaseScratchTrackCustomFieldsOnboardingType,
  DatabaseScratchTrackProjectFieldsOnboardingType,
  DatabaseScratchTrackTaskFieldsOnboardingType,
  DatabaseScratchTrackTeamFieldsOnboardingType,
} from '@fwego/modules/database/databaseScratchTrackFieldsStepType'

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

  store.registerModule('table', tableStore)
  store.registerModule('view', viewStore)
  store.registerModule('field', fieldStore)
  store.registerModule('rowModal', rowModal)
  store.registerModule('rowModalNavigation', rowModalNavigationStore)
  store.registerModule('rowHistory', rowHistoryStore)
  store.registerModule('page/view/grid', gridStore)
  store.registerModule('page/view/gallery', galleryStore)
  store.registerModule('page/view/form', formStore)
  store.registerModule('page/view/public', publicStore)
  store.registerModule('template/view/grid', gridStore)
  store.registerModule('template/view/gallery', galleryStore)
  store.registerModule('template/view/form', formStore)

  app.$registry.registerNamespace('viewDecorator')
  app.$registry.registerNamespace('decoratorValueProvider')

  app.$registry.register('plugin', new DatabasePlugin(context))
  app.$registry.register('application', new DatabaseApplicationType(context))
  app.$registry.register('job', new DuplicateTableJobType(context))
  app.$registry.register('view', new GridViewType(context))
  app.$registry.register('view', new GalleryViewType(context))
  app.$registry.register('view', new FormViewType(context))
  app.$registry.register('viewFilter', new EqualViewFilterType(context))
  app.$registry.register('viewFilter', new NotEqualViewFilterType(context))
  app.$registry.register(
    'viewFilter',
    new DateIsEqualMultiStepViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateIsNotEqualMultiStepViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateIsBeforeMultiStepViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateIsOnOrBeforeMultiStepViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateIsAfterMultiStepViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateIsOnOrAfterMultiStepViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateIsWithinMultiStepViewFilterType(context)
  )
  // DEPRECATED
  app.$registry.register('viewFilter', new DateEqualViewFilterType(context))
  app.$registry.register('viewFilter', new DateNotEqualViewFilterType(context))
  app.$registry.register(
    'viewFilter',
    new DateEqualsTodayViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateBeforeTodayViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateAfterTodayViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateWithinDaysViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateWithinWeeksViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateWithinMonthsViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateEqualsDaysAgoViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateEqualsMonthsAgoViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateEqualsYearsAgoViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateEqualsCurrentWeekViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateEqualsCurrentMonthViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateEqualsCurrentYearViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateEqualsDayOfMonthViewFilterType(context)
  )
  app.$registry.register('viewFilter', new DateBeforeViewFilterType(context))
  app.$registry.register(
    'viewFilter',
    new DateBeforeOrEqualViewFilterType(context)
  )
  app.$registry.register('viewFilter', new DateAfterViewFilterType(context))
  app.$registry.register(
    'viewFilter',
    new DateAfterOrEqualViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new DateAfterDaysAgoViewFilterType(context)
  )
  // END
  app.$registry.register('viewFilter', new HasEmptyValueViewFilterType(context))
  app.$registry.register(
    'viewFilter',
    new HasNotEmptyValueViewFilterType(context)
  )
  app.$registry.register('viewFilter', new HasValueEqualViewFilterType(context))
  app.$registry.register(
    'viewFilter',
    new HasNotValueEqualViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new HasValueContainsViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new HasNotValueContainsViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new HasValueContainsWordViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new HasNotValueContainsWordViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new HasValueLengthIsLowerThanViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',

    new HasAllValuesEqualViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new HasAnySelectOptionEqualViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new HasNoneSelectOptionEqualViewFilterType(context)
  )
  app.$registry.register('viewFilter', new ContainsViewFilterType(context))
  app.$registry.register('viewFilter', new ContainsNotViewFilterType(context))
  app.$registry.register('viewFilter', new ContainsWordViewFilterType(context))
  app.$registry.register(
    'viewFilter',
    new DoesntContainWordViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new FilenameContainsViewFilterType(context)
  )
  app.$registry.register('viewFilter', new HasFileTypeViewFilterType(context))
  app.$registry.register(
    'viewFilter',
    new FilesLowerThanViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new LengthIsLowerThanViewFilterType(context)
  )
  app.$registry.register('viewFilter', new HigherThanViewFilterType(context))
  app.$registry.register(
    'viewFilter',
    new HigherThanOrEqualViewFilterType(context)
  )
  app.$registry.register('viewFilter', new LowerThanViewFilterType(context))
  app.$registry.register(
    'viewFilter',
    new LowerThanOrEqualViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new IsEvenAndWholeViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new SingleSelectEqualViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new SingleSelectNotEqualViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new SingleSelectIsAnyOfViewFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new SingleSelectIsNoneOfViewFilterType(context)
  )

  app.$registry.register('viewFilter', new BooleanViewFilterType(context))
  app.$registry.register('viewFilter', new LinkRowHasFilterType(context))
  app.$registry.register('viewFilter', new LinkRowHasNotFilterType(context))
  app.$registry.register('viewFilter', new LinkRowContainsFilterType(context))
  app.$registry.register(
    'viewFilter',
    new LinkRowNotContainsFilterType(context)
  )
  app.$registry.register('viewFilter', new MultipleSelectHasFilterType(context))
  app.$registry.register(
    'viewFilter',
    new MultipleSelectHasNotFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new MultipleCollaboratorsHasFilterType(context)
  )
  app.$registry.register(
    'viewFilter',
    new MultipleCollaboratorsHasNotFilterType(context)
  )
  app.$registry.register('viewFilter', new EmptyViewFilterType(context))
  app.$registry.register('viewFilter', new NotEmptyViewFilterType(context))
  app.$registry.register('viewFilter', new UserIsFilterType(context))
  app.$registry.register('viewFilter', new UserIsNotFilterType(context))

  app.$registry.register(
    'viewOwnershipType',
    new CollaborativeViewOwnershipType(context)
  )

  app.$registry.register('field', new TextFieldType(context))
  app.$registry.register('field', new LongTextFieldType(context))
  app.$registry.register('field', new LinkRowFieldType(context))
  app.$registry.register('field', new NumberFieldType(context))
  app.$registry.register('field', new RatingFieldType(context))
  app.$registry.register('field', new BooleanFieldType(context))
  app.$registry.register('field', new DateFieldType(context))
  app.$registry.register('field', new LastModifiedFieldType(context))
  app.$registry.register('field', new LastModifiedByFieldType(context))
  app.$registry.register('field', new CreatedOnFieldType(context))
  app.$registry.register('field', new CreatedByFieldType(context))
  app.$registry.register('field', new DurationFieldType(context))
  app.$registry.register('field', new URLFieldType(context))
  app.$registry.register('field', new EmailFieldType(context))
  app.$registry.register('field', new FileFieldType(context))
  app.$registry.register('field', new SingleSelectFieldType(context))
  app.$registry.register('field', new MultipleSelectFieldType(context))
  app.$registry.register('field', new PhoneNumberFieldType(context))
  app.$registry.register('field', new FormulaFieldType(context))
  app.$registry.register('field', new CountFieldType(context))
  app.$registry.register('field', new RollupFieldType(context))
  app.$registry.register('field', new LookupFieldType(context))
  app.$registry.register('field', new MultipleCollaboratorsFieldType(context))
  app.$registry.register('field', new UUIDFieldType(context))
  app.$registry.register('field', new AutonumberFieldType(context))
  app.$registry.register('field', new PasswordFieldType(context))

  app.$registry.register('importer', new CSVImporterType(context))
  app.$registry.register('importer', new PasteImporterType(context))
  app.$registry.register('importer', new XMLImporterType(context))
  app.$registry.register('importer', new JSONImporterType(context))
  app.$registry.register('dataSync', new ICalCalendarDataSyncType(context))
  app.$registry.register('dataSync', new PostgreSQLDataSyncType(context))
  app.$registry.register('settings', new APITokenSettingsType(context))
  app.$registry.register('exporter', new CSVTableExporterType(context))
  app.$registry.register(
    'webhookEvent',
    new RowsCreatedWebhookEventType(context)
  )
  app.$registry.register(
    'webhookEvent',
    new RowsUpdatedWebhookEventType(context)
  )
  app.$registry.register(
    'webhookEvent',
    new RowsDeletedWebhookEventType(context)
  )
  app.$registry.register(
    'webhookEvent',
    new FieldCreatedWebhookEventType(context)
  )
  app.$registry.register(
    'webhookEvent',
    new FieldUpdatedWebhookEventType(context)
  )
  app.$registry.register(
    'webhookEvent',
    new FieldDeletedWebhookEventType(context)
  )
  app.$registry.register(
    'webhookEvent',
    new ViewCreatedWebhookEventType(context)
  )
  app.$registry.register(
    'webhookEvent',
    new ViewUpdatedWebhookEventType(context)
  )
  app.$registry.register(
    'webhookEvent',
    new ViewDeletedWebhookEventType(context)
  )

  // Text functions
  app.$registry.register('formula_function', new FwegoUpper(context))
  app.$registry.register('formula_function', new FwegoLower(context))
  app.$registry.register('formula_function', new FwegoConcat(context))
  app.$registry.register('formula_function', new FwegoToText(context))
  app.$registry.register('formula_function', new FwegoT(context))
  app.$registry.register('formula_function', new FwegoReplace(context))
  app.$registry.register('formula_function', new FwegoSearch(context))
  app.$registry.register('formula_function', new FwegoLength(context))
  app.$registry.register('formula_function', new FwegoReverse(context))
  app.$registry.register('formula_function', new FwegoEncodeUri(context))
  app.$registry.register(
    'formula_function',
    new FwegoEncodeUriComponent(context)
  )
  app.$registry.register('formula_function', new FwegoSplitPart(context))
  // Number functions
  app.$registry.register('formula_function', new FwegoMultiply(context))
  app.$registry.register('formula_function', new FwegoDivide(context))
  app.$registry.register('formula_function', new FwegoToNumber(context))
  // Boolean functions
  app.$registry.register('formula_function', new FwegoIf(context))
  app.$registry.register('formula_function', new FwegoEqual(context))
  app.$registry.register('formula_function', new FwegoHasOption(context))
  app.$registry.register('formula_function', new FwegoIsBlank(context))
  app.$registry.register('formula_function', new FwegoIsNull(context))
  app.$registry.register('formula_function', new FwegoNot(context))
  app.$registry.register('formula_function', new FwegoNotEqual(context))
  app.$registry.register('formula_function', new FwegoGreaterThan(context))
  app.$registry.register(
    'formula_function',
    new FwegoGreaterThanOrEqual(context)
  )
  app.$registry.register('formula_function', new FwegoLessThan(context))
  app.$registry.register(
    'formula_function',
    new FwegoLessThanOrEqual(context)
  )
  app.$registry.register('formula_function', new FwegoAnd(context))
  app.$registry.register('formula_function', new FwegoOr(context))
  // Date functions
  app.$registry.register('formula_function', new FwegoDatetimeFormat(context))
  app.$registry.register(
    'formula_function',
    new FwegoDatetimeFormatTz(context)
  )
  app.$registry.register('formula_function', new FwegoDay(context))
  app.$registry.register('formula_function', new FwegoNow(context))
  app.$registry.register('formula_function', new FwegoToday(context))
  app.$registry.register('formula_function', new FwegoToDateTz(context))
  app.$registry.register('formula_function', new FwegoToDate(context))
  app.$registry.register('formula_function', new FwegoDateDiff(context))
  // Date interval functions
  app.$registry.register('formula_function', new FwegoDateInterval(context))
  app.$registry.register(
    'formula_function',
    new FwegoDurationToSeconds(context)
  )
  app.$registry.register(
    'formula_function',
    new FwegoSecondsToDuration(context)
  )
  // Special functions. NOTE: rollup compatible functions are shown field sub-form in
  // the same order as they are listed here.
  app.$registry.register('formula_function', new FwegoAdd(context))
  app.$registry.register('formula_function', new FwegoMinus(context))
  app.$registry.register('formula_function', new FwegoField(context))
  app.$registry.register('formula_function', new FwegoLookup(context))
  app.$registry.register('formula_function', new FwegoRowId(context))
  app.$registry.register('formula_function', new FwegoContains(context))
  app.$registry.register('formula_function', new FwegoLeft(context))
  app.$registry.register('formula_function', new FwegoRight(context))
  app.$registry.register('formula_function', new FwegoTrim(context))
  app.$registry.register('formula_function', new FwegoRegexReplace(context))
  app.$registry.register('formula_function', new FwegoGreatest(context))
  app.$registry.register('formula_function', new FwegoLeast(context))
  app.$registry.register('formula_function', new FwegoMonth(context))
  app.$registry.register('formula_function', new FwegoYear(context))
  app.$registry.register('formula_function', new FwegoSecond(context))
  app.$registry.register('formula_function', new FwegoWhenEmpty(context))
  app.$registry.register('formula_function', new FwegoAny(context))
  app.$registry.register('formula_function', new FwegoEvery(context))
  app.$registry.register('formula_function', new FwegoMin(context))
  app.$registry.register('formula_function', new FwegoMax(context))
  app.$registry.register('formula_function', new FwegoCount(context))
  app.$registry.register('formula_function', new FwegoSum(context))
  app.$registry.register('formula_function', new FwegoAvg(context))
  app.$registry.register('formula_function', new FwegoJoin(context))
  app.$registry.register('formula_function', new FwegoStddevPop(context))
  app.$registry.register('formula_function', new FwegoStddevSample(context))
  app.$registry.register('formula_function', new FwegoVarianceSample(context))
  app.$registry.register('formula_function', new FwegoVariancePop(context))
  app.$registry.register('formula_function', new FwegoFilter(context))
  app.$registry.register('formula_function', new FwegoTrunc(context))
  app.$registry.register('formula_function', new FwegoIsNaN(context))
  app.$registry.register('formula_function', new FwegoWhenNaN(context))
  app.$registry.register('formula_function', new FwegoEven(context))
  app.$registry.register('formula_function', new FwegoOdd(context))
  app.$registry.register('formula_function', new FwegoAbs(context))
  app.$registry.register('formula_function', new FwegoCeil(context))
  app.$registry.register('formula_function', new FwegoFloor(context))
  app.$registry.register('formula_function', new FwegoSign(context))
  app.$registry.register('formula_function', new FwegoLog(context))
  app.$registry.register('formula_function', new FwegoExp(context))
  app.$registry.register('formula_function', new FwegoLn(context))
  app.$registry.register('formula_function', new FwegoPower(context))
  app.$registry.register('formula_function', new FwegoSqrt(context))
  app.$registry.register('formula_function', new FwegoRound(context))
  app.$registry.register('formula_function', new FwegoMod(context))
  // Link functions
  app.$registry.register('formula_function', new FwegoLink(context))
  app.$registry.register('formula_function', new FwegoButton(context))
  app.$registry.register('formula_function', new FwegoGetLinkUrl(context))
  app.$registry.register('formula_function', new FwegoGetLinkLabel(context))
  // File functions
  app.$registry.register(
    'formula_function',
    new FwegoGetFileVisibleName(context)
  )
  app.$registry.register(
    'formula_function',
    new FwegoGetFileMimeType(context)
  )
  app.$registry.register('formula_function', new FwegoGetFileSize(context))
  app.$registry.register('formula_function', new FwegoGetImageWidth(context))
  app.$registry.register('formula_function', new FwegoGetImageHeight(context))
  app.$registry.register('formula_function', new FwegoIsImage(context))

  app.$registry.register('formula_function', new FwegoGetFileCount(context))
  app.$registry.register('formula_function', new FwegoIndex(context))
  app.$registry.register('formula_function', new FwegoToUrl(context))

  // Formula Types
  app.$registry.register('formula_type', new FwegoFormulaTextType(context))
  app.$registry.register('formula_type', new FwegoFormulaCharType(context))
  app.$registry.register('formula_type', new FwegoFormulaBooleanType(context))
  app.$registry.register('formula_type', new FwegoFormulaDateType(context))
  app.$registry.register(
    'formula_type',
    new FwegoFormulaDateIntervalType(context)
  )
  app.$registry.register(
    'formula_type',
    new FwegoFormulaDurationType(context)
  )
  app.$registry.register('formula_type', new FwegoFormulaNumberType(context))
  app.$registry.register('formula_type', new FwegoFormulaArrayType(context))
  app.$registry.register('formula_type', new FwegoFormulaSpecialType(context))
  app.$registry.register('formula_type', new FwegoFormulaInvalidType(context))
  app.$registry.register(
    'formula_type',
    new FwegoFormulaSingleSelectType(context)
  )
  app.$registry.register('formula_type', new FwegoFormulaURLType(context))
  app.$registry.register(
    'formula_type',
    new FwegoFormulaMultipleSelectType(context)
  )
  app.$registry.register('formula_type', new FwegoFormulaButtonType(context))
  app.$registry.register('formula_type', new FwegoFormulaLinkType(context))
  app.$registry.register('formula_type', new FwegoFormulaFileType(context))

  // File preview types
  app.$registry.register('preview', new ImageFilePreview(context))
  app.$registry.register('preview', new AudioFilePreview(context))
  app.$registry.register('preview', new VideoFilePreview(context))
  app.$registry.register('preview', new PDFBrowserFilePreview(context))
  app.$registry.register('preview', new GoogleDocFilePreview(context))

  app.$registry.register('viewAggregation', new MinViewAggregationType(context))
  app.$registry.register('viewAggregation', new MaxViewAggregationType(context))
  app.$registry.register('viewAggregation', new SumViewAggregationType(context))
  app.$registry.register(
    'viewAggregation',
    new AverageViewAggregationType(context)
  )
  app.$registry.register(
    'viewAggregation',
    new MedianViewAggregationType(context)
  )
  app.$registry.register(
    'viewAggregation',
    new StdDevViewAggregationType(context)
  )
  app.$registry.register(
    'viewAggregation',
    new VarianceViewAggregationType(context)
  )
  app.$registry.register(
    'viewAggregation',
    new EarliestDateViewAggregationType(context)
  )
  app.$registry.register(
    'viewAggregation',
    new LatestDateViewAggregationType(context)
  )
  app.$registry.register(
    'viewAggregation',
    new EmptyCountViewAggregationType(context)
  )
  app.$registry.register(
    'viewAggregation',
    new NotEmptyCountViewAggregationType(context)
  )
  app.$registry.register(
    'viewAggregation',
    new CheckedCountViewAggregationType(context)
  )
  app.$registry.register(
    'viewAggregation',
    new NotCheckedCountViewAggregationType(context)
  )
  app.$registry.register(
    'viewAggregation',
    new EmptyPercentageViewAggregationType(context)
  )
  app.$registry.register(
    'viewAggregation',
    new NotEmptyPercentageViewAggregationType(context)
  )
  app.$registry.register(
    'viewAggregation',
    new CheckedPercentageViewAggregationType(context)
  )
  app.$registry.register(
    'viewAggregation',
    new NotCheckedPercentageViewAggregationType(context)
  )
  app.$registry.register(
    'viewAggregation',
    new UniqueCountViewAggregationType(context)
  )

  app.$registry.register('formViewMode', new FormViewFormModeType(context))

  app.$registry.register(
    'databaseDataProvider',
    new FieldsDataProviderType(context)
  )

  // notifications
  app.$registry.register(
    'notification',
    new CollaboratorAddedToRowNotificationType(context)
  )
  app.$registry.register(
    'notification',
    new FormSubmittedNotificationType(context)
  )
  app.$registry.register(
    'notification',
    new UserMentionInRichTextFieldNotificationType(context)
  )

  app.$registry.register(
    'rowModalSidebar',
    new HistoryRowModalSidebarType(context)
  )

  app.$registry.register('onboarding', new DatabaseOnboardingType(context))
  app.$registry.register(
    'onboarding',
    new DatabaseScratchTrackOnboardingType(context)
  )
  app.$registry.register(
    'onboarding',
    new DatabaseScratchTrackFieldsOnboardingType(context)
  )
  app.$registry.register(
    'onboarding',
    new DatabaseImportOnboardingType(context)
  )

  app.$registry.register(
    'onboardingTrackFields',
    new DatabaseScratchTrackProjectFieldsOnboardingType(context)
  )
  app.$registry.register(
    'onboardingTrackFields',
    new DatabaseScratchTrackTeamFieldsOnboardingType(context)
  )
  app.$registry.register(
    'onboardingTrackFields',
    new DatabaseScratchTrackTaskFieldsOnboardingType(context)
  )
  app.$registry.register(
    'onboardingTrackFields',
    new DatabaseScratchTrackCampaignFieldsOnboardingType(context)
  )
  app.$registry.register(
    'onboardingTrackFields',
    new DatabaseScratchTrackCustomFieldsOnboardingType(context)
  )

  registerRealtimeEvents(app.$realtime)
}
