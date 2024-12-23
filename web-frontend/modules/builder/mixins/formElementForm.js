import elementForm from '@fwego/modules/builder/mixins/elementForm'
import { DATA_PROVIDERS_ALLOWED_FORM_ELEMENTS } from '@fwego/modules/builder/enums'

export default {
  inject: ['workspace', 'builder', 'currentPage', 'elementPage', 'mode'],
  mixins: [elementForm],
  provide() {
    return {
      dataProvidersAllowed: DATA_PROVIDERS_ALLOWED_FORM_ELEMENTS,
    }
  },
}
