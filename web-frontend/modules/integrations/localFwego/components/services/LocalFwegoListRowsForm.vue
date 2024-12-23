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
      <div class="col col-12">
        <Tabs>
          <Tab
            :title="$t('localFwegoListRowsForm.filterTabTitle')"
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
              {{ $t('localFwegoListRowsForm.noTableChosenForFiltering') }}
            </p>
          </Tab>
          <Tab
            :title="$t('localFwegoListRowsForm.sortTabTitle')"
            class="data-source-form__sort-form-tab"
          >
            <LocalFwegoTableServiceSortForm
              v-if="values.table_id"
              v-model="dataSourceSortings"
              :fields="tableFields"
            ></LocalFwegoTableServiceSortForm>
            <p v-if="!values.table_id">
              {{ $t('localFwegoListRowsForm.noTableChosenForSorting') }}
            </p>
          </Tab>
          <Tab
            :title="$t('localFwegoListRowsForm.searchTabTitle')"
            class="data-source-form__search-form-tab"
          >
            <InjectedFormulaInput
              v-model="values.search_query"
              small
              :placeholder="
                $t('localFwegoListRowsForm.searchFieldPlaceHolder')
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
import LocalFwegoTableServiceSortForm from '@fwego/modules/integrations/localFwego/components/services/LocalFwegoTableServiceSortForm'
import InjectedFormulaInput from '@fwego/modules/core/components/formula/InjectedFormulaInput'
import localFwegoService from '@fwego/modules/integrations/localFwego/mixins/localFwegoService'

export default {
  components: {
    InjectedFormulaInput,
    LocalFwegoTableSelector,
    LocalFwegoTableServiceSortForm,
    LocalFwegoTableServiceConditionalForm,
  },
  mixins: [form, localFwegoService],
  data() {
    return {
      allowedValues: [
        'table_id',
        'view_id',
        'search_query',
        'filters',
        'filter_type',
        'sortings',
      ],
      values: {
        table_id: null,
        view_id: null,
        search_query: '',
        filters: [],
        sortings: [],
        filter_type: 'AND',
      },
      tableLoading: false,
    }
  },
}
</script>
