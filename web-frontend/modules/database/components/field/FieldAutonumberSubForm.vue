<script>
import form from '@fwego/modules/core/mixins/form'
import fieldSubForm from '@fwego/modules/database/mixins/fieldSubForm'

export default {
  name: 'FieldAutonumberSubForm',
  mixins: [form, fieldSubForm],
  data() {
    return {
      allowedValues: ['view_id'],
      values: { view_id: null },
    }
  },
  methods: {
    getDefaultValues() {
      return {
        view_id: this.view.id,
      }
    },
  },
  validations: {},
}
</script>
