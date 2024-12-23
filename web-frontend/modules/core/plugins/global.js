import Vue from 'vue'

import Context from '@fwego/modules/core/components/Context'
import Modal from '@fwego/modules/core/components/Modal'
import Editable from '@fwego/modules/core/components/Editable'
import Dropdown from '@fwego/modules/core/components/Dropdown'
import DropdownItem from '@fwego/modules/core/components/DropdownItem'
import Picker from '@fwego/modules/core/components/Picker'
import ProgressBar from '@fwego/modules/core/components/ProgressBar'
import Checkbox from '@fwego/modules/core/components/Checkbox'
import Radio from '@fwego/modules/core/components/Radio'
import RadioGroup from '@fwego/modules/core/components/RadioGroup'
import Scrollbars from '@fwego/modules/core/components/Scrollbars'
import Error from '@fwego/modules/core/components/Error'
import SwitchInput from '@fwego/modules/core/components/SwitchInput'
import Copied from '@fwego/modules/core/components/Copied'
import MarkdownIt from '@fwego/modules/core/components/MarkdownIt'
import DownloadLink from '@fwego/modules/core/components/DownloadLink'
import FormElement from '@fwego/modules/core/components/FormElement'
import Alert from '@fwego/modules/core/components/Alert'
import Tabs from '@fwego/modules/core/components/Tabs'
import Tab from '@fwego/modules/core/components/Tab'
import List from '@fwego/modules/core/components/List'
import HelpIcon from '@fwego/modules/core/components/HelpIcon'
import Button from '@fwego/modules/core/components/Button'
import ButtonText from '@fwego/modules/core/components/ButtonText'
import ButtonAdd from '@fwego/modules/core/components/ButtonAdd'
import ButtonIcon from '@fwego/modules/core/components/ButtonIcon'
import ButtonFloating from '@fwego/modules/core/components/ButtonFloating'
import Avatar from '@fwego/modules/core/components/Avatar'
import Chips from '@fwego/modules/core/components/Chips'
import Presentation from '@fwego/modules/core/components/Presentation'
import FormInput from '@fwego/modules/core/components/FormInput'
import ImageInput from '@fwego/modules/core/components/ImageInput'
import FormTextarea from '@fwego/modules/core/components/FormTextarea'
import CallToAction from '@fwego/modules/core/components/CallToAction.vue'
import FormGroup from '@fwego/modules/core/components/FormGroup'
import FormRow from '@fwego/modules/core/components/FormRow'
import Logo from '@fwego/modules/core/components/Logo'
import ReadOnlyForm from '@fwego/modules/core/components/ReadOnlyForm'
import FormSection from '@fwego/modules/core/components/FormSection'

import lowercase from '@fwego/modules/core/filters/lowercase'
import uppercase from '@fwego/modules/core/filters/uppercase'
import nameAbbreviation from '@fwego/modules/core/filters/nameAbbreviation'

import scroll from '@fwego/modules/core/directives/scroll'
import preventParentScroll from '@fwego/modules/core/directives/preventParentScroll'
import tooltip from '@fwego/modules/core/directives/tooltip'
import sortable from '@fwego/modules/core/directives/sortable'
import autoOverflowScroll from '@fwego/modules/core/directives/autoOverflowScroll'
import userFileUpload from '@fwego/modules/core/directives/userFileUpload'
import autoScroll from '@fwego/modules/core/directives/autoScroll'
import clickOutside from '@fwego/modules/core/directives/clickOutside'
import Badge from '@fwego/modules/core/components/Badge'
import BadgeCollaborator from '@fwego/modules/core/components/BadgeCollaborator'
import Expandable from '@fwego/modules/core/components/Expandable.vue'
import RadioButton from '@fwego/modules/core/components/RadioButton'
import Thumbnail from '@fwego/modules/core/components/Thumbnail'
import ColorInput from '@fwego/modules/core/components/ColorInput'
import SelectSearch from '@fwego/modules/core/components/SelectSearch'

function setupVue(Vue) {
  Vue.component('Context', Context)
  Vue.component('Modal', Modal)
  Vue.component('Editable', Editable)
  Vue.component('Dropdown', Dropdown)
  Vue.component('DropdownItem', DropdownItem)
  Vue.component('Checkbox', Checkbox)
  Vue.component('Radio', Radio)
  Vue.component('RadioGroup', RadioGroup)
  Vue.component('Scrollbars', Scrollbars)
  Vue.component('Alert', Alert)
  Vue.component('Error', Error)
  Vue.component('SwitchInput', SwitchInput)
  Vue.component('Copied', Copied)
  Vue.component('MarkdownIt', MarkdownIt)
  Vue.component('DownloadLink', DownloadLink)
  Vue.component('FormElement', FormElement)
  Vue.component('Picker', Picker)
  Vue.component('ProgressBar', ProgressBar)
  Vue.component('Tab', Tab)
  Vue.component('Tabs', Tabs)
  Vue.component('List', List)
  Vue.component('HelpIcon', HelpIcon)
  Vue.component('Badge', Badge)
  Vue.component('BadgeCollaborator', BadgeCollaborator)
  Vue.component('Expandable', Expandable)
  Vue.component('Button', Button)
  Vue.component('ButtonText', ButtonText)
  Vue.component('ButtonFloating', ButtonFloating)
  Vue.component('ButtonAdd', ButtonAdd)
  Vue.component('ButtonIcon', ButtonIcon)
  Vue.component('Chips', Chips)
  Vue.component('RadioButton', RadioButton)
  Vue.component('Thumbnail', Thumbnail)
  Vue.component('Avatar', Avatar)
  Vue.component('Presentation', Presentation)
  Vue.component('FormInput', FormInput)
  Vue.component('FormTextarea', FormTextarea)
  Vue.component('CallToAction', CallToAction)
  Vue.component('FormGroup', FormGroup)
  Vue.component('FormRow', FormRow)
  Vue.component('ColorInput', ColorInput)
  Vue.component('ImageInput', ImageInput)
  Vue.component('SelectSearch', SelectSearch)
  Vue.component('Logo', Logo)
  Vue.component('ReadOnlyForm', ReadOnlyForm)
  Vue.component('FormSection', FormSection)

  Vue.filter('lowercase', lowercase)
  Vue.filter('uppercase', uppercase)
  Vue.filter('nameAbbreviation', nameAbbreviation)

  Vue.directive('scroll', scroll)
  Vue.directive('preventParentScroll', preventParentScroll)
  Vue.directive('tooltip', tooltip)
  Vue.directive('sortable', sortable)
  Vue.directive('autoOverflowScroll', autoOverflowScroll)
  Vue.directive('userFileUpload', userFileUpload)
  Vue.directive('autoScroll', autoScroll)
  Vue.directive('clickOutside', clickOutside)

  Vue.prototype.$super = function (options) {
    return new Proxy(options, {
      get: (options, name) => {
        if (options.methods && name in options.methods) {
          return options.methods[name].bind(this)
        }
      },
    })
  }
}

setupVue(Vue)

export { setupVue }
