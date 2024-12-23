<template>
  <form>
    <LocalFwegoTableSelector
      v-model="computedTableId"
      class="local-fwego-user-source-form__table-selector"
      :databases="integration.context_data.databases"
      :display-view-dropdown="false"
      dropdown-size="large"
    />

    <p>{{ $t('localFwegoUserSourceForm.description') }}</p>
    <FormRow>
      <FormGroup
        :label="$t('localFwegoUserSourceForm.emailFieldLabel')"
        small-label
        required
      >
        <Dropdown
          v-model="values.email_field_id"
          fixed-items
          :disabled="!selectedTable"
          :placeholder="
            $t('localFwegoUserSourceForm.emailFieldLabelPlaceholder')
          "
          size="large"
        >
          <DropdownItem
            v-for="field in emailFields"
            :key="field.id"
            :name="field.name"
            :value="field.id"
            :icon="getIconForType(field.type)"
          />
          <template #emptyState>
            {{ $t('localFwegoUserSourceForm.noFields') }}
          </template>
        </Dropdown>
      </FormGroup>

      <FormGroup
        :label="$t('localFwegoUserSourceForm.nameFieldLabel')"
        small-label
        required
      >
        <Dropdown
          v-model="values.name_field_id"
          fixed-items
          :disabled="!selectedTable"
          :placeholder="$t('localFwegoUserSourceForm.nameFieldPlaceholder')"
          size="large"
        >
          <DropdownItem
            v-for="field in nameFields"
            :key="field.id"
            :name="field.name"
            :value="field.id"
            :icon="getIconForType(field.type)"
          />
          <template #emptyState>
            {{ $t('localFwegoUserSourceForm.noFields') }}
          </template>
        </Dropdown>
      </FormGroup>

      <FormGroup
        :label="$t('localFwegoUserSourceForm.roleFieldLabel')"
        small-label
        required
      >
        <Dropdown
          v-model="values.role_field_id"
          fixed-items
          :disabled="!selectedTable"
          :placeholder="$t('localFwegoUserSourceForm.roleFieldPlaceholder')"
          size="large"
        >
          <DropdownItem
            key="use-default-role"
            name="Use Default Role"
            :value="null"
            icon="iconoir-user"
          />
          <DropdownItem
            v-for="field in roleFields"
            :key="field.id"
            :name="field.name"
            :value="field.id"
            :icon="getIconForType(field.type)"
          />
          <template #emptyState>
            {{ $t('localFwegoUserSourceForm.noFields') }}
          </template>
        </Dropdown>
      </FormGroup>
    </FormRow>
  </form>
</template>

<script>
import form from '@fwego/modules/core/mixins/form'
import LocalFwegoTableSelector from '@fwego/modules/integrations/localFwego/components/services/LocalFwegoTableSelector'

export default {
  components: {
    LocalFwegoTableSelector,
  },
  mixins: [form],
  props: {
    application: {
      type: Object,
      required: true,
    },
    integration: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      values: {
        table_id: null,
        email_field_id: null,
        name_field_id: null,
        role_field_id: null,
      },
      allowedValues: [
        'table_id',
        'email_field_id',
        'name_field_id',
        'role_field_id',
      ],
    }
  },
  computed: {
    userSourceType() {
      return this.$registry.get('userSource', 'local_fwego')
    },
    databases() {
      return this.integration.context_data.databases
    },
    fieldTypes() {
      return this.$registry.getAll('field')
    },
    computedTableId: {
      get() {
        return this.values.table_id
      },
      set(newValue) {
        // If we currently have a `table_id` selected, and the `newValue`
        // is different to the current `table_id`, then reset the `fields`
        // to null.
        if (this.values.table_id && this.values.table_id !== newValue) {
          this.values.email_field_id = null
          this.values.name_field_id = null
          this.values.role_field_id = null
        }
        this.values.table_id = newValue
      },
    },
    selectedTable() {
      if (!this.values.table_id) {
        return null
      }
      for (const database of this.databases) {
        for (const table of database.tables) {
          if (table.id === this.values.table_id) {
            return table
          }
        }
      }
      return null
    },
    fields() {
      if (!this.selectedTable) {
        return []
      } else {
        return this.selectedTable.fields
      }
    },
    emailFields() {
      return this.fields.filter(({ type }) =>
        this.userSourceType.allowedEmailFieldTypes.includes(type)
      )
    },
    nameFields() {
      return this.fields.filter(({ type }) =>
        this.userSourceType.allowedNameFieldTypes.includes(type)
      )
    },
    roleFields() {
      return this.fields.filter(({ type }) =>
        this.userSourceType.allowedRoleFieldTypes.includes(type)
      )
    },
  },
  methods: {
    getIconForType(type) {
      return this.fieldTypes[type].getIconClass()
    },
  },
}
</script>
