<template>
  <div>
    <div
      v-if="(!value || (!opened && generating)) && !readOnly"
      ref="cell"
      class="grid-view__cell active"
    >
      <div class="grid-field-button">
        <Button
          type="secondary"
          size="tiny"
          :disabled="!modelAvailable || generating"
          :loading="generating"
          :icon="isDeactivated ? 'iconoir-lock' : ''"
          @click="generate()"
        >
          {{ $t('gridViewFieldAI.generate') }}
        </Button>
      </div>
    </div>
    <component
      :is="outputGridViewFieldComponent"
      v-else
      ref="cell"
      v-bind="$props"
      :read-only="true"
    >
      <template v-if="!readOnly && editing" #default="{ editing }">
        <div style="background-color: #fff; padding: 8px">
          <ButtonText
            v-if="!isDeactivated"
            icon="iconoir-magic-wand"
            :disabled="!modelAvailable || generating"
            :loading="generating"
            @click.prevent.stop="generate()"
          >
            {{ $t('gridViewFieldAI.regenerate') }}
          </ButtonText>
          <ButtonText
            v-else
            icon="iconoir-lock"
            @click.prevent.stop="$refs.clickModal.show()"
          >
            {{ $t('gridViewFieldAI.regenerate') }}
          </ButtonText>
        </div>
      </template>
    </component>
    <component
      :is="deactivatedClickComponent"
      v-if="isDeactivated && workspace"
      ref="clickModal"
      :workspace="workspace"
      :name="fieldName"
    ></component>
  </div>
</template>

<script>
import { isElement } from '@fwego/modules/core/utils/dom'
import gridField from '@fwego/modules/database/mixins/gridField'
import gridFieldInput from '@fwego/modules/database/mixins/gridFieldInput'
import gridFieldAI from '@fwego_premium/mixins/gridFieldAI'

export default {
  name: 'GridViewFieldAI',
  mixins: [gridField, gridFieldInput, gridFieldAI],
  computed: {
    fieldName() {
      return this.$registry.get('field', this.field.type).getName()
    },
    outputGridViewFieldComponent() {
      return this.$registry
        .get('aiFieldOutputType', this.field.ai_output_type)
        .getFwegoFieldType()
        .getGridViewFieldComponent(this.field)
    },
  },
  methods: {
    save() {
      this.opened = false
      this.editing = false
      this.afterSave()
    },
    canUnselectByClickingOutside(event) {
      if (this.isDeactivated && this.workspace) {
        return !isElement(this.$refs.clickModal.$el, event.target)
      }
      return true
    },
  },
}
</script>
