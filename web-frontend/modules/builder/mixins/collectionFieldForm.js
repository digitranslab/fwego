import applicationContextMixin from '@fwego/modules/builder/mixins/applicationContext'
import elementForm from '@fwego/modules/builder/mixins/elementForm'

export default {
  mixins: [elementForm, applicationContextMixin],
  props: {
    element: {
      type: Object,
      required: true,
    },
    baseTheme: {
      type: Object,
      required: true,
    },
  },
}
