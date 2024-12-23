<template>
  <form @submit.prevent>
    <div>
      <div class="row">
        <div class="col col-12">
          <LocalFwegoTableSelector
            v-model="fakeTableId"
            class="local-fwego-get-row-form__table-selector"
            :databases="databases"
            :view-id.sync="values.view_id"
          ></LocalFwegoTableSelector>
        </div>
      </div>
      <div class="row">
        <div class="col col-6">
          <FormGroup
            small-label
            :label="$t('localFwegoGetRowForm.rowFieldLabel')"
            required
          >
            <InjectedFormulaInput
              v-model="values.row_id"
              :placeholder="$t('localFwegoGetRowForm.rowFieldPlaceHolder')"
            />
            <template #helper>
              {{ $t('localFwegoGetRowForm.rowFieldHelpText') }}
            </template>
          </FormGroup>
        </div>
      </div>
      <div class="row">
        <div class="col col-12">
          <Tabs>
            <Tab
              :title="$t('localFwegoGetRowForm.filterTabTitle')"
              class="data-source-form__condition-form-tab"
            >
              <LocalFwegoTableServiceConditionalForm
                v-if="values.table_id"
                v-model="dataSourceFilters"
                :fields="tableFields"
                :filter-type.sync="values.filter_type"
              />
              <p v-if="!values.table_id">
                {{ $t('localFwegoGetRowForm.noTableChosenForFiltering') }}
              </p>
            </Tab>
            <Tab
              :title="$t('localFwegoGetRowForm.searchTabTitle')"
              class="data-source-form__search-form-tab"
            >
              <FormGroup>
                <InjectedFormulaInput
                  v-model="values.search_query"
                  :placeholder="
                    $t('localFwegoGetRowForm.searchFieldPlaceHolder')
                  "
                />
              </FormGroup>
            </Tab>
          </Tabs>
        </div>
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
        'row_id',
        'search_query',
        'filters',
        'filter_type',
      ],
      values: {
        table_id: null,
        view_id: null,
        row_id: '',
        search_query: '',
        filters: [],
        filter_type: 'AND',
      },
      tableLoading: false,
    }
  },
}
</script>
