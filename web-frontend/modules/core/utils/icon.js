import {
  DATA_TYPE_TO_ICON_MAP,
  UNKNOWN_DATA_TYPE_ICON,
} from '@fwego/modules/core/enums'

export const getIconForType = (type) => {
  return DATA_TYPE_TO_ICON_MAP[type] || UNKNOWN_DATA_TYPE_ICON
}
