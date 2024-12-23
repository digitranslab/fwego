import { TableExporterType } from '@fwego/modules/database/exporterTypes'
import { GridViewType } from '@fwego/modules/database/viewTypes'
import TableJSONExporter from '@fwego_premium/components/exporter/TableJSONExporter'
import TableXMLExporter from '@fwego_premium/components/exporter/TableXMLExporter'
import PremiumModal from '@fwego_premium/components/PremiumModal'
import PremiumFeatures from '@fwego_premium/features'
import TableExcelExporter from '@fwego_premium/components/exporter/TableExcelExporter'

class PremiumTableExporterType extends TableExporterType {
  getDeactivatedText() {
    return this.app.i18n.t('premium.deactivated')
  }

  getDeactivatedClickModal() {
    return PremiumModal
  }

  isDeactivated(workspaceId) {
    return !this.app.$hasFeature(PremiumFeatures.PREMIUM, workspaceId)
  }
}

export class JSONTableExporter extends PremiumTableExporterType {
  static getType() {
    return 'json'
  }

  getIconClass() {
    return 'fwego-icon-file-code'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('premium.exporterType.json')
  }

  getFormComponent() {
    return TableJSONExporter
  }

  getCanExportTable() {
    return true
  }

  getSupportedViews() {
    return [GridViewType.getType()]
  }
}

export class XMLTableExporter extends PremiumTableExporterType {
  static getType() {
    return 'xml'
  }

  getIconClass() {
    return 'fwego-icon-file-code'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('premium.exporterType.xml')
  }

  getFormComponent() {
    return TableXMLExporter
  }

  getCanExportTable() {
    return true
  }

  getSupportedViews() {
    return [GridViewType.getType()]
  }
}

export class ExcelTableExporterType extends PremiumTableExporterType {
  static getType() {
    return 'excel'
  }

  getFileExtension() {
    return 'xlsx'
  }

  getIconClass() {
    return 'fwego-icon-file-excel'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('premium.exporterType.excel')
  }

  getFormComponent() {
    return TableExcelExporter
  }

  getCanExportTable() {
    return true
  }

  getSupportedViews() {
    return [GridViewType.getType()]
  }
}
