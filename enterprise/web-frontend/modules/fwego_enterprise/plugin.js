import { registerRealtimeEvents } from '@fwego_enterprise/realtime'
import { RolePermissionManagerType } from '@fwego_enterprise/permissionManagerTypes'
import { AuthProvidersType, AuditLogType } from '@fwego_enterprise/adminTypes'
import authProviderAdminStore from '@fwego_enterprise/store/authProviderAdmin'
import { PasswordAuthProviderType as CorePasswordAuthProviderType } from '@fwego/modules/core/authProviderTypes'
import {
  PasswordAuthProviderType,
  SamlAuthProviderType,
  GitHubAuthProviderType,
  GoogleAuthProviderType,
  FacebookAuthProviderType,
  GitLabAuthProviderType,
  OpenIdConnectAuthProviderType,
} from '@fwego_enterprise/authProviderTypes'
import { TeamsWorkspaceSettingsPageType } from '@fwego_enterprise/workspaceSettingsPageTypes'
import { EnterpriseMembersPagePluginType } from '@fwego_enterprise/membersPagePluginTypes'
import en from '@fwego_enterprise/locales/en.json'
import fr from '@fwego_enterprise/locales/fr.json'
import nl from '@fwego_enterprise/locales/nl.json'
import de from '@fwego_enterprise/locales/de.json'
import es from '@fwego_enterprise/locales/es.json'
import it from '@fwego_enterprise/locales/it.json'
import ko from '@fwego_enterprise/locales/ko.json'
import {
  EnterpriseWithoutSupportLicenseType,
  EnterpriseLicenseType,
} from '@fwego_enterprise/licenseTypes'
import { EnterprisePlugin } from '@fwego_enterprise/plugins'
import { LocalFwegoUserSourceType } from '@fwego_enterprise/integrations/userSourceTypes'
import {
  LocalFwegoPasswordAppAuthProviderType,
  SamlAppAuthProviderType,
} from '@fwego_enterprise/integrations/appAuthProviderTypes'
import { AuthFormElementType } from '@fwego_enterprise/builder/elementTypes'
import {
  EnterpriseAdminRoleType,
  EnterpriseMemberRoleType,
  EnterpriseBuilderRoleType,
  EnterpriseEditorRoleType,
  EnterpriseCommenterRoleType,
  EnterpriseViewerRoleType,
  NoAccessRoleType,
  NoRoleLowPriorityRoleType,
} from '@fwego_enterprise/roleTypes'
import {
  LocalFwegoTableDataSyncType,
  JiraIssuesDataSyncType,
  GitHubIssuesDataSyncType,
  GitLabIssuesDataSyncType,
  HubspotContactsDataSyncType,
} from '@fwego_enterprise/dataSyncTypes'

import { FF_AB_SSO } from '@fwego/modules/core/plugins/featureFlags'

export default (context) => {
  const { app, isDev, store } = context

  // Allow locale file hot reloading
  if (isDev && app.i18n) {
    const { i18n } = app
    i18n.mergeLocaleMessage('en', en)
    i18n.mergeLocaleMessage('fr', fr)
    i18n.mergeLocaleMessage('nl', nl)
    i18n.mergeLocaleMessage('de', de)
    i18n.mergeLocaleMessage('es', es)
    i18n.mergeLocaleMessage('it', it)
    i18n.mergeLocaleMessage('ko', ko)
  }

  app.$registry.register('plugin', new EnterprisePlugin(context))

  app.$registry.register(
    'permissionManager',
    new RolePermissionManagerType(context)
  )

  store.registerModule('authProviderAdmin', authProviderAdminStore)

  app.$registry.register('admin', new AuthProvidersType(context))
  app.$registry.unregister(
    'authProvider',
    new CorePasswordAuthProviderType(context)
  )
  app.$registry.register('authProvider', new PasswordAuthProviderType(context))
  app.$registry.register('authProvider', new SamlAuthProviderType(context))
  app.$registry.register('authProvider', new GoogleAuthProviderType(context))
  app.$registry.register('authProvider', new FacebookAuthProviderType(context))
  app.$registry.register('authProvider', new GitHubAuthProviderType(context))
  app.$registry.register('authProvider', new GitLabAuthProviderType(context))
  app.$registry.register(
    'authProvider',
    new OpenIdConnectAuthProviderType(context)
  )

  app.$registry.register('admin', new AuditLogType(context))
  app.$registry.register('plugin', new EnterprisePlugin(context))

  registerRealtimeEvents(app.$realtime)

  app.$registry.register(
    'membersPagePlugins',
    new EnterpriseMembersPagePluginType(context)
  )

  app.$registry.register(
    'workspaceSettingsPage',
    new TeamsWorkspaceSettingsPageType(context)
  )

  app.$registry.register(
    'license',
    new EnterpriseWithoutSupportLicenseType(context)
  )

  app.$registry.register('license', new EnterpriseLicenseType(context))

  app.$registry.register('userSource', new LocalFwegoUserSourceType(context))

  app.$registry.register(
    'appAuthProvider',
    new LocalFwegoPasswordAppAuthProviderType(context)
  )

  if (app.$featureFlagIsEnabled(FF_AB_SSO)) {
    app.$registry.register(
      'appAuthProvider',
      new SamlAppAuthProviderType(context)
    )
  }

  app.$registry.register('roles', new EnterpriseAdminRoleType(context))
  app.$registry.register('roles', new EnterpriseMemberRoleType(context))
  app.$registry.register('roles', new EnterpriseBuilderRoleType(context))
  app.$registry.register('roles', new EnterpriseEditorRoleType(context))
  app.$registry.register('roles', new EnterpriseCommenterRoleType(context))
  app.$registry.register('roles', new EnterpriseViewerRoleType(context))
  app.$registry.register('roles', new NoAccessRoleType(context))
  app.$registry.register('roles', new NoRoleLowPriorityRoleType(context))

  app.$registry.register('element', new AuthFormElementType(context))

  app.$registry.register('dataSync', new LocalFwegoTableDataSyncType(context))
  app.$registry.register('dataSync', new JiraIssuesDataSyncType(context))
  app.$registry.register('dataSync', new GitHubIssuesDataSyncType(context))
  app.$registry.register('dataSync', new GitLabIssuesDataSyncType(context))
  app.$registry.register('dataSync', new HubspotContactsDataSyncType(context))
}
