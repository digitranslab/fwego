import { DataSyncType } from '@fwego/modules/database/dataSyncTypes'

import LocalFwegoTableDataSync from '@fwego_enterprise/components/dataSync/LocalFwegoTableDataSync'
import EnterpriseFeatures from '@fwego_enterprise/features'
import EnterpriseModal from '@fwego_enterprise/components/EnterpriseModal'
import JiraIssuesDataSyncForm from '@fwego_enterprise/components/dataSync/JiraIssuesDataSyncForm'
import GitHubIssuesDataSyncForm from '@fwego_enterprise/components/dataSync/GitHubIssuesDataSyncForm'
import GitLabIssuesDataSyncForm from '@fwego_enterprise/components/dataSync/GitLabIssuesDataSyncForm'
import HubspotContactsDataSyncForm from '@fwego_enterprise/components/dataSync/HubspotContactsDataSyncForm'

export class LocalFwegoTableDataSyncType extends DataSyncType {
  static getType() {
    return 'local_fwego_table'
  }

  getIconClass() {
    return 'iconoir-menu'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('enterpriseDataSyncType.localFwegoTable')
  }

  getFormComponent() {
    return LocalFwegoTableDataSync
  }

  isDeactivated(workspaceId) {
    return !this.app.$hasFeature(EnterpriseFeatures.DATA_SYNC, workspaceId)
  }

  getDeactivatedClickModal() {
    return EnterpriseModal
  }
}

export class JiraIssuesDataSyncType extends DataSyncType {
  static getType() {
    return 'jira_issues'
  }

  getIconClass() {
    return 'fwego-icon-jira'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('enterpriseDataSyncType.jiraIssues')
  }

  getFormComponent() {
    return JiraIssuesDataSyncForm
  }

  isDeactivated(workspaceId) {
    return !this.app.$hasFeature(EnterpriseFeatures.DATA_SYNC, workspaceId)
  }

  getDeactivatedClickModal() {
    return EnterpriseModal
  }
}

export class GitHubIssuesDataSyncType extends DataSyncType {
  static getType() {
    return 'github_issues'
  }

  getIconClass() {
    return 'iconoir-github'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('enterpriseDataSyncType.githubIssues')
  }

  getFormComponent() {
    return GitHubIssuesDataSyncForm
  }

  isDeactivated(workspaceId) {
    return !this.app.$hasFeature(EnterpriseFeatures.DATA_SYNC, workspaceId)
  }

  getDeactivatedClickModal() {
    return EnterpriseModal
  }
}

export class GitLabIssuesDataSyncType extends DataSyncType {
  static getType() {
    return 'gitlab_issues'
  }

  getIconClass() {
    return 'fwego-icon-gitlab'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('enterpriseDataSyncType.gitlabIssues')
  }

  getFormComponent() {
    return GitLabIssuesDataSyncForm
  }

  isDeactivated(workspaceId) {
    return !this.app.$hasFeature(EnterpriseFeatures.DATA_SYNC, workspaceId)
  }

  getDeactivatedClickModal() {
    return EnterpriseModal
  }
}

export class HubspotContactsDataSyncType extends DataSyncType {
  static getType() {
    return 'hubspot_contacts'
  }

  getIconClass() {
    return 'fwego-icon-hubspot'
  }

  getName() {
    const { i18n } = this.app
    return i18n.t('enterpriseDataSyncType.hubspotContacts')
  }

  getFormComponent() {
    return HubspotContactsDataSyncForm
  }

  isDeactivated(workspaceId) {
    return !this.app.$hasFeature(EnterpriseFeatures.DATA_SYNC, workspaceId)
  }

  getDeactivatedClickModal() {
    return EnterpriseModal
  }
}
