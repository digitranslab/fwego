<template>
  <form @submit.prevent>
    <div class="row">
      <div class="col col-12">
        <LocalFwegoTableSelector
          v-model="fakeTableId"
          :databases="databases"
          :view-id.sync="values.view_id"
        ></LocalFwegoTableSelector>
      </div>
    </div>
    <div class="row">
      <div class="col col-6">
        <FormGroup
          small-label
          :label="$t('localFwegoAggregateRowsForm.aggregationFieldLabel')"
          required
        >
          <Dropdown
            v-model="values.field_id"
            :disabled="tableFields.length === 0"
          >
            <DropdownItem
              v-for="field in tableFields"
              :key="field.id"
              :name="field.name"
              :value="field.id"
            >
            </DropdownItem>
          </Dropdown>
        </FormGroup>
      </div>
      <div class="col col-6">
        <FormGroup
          small-label
          :label="$t('localFwegoAggregateRowsForm.aggregationTypeLabel')"
          required
        >
          <Dropdown
            v-model="values.aggregation_type"
            :disabled="!values.field_id"
          >
            <DropdownItem
              v-for="viewAggregation in viewAggregationTypes"
              :key="viewAggregation.getType()"
              :name="viewAggregation.getName()"
              :value="viewAggregation.getType()"
            >
            </DropdownItem>
          </Dropdown>
        </FormGroup>
      </div>
    </div>
    <div class="margin-top-2 row">
      <div class="col col-12">
        <Tabs>
          <Tab
            :title="$t('localFwegoAggregateRowsForm.filterTabTitle')"
            class="data-source-form__condition-form-tab"
          >
            <LocalFwegoTableServiceConditionalForm
              v-if="values.table_id"
              v-model="dataSourceFilters"
              :fields="tableFields"
              :filter-type.sync="values.filter_type"
            >
            </LocalFwegoTableServiceConditionalForm>
            <p v-if="!values.table_id">
              {{
                $t('localFwegoAggregateRowsForm.noTableChosenForFiltering')
              }}
            </p>
          </Tab>
          <Tab
            :title="$t('localFwegoAggregateRowsForm.searchTabTitle')"
            class="data-source-form__search-form-tab"
          >
            <InjectedFormulaInput
              v-model="values.search_query"
              small
              :placeholder="
                $t('localFwegoAggregateRowsForm.searchFieldPlaceHolder')
              "
            />
          </Tab>
        </Tabs>
      </div>
    </div>
  </form>
</template>

<script>
import form from '@fwego/modules/core/mixins/form'
import LocalFwegoTableSelector from '@fwego/modules/integrations/localFwego/components/services/LocalFwegoTableSelector'
import LocalFwegoTableServiceConditionalForm from '@fwego/modules/integrations/localFwego/components/services/LocalFwegoTableServiceConditionalForm'
import InjectedFormulaInput from '@fwego/modules/core/components/formula/InjectedFormulaInput'
import localFwegoService from '@fwego/modules/integrations/localFwego/mixins/localFwegoService'

export default {
  components: {
    InjectedFormulaInput,
    LocalFwegoTableSelector,
    LocalFwegoTableServiceConditionalForm,
  },
  mixins: [form, localFwegoService],
  data() {
    return {
      allowedValues: [
        'table_id',
        'view_id',
        'field_id',
        'search_query',
        'filters',
        'filter_type',
        'aggregation_type',
      ],
      values: {
        table_id: null,
        view_id: null,
        field_id: null,
        search_query: '',
        filters: [],
        filter_type: 'AND',
        aggregation_type: 'sum',
      },
      tableLoading: false,
    }
  },
  computed: {
    viewAggregationTypes() {
      const selectedField = this.tableFields.find(
        (field) => field.id === this.values.field_id
      )
      if (!selectedField) return []
      return this.$registry
        .getOrderedList('viewAggregation')
        .filter((agg) => agg.fieldIsCompatible(selectedField))
    },
  },
}
</script>
