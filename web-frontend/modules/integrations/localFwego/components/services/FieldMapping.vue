<template>
  <FormGroup required class="margin-bottom-2">
    <InjectedFormulaInput
      v-model="fieldValue"
      :disabled="!fieldMapping.enabled"
      v-bind="$attrs"
    />
    <template #after-input>
      <div ref="editFieldMappingOpener">
        <ButtonIcon
          type="secondary"
          icon="iconoir-more-vert"
          @click="openContext"
        />
      </div>
      <FieldMappingContext
        ref="fieldMappingContext"
        :field-mapping="fieldMapping"
        @edit="$emit('change', $event)"
      />
    </template>
  </FormGroup>
</template>

<script>
import InjectedFormulaInput from '@fwego/modules/core/components/formula/InjectedFormulaInput'
import FieldMappingContext from '@fwego/modules/integrations/localFwego/components/services/FieldMappingContext'

export default {
  name: 'FieldMapping',
  components: { FieldMappingContext, InjectedFormulaInput },
  props: {
    fieldMapping: {
      type: Object,
      required: true,
    },
  },
  computed: {
    fieldValue: {
      get() {
        return this.fieldMapping.value
      },
      set(value) {
        this.$emit('change', { value })
      },
    },
  },
  methods: {
    openContext() {
      this.$refs.fieldMappingContext.toggle(
        this.$refs.editFieldMappingOpener,
        'bottom',
        'left',
        4
      )
    },
  },
}
</script>
