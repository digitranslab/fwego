import Vue from 'vue'

import ABButton from '@fwego/modules/builder/components/elements/baseComponents/ABButton'
import ABInput from '@fwego/modules/builder/components/elements/baseComponents/ABInput'
import ABFormGroup from '@fwego/modules/builder/components/elements/baseComponents/ABFormGroup'
import ABLink from '@fwego/modules/builder/components/elements/baseComponents/ABLink'
import ABHeading from '@fwego/modules/builder/components/elements/baseComponents/ABHeading'
import ABDropdown from '@fwego/modules/builder/components/elements/baseComponents/ABDropdown'
import ABDropdownItem from '@fwego/modules/builder/components/elements/baseComponents/ABDropdownItem'
import ABCheckbox from '@fwego/modules/builder/components/elements/baseComponents/ABCheckbox.vue'
import ABRadio from '@fwego/modules/builder/components/elements/baseComponents/ABRadio.vue'
import ABImage from '@fwego/modules/builder/components/elements/baseComponents/ABImage.vue'
import ABParagraph from '@fwego/modules/builder/components/elements/baseComponents/ABParagraph.vue'
import ABTag from '@fwego/modules/builder/components/elements/baseComponents/ABTag.vue'
import ABTable from '@fwego/modules/builder/components/elements/baseComponents/ABTable.vue'

function setupVueForAB(Vue) {
  Vue.component('ABButton', ABButton)
  Vue.component('ABInput', ABInput)
  Vue.component('ABFormGroup', ABFormGroup)
  Vue.component('ABLink', ABLink)
  Vue.component('ABHeading', ABHeading)
  Vue.component('ABDropdown', ABDropdown)
  Vue.component('ABDropdownItem', ABDropdownItem)
  Vue.component('ABCheckbox', ABCheckbox)
  Vue.component('ABRadio', ABRadio)
  Vue.component('ABImage', ABImage)
  Vue.component('ABParagraph', ABParagraph)
  Vue.component('ABTag', ABTag)
  Vue.component('ABTable', ABTable)
}

setupVueForAB(Vue)

export { setupVueForAB }
