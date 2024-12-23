<template>
  <div class="fwego-table-wrapper">
    <table class="fwego-table" :class="`fwego-table--${orientation}`">
      <template v-if="orientation === TABLE_ORIENTATION.HORIZONTAL">
        <thead>
          <tr class="fwego-table__row">
            <template v-for="field in fields">
              <slot name="field-name" :field="field">
                <th :key="field.__id__" class="fwego-table__header-cell">
                  {{ field.name }}
                </th>
              </slot>
            </template>
          </tr>
        </thead>
        <tbody v-if="rows.length">
          <tr
            v-for="(row, index) in rows"
            :key="row.__id__"
            class="fwego-table__row"
          >
            <template v-for="field in fields">
              <slot
                name="cell-content"
                :value="row[field.name]"
                :field="field"
                :row-index="index"
              >
                <td :key="field.id" class="fwego-table__cell">
                  {{ row[field.name] }}
                </td>
              </slot>
            </template>
          </tr>
        </tbody>
      </template>
      <template v-else>
        <template v-if="rows.length">
          <tbody
            v-for="(row, rowIndex) in rows"
            :key="row.__id__"
            class="fwego-table__row"
          >
            <tr
              v-for="(field, fieldIndex) in fields"
              :key="`${row.__id__}_${field.id}`"
            >
              <slot name="field-name" :field="field">
                <th :key="field.__id__" class="fwego-table__header-cell">
                  {{ field.name }}
                </th>
              </slot>
              <slot
                name="cell-content"
                :value="row[field.name]"
                :field="field"
                :row-index="rowIndex"
              >
                <td
                  class="fwego-table__cell"
                  :class="{
                    'fwego-table__separator':
                      fieldIndex === fields.length - 1,
                  }"
                >
                  {{ value }}
                </td>
              </slot>
            </tr>
          </tbody>
        </template>
      </template>
      <tbody v-if="!rows.length">
        <tr>
          <td class="fwego-table__empty-message" :colspan="fields.length">
            <slot name="empty-state"></slot>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { TABLE_ORIENTATION } from '@fwego/modules/builder/enums'

export default {
  name: 'FwegoTable',
  inject: ['mode'],
  props: {
    fields: {
      type: Array,
      required: true,
    },
    rows: {
      type: Array,
      required: true,
    },
    orientation: {
      type: String,
      default: TABLE_ORIENTATION.HORIZONTAL,
    },
  },
  computed: {
    TABLE_ORIENTATION() {
      return TABLE_ORIENTATION
    },
  },
}
</script>
