export const IMAGE_FILE_TYPES = [
  'image/jpeg',
  'image/jpg',
  'image/png',
  'image/apng',
  'image/gif',
  'image/tiff',
  'image/bmp',
  'image/webp',
]

export const FAVICON_IMAGE_FILE_TYPES = [...IMAGE_FILE_TYPES, 'image/x-icon']

// Keep these in sync with the backend options in
// fwego.core.models.Settings.EmailVerificationOptions
export const EMAIL_VERIFICATION_OPTIONS = {
  NO_VERIFICATION: 'no_verification',
  RECOMMENDED: 'recommended',
  ENFORCED: 'enforced',
}

// Keep these in sync with the backend options in
// fwego.core.models.UserProfile.EmailNotificationFrequencyOptions
export const EMAIL_NOTIFICATIONS_FREQUENCY_OPTIONS = {
  INSTANT: 'instant',
  DAILY: 'daily',
  WEEKLY: 'weekly',
  NEVER: 'never',
}

export const DATA_TYPE_TO_ICON_MAP = {
  string: 'iconoir-text',
  number: 'fwego-icon-hashtag',
  boolean: 'fwego-icon-circle-checked',
  date: 'iconoir-calendar',
  datetime: 'iconoir-calendar',
  array: 'iconoir-list',
}

export const UNKNOWN_DATA_TYPE_ICON = 'iconoir-question-mark'
