from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from fwego_premium.row_comments.operations import (
    CreateRowCommentsOperationType,
    DeleteRowCommentsOperationType,
    ReadRowCommentsOperationType,
    RestoreRowCommentOperationType,
    UpdateRowCommentsOperationType,
)

from fwego.contrib.builder.data_sources.operations import (
    CreateDataSourceOperationType,
    DeleteDataSourceOperationType,
    DispatchDataSourceOperationType,
    ListDataSourcesPageOperationType,
    OrderDataSourcesPageOperationType,
    ReadDataSourceOperationType,
    UpdateDataSourceOperationType,
)
from fwego.contrib.builder.domains.operations import (
    CreateDomainOperationType,
    DeleteDomainOperationType,
    PublishDomainOperationType,
    ReadDomainOperationType,
    RestoreDomainOperationType,
    UpdateDomainOperationType,
)
from fwego.contrib.builder.elements.operations import (
    CreateElementOperationType,
    DeleteElementOperationType,
    ListElementsPageOperationType,
    OrderElementsPageOperationType,
    ReadElementOperationType,
    UpdateElementOperationType,
)
from fwego.contrib.builder.operations import (
    ListDomainsBuilderOperationType,
    ListPagesBuilderOperationType,
    OrderDomainsBuilderOperationType,
    OrderPagesBuilderOperationType,
)
from fwego.contrib.builder.pages.operations import (
    CreatePageOperationType,
    DeletePageOperationType,
    DuplicatePageOperationType,
    ReadPageOperationType,
    UpdatePageOperationType,
)
from fwego.contrib.builder.theme.operations import UpdateThemeOperationType
from fwego.contrib.builder.workflow_actions.operations import (
    CreateBuilderWorkflowActionOperationType,
    DeleteBuilderWorkflowActionOperationType,
    DispatchBuilderWorkflowActionOperationType,
    ListBuilderWorkflowActionsPageOperationType,
    OrderBuilderWorkflowActionOperationType,
    ReadBuilderWorkflowActionOperationType,
    UpdateBuilderWorkflowActionOperationType,
)
from fwego.contrib.dashboard.data_sources.operations import (
    CreateDashboardDataSourceOperationType,
    DeleteDashboardDataSourceOperationType,
    DispatchDashboardDataSourceOperationType,
    ListDashboardDataSourcesOperationType,
    ReadDashboardDataSourceOperationType,
    UpdateDashboardDataSourceOperationType,
)
from fwego.contrib.dashboard.widgets.operations import (
    CreateWidgetOperationType,
    DeleteWidgetOperationType,
    ListWidgetsOperationType,
    ReadWidgetOperationType,
    UpdateWidgetOperationType,
)
from fwego.contrib.database.airtable.operations import (
    RunAirtableImportJobOperationType,
)
from fwego.contrib.database.data_sync.operations import (
    GetIncludingPublicValuesOperationType,
    ListPropertiesOperationType,
    SyncTableOperationType,
)
from fwego.contrib.database.export.operations import ExportTableOperationType
from fwego.contrib.database.fields.operations import (
    CreateFieldOperationType,
    DeleteFieldOperationType,
    DeleteRelatedLinkRowFieldOperationType,
    DuplicateFieldOperationType,
    ListFieldsOperationType,
    ReadFieldOperationType,
    RestoreFieldOperationType,
    UpdateFieldOperationType,
)
from fwego.contrib.database.formula import TypeFormulaOperationType
from fwego.contrib.database.operations import (
    CreateTableDatabaseTableOperationType,
    ListTablesDatabaseTableOperationType,
    OrderTablesDatabaseTableOperationType,
)
from fwego.contrib.database.rows.operations import (
    DeleteDatabaseRowOperationType,
    MoveRowDatabaseRowOperationType,
    ReadAdjacentRowDatabaseRowOperationType,
    ReadDatabaseRowHistoryOperationType,
    ReadDatabaseRowOperationType,
    RestoreDatabaseRowOperationType,
    UpdateDatabaseRowOperationType,
)
from fwego.contrib.database.table.operations import (
    CreateRowDatabaseTableOperationType,
    DeleteDatabaseTableOperationType,
    DuplicateDatabaseTableOperationType,
    ImportRowsDatabaseTableOperationType,
    ListenToAllDatabaseTableEventsOperationType,
    ListRowNamesDatabaseTableOperationType,
    ListRowsDatabaseTableOperationType,
    ReadDatabaseTableOperationType,
    RestoreDatabaseTableOperationType,
    UpdateDatabaseTableOperationType,
)
from fwego.contrib.database.tokens.operations import (
    CreateTokenOperationType,
    ReadTokenOperationType,
    UpdateTokenOperationType,
    UseTokenOperationType,
)
from fwego.contrib.database.views.operations import (
    CreateAndUsePersonalViewOperationType,
    CreatePublicViewOperationType,
    CreateViewDecorationOperationType,
    CreateViewFilterGroupOperationType,
    CreateViewFilterOperationType,
    CreateViewGroupByOperationType,
    CreateViewOperationType,
    CreateViewSortOperationType,
    DeleteViewDecorationOperationType,
    DeleteViewFilterGroupOperationType,
    DeleteViewFilterOperationType,
    DeleteViewGroupByOperationType,
    DeleteViewOperationType,
    DeleteViewSortOperationType,
    DuplicateViewOperationType,
    ListAggregationsViewOperationType,
    ListViewDecorationOperationType,
    ListViewFilterOperationType,
    ListViewGroupByOperationType,
    ListViewsOperationType,
    ListViewSortOperationType,
    OrderViewsOperationType,
    ReadAggregationsViewOperationType,
    ReadViewDecorationOperationType,
    ReadViewFieldOptionsOperationType,
    ReadViewFilterGroupOperationType,
    ReadViewFilterOperationType,
    ReadViewGroupByOperationType,
    ReadViewOperationType,
    ReadViewsOrderOperationType,
    ReadViewSortOperationType,
    RestoreViewOperationType,
    UpdateViewDecorationOperationType,
    UpdateViewFieldOptionsOperationType,
    UpdateViewFilterGroupOperationType,
    UpdateViewFilterOperationType,
    UpdateViewGroupByOperationType,
    UpdateViewOperationType,
    UpdateViewPublicOperationType,
    UpdateViewSlugOperationType,
    UpdateViewSortOperationType,
)
from fwego.contrib.database.webhooks.operations import (
    CreateWebhookOperationType,
    DeleteWebhookOperationType,
    ListTableWebhooksOperationType,
    ReadWebhookOperationType,
    TestTriggerWebhookOperationType,
    UpdateWebhookOperationType,
)
from fwego.core.integrations.operations import (
    CreateIntegrationOperationType,
    DeleteIntegrationOperationType,
    ListIntegrationsApplicationOperationType,
    OrderIntegrationsOperationType,
    ReadIntegrationOperationType,
    UpdateIntegrationOperationType,
)
from fwego.core.operations import (
    CreateApplicationsWorkspaceOperationType,
    CreateInvitationsWorkspaceOperationType,
    DeleteApplicationOperationType,
    DeleteWorkspaceInvitationOperationType,
    DeleteWorkspaceOperationType,
    DeleteWorkspaceUserOperationType,
    DuplicateApplicationOperationType,
    ListApplicationsWorkspaceOperationType,
    ListInvitationsWorkspaceOperationType,
    ListWorkspaceUsersWorkspaceOperationType,
    OrderApplicationsOperationType,
    ReadApplicationOperationType,
    ReadInvitationWorkspaceOperationType,
    ReadWorkspaceOperationType,
    RestoreApplicationOperationType,
    RestoreWorkspaceOperationType,
    UpdateApplicationOperationType,
    UpdateWorkspaceInvitationType,
    UpdateWorkspaceOperationType,
    UpdateWorkspaceUserOperationType,
)
from fwego.core.snapshots.operations import (
    CreateSnapshotApplicationOperationType,
    DeleteApplicationSnapshotOperationType,
    ListSnapshotsApplicationOperationType,
    RestoreApplicationSnapshotOperationType,
)
from fwego.core.trash.operations import (
    EmptyApplicationTrashOperationType,
    EmptyWorkspaceTrashOperationType,
    ReadApplicationTrashOperationType,
    ReadWorkspaceTrashOperationType,
)
from fwego.core.user_sources.operations import (
    AuthenticateUserSourceOperationType,
    CreateUserSourceOperationType,
    DeleteUserSourceOperationType,
    ListUserSourcesApplicationOperationType,
    LoginUserSourceOperationType,
    OrderUserSourcesOperationType,
    ReadUserSourceOperationType,
    UpdateUserSourceOperationType,
)
from fwego_enterprise.audit_log.operations import (
    ListWorkspaceAuditLogEntriesOperationType,
)
from fwego_enterprise.role.constants import (
    ADMIN_ROLE_UID,
    BUILDER_ROLE_UID,
    COMMENTER_ROLE_UID,
    EDITOR_ROLE_UID,
    NO_ACCESS_ROLE_UID,
    NO_ROLE_LOW_PRIORITY_ROLE_UID,
    VIEWER_ROLE_UID,
)
from fwego_enterprise.role.operations import (
    AssignRoleWorkspaceOperationType,
    ReadRoleApplicationOperationType,
    ReadRoleTableOperationType,
    ReadRoleWorkspaceOperationType,
    UpdateRoleApplicationOperationType,
    UpdateRoleTableOperationType,
)
from fwego_enterprise.teams.operations import (
    CreateTeamOperationType,
    CreateTeamSubjectOperationType,
    DeleteTeamOperationType,
    DeleteTeamSubjectOperationType,
    ListTeamsOperationType,
    ListTeamSubjectsOperationType,
    ReadTeamOperationType,
    ReadTeamSubjectOperationType,
    RestoreTeamOperationType,
    UpdateTeamOperationType,
)

default_roles = {
    ADMIN_ROLE_UID: [],
    BUILDER_ROLE_UID: [],
    EDITOR_ROLE_UID: [],
    COMMENTER_ROLE_UID: [],
    VIEWER_ROLE_UID: [],
    NO_ACCESS_ROLE_UID: [],
    NO_ROLE_LOW_PRIORITY_ROLE_UID: [],
}

if settings.FWEGO_PERSONAL_VIEW_LOWEST_ROLE_ALLOWED not in default_roles:
    raise ImproperlyConfigured(
        f"The env var FWEGO_PERSONAL_VIEW_LOWEST_ROLE_ALLOWED must be set to one of "
        f"the following values: {default_roles.keys()} but instead it is "
        f"{settings.FWEGO_PERSONAL_VIEW_LOWEST_ROLE_ALLOWED}. "
    )

default_roles[settings.FWEGO_PERSONAL_VIEW_LOWEST_ROLE_ALLOWED].append(
    CreateAndUsePersonalViewOperationType
)

default_roles[VIEWER_ROLE_UID].extend(
    default_roles[NO_ACCESS_ROLE_UID]
    + [
        ReadWorkspaceOperationType,
        ReadTeamOperationType,
        ListTeamsOperationType,
        ListApplicationsWorkspaceOperationType,
        ListTablesDatabaseTableOperationType,
        ReadApplicationOperationType,
        ReadDatabaseTableOperationType,
        ListRowsDatabaseTableOperationType,
        ReadDatabaseRowOperationType,
        ReadViewOperationType,
        ReadFieldOperationType,
        ListViewSortOperationType,
        ReadViewFieldOptionsOperationType,
        ReadViewDecorationOperationType,
        ListViewDecorationOperationType,
        ListViewFilterOperationType,
        ListViewsOperationType,
        ListFieldsOperationType,
        ListAggregationsViewOperationType,
        ReadAggregationsViewOperationType,
        ReadAdjacentRowDatabaseRowOperationType,
        ListRowNamesDatabaseTableOperationType,
        ReadViewFilterOperationType,
        ListenToAllDatabaseTableEventsOperationType,
        ReadViewsOrderOperationType,
        ReadViewSortOperationType,
        ListViewGroupByOperationType,
        ReadViewGroupByOperationType,
        ListBuilderWorkflowActionsPageOperationType,
        ReadBuilderWorkflowActionOperationType,
        ReadViewFilterGroupOperationType,
        ReadWidgetOperationType,
        ListWidgetsOperationType,
        ListDashboardDataSourcesOperationType,
        ReadDashboardDataSourceOperationType,
        DispatchDashboardDataSourceOperationType,
    ]
)
default_roles[COMMENTER_ROLE_UID].extend(
    default_roles[VIEWER_ROLE_UID]
    + [
        CreateRowCommentsOperationType,
        DeleteRowCommentsOperationType,
        ReadRowCommentsOperationType,
        RestoreRowCommentOperationType,
        UpdateRowCommentsOperationType,
        ReadDatabaseRowHistoryOperationType,
    ]
)
default_roles[EDITOR_ROLE_UID].extend(
    default_roles[COMMENTER_ROLE_UID]
    + [
        CreateRowDatabaseTableOperationType,
        UpdateDatabaseRowOperationType,
        DeleteDatabaseRowOperationType,
        ExportTableOperationType,
        MoveRowDatabaseRowOperationType,
        ImportRowsDatabaseTableOperationType,
        ListWorkspaceUsersWorkspaceOperationType,
        RestoreDatabaseRowOperationType,
        ListTeamSubjectsOperationType,
        ReadTeamSubjectOperationType,
    ]
)
default_roles[BUILDER_ROLE_UID].extend(
    default_roles[EDITOR_ROLE_UID]
    + [
        CreatePageOperationType,
        DeletePageOperationType,
        UpdatePageOperationType,
        UpdateThemeOperationType,
        DuplicatePageOperationType,
        CreateTableDatabaseTableOperationType,
        UpdateDatabaseTableOperationType,
        DeleteDatabaseTableOperationType,
        RestoreDatabaseTableOperationType,
        DeleteDatabaseRowOperationType,
        CreateViewOperationType,
        CreateFieldOperationType,
        UpdateViewDecorationOperationType,
        TestTriggerWebhookOperationType,
        ListTableWebhooksOperationType,
        DuplicateFieldOperationType,
        CreateViewDecorationOperationType,
        DeleteFieldOperationType,
        DeleteRelatedLinkRowFieldOperationType,
        RestoreFieldOperationType,
        UpdateFieldOperationType,
        TypeFormulaOperationType,
        RunAirtableImportJobOperationType,
        UpdateViewOperationType,
        DeleteViewOperationType,
        RestoreViewOperationType,
        DuplicateViewOperationType,
        UpdateWebhookOperationType,
        CreateViewFilterOperationType,
        CreateViewFilterGroupOperationType,
        UpdateViewFilterGroupOperationType,
        DeleteViewFilterGroupOperationType,
        UpdateViewFilterOperationType,
        DeleteViewFilterOperationType,
        DeleteViewDecorationOperationType,
        CreateWebhookOperationType,
        DeleteWebhookOperationType,
        ReadWebhookOperationType,
        OrderViewsOperationType,
        UpdateViewFieldOptionsOperationType,
        CreateApplicationsWorkspaceOperationType,
        DeleteViewSortOperationType,
        UpdateViewSlugOperationType,
        CreatePublicViewOperationType,
        UpdateViewPublicOperationType,
        DeleteApplicationOperationType,
        RestoreApplicationOperationType,
        ReadApplicationTrashOperationType,
        DuplicateApplicationOperationType,
        UpdateApplicationOperationType,
        UpdateViewSortOperationType,
        DuplicateDatabaseTableOperationType,
        CreateViewSortOperationType,
        CreateViewGroupByOperationType,
        UpdateViewGroupByOperationType,
        DeleteViewGroupByOperationType,
        ReadWorkspaceTrashOperationType,
        CreateTokenOperationType,
        ReadTokenOperationType,
        UpdateTokenOperationType,
        UseTokenOperationType,
        OrderTablesDatabaseTableOperationType,
        OrderApplicationsOperationType,
        CreateElementOperationType,
        UpdateElementOperationType,
        DeleteElementOperationType,
        ReadElementOperationType,
        ListElementsPageOperationType,
        OrderElementsPageOperationType,
        CreateDomainOperationType,
        DeleteDomainOperationType,
        ReadDomainOperationType,
        UpdateDomainOperationType,
        PublishDomainOperationType,
        CreateIntegrationOperationType,
        DeleteIntegrationOperationType,
        ListIntegrationsApplicationOperationType,
        OrderIntegrationsOperationType,
        ReadIntegrationOperationType,
        UpdateIntegrationOperationType,
        CreateDataSourceOperationType,
        DeleteDataSourceOperationType,
        ListDataSourcesPageOperationType,
        OrderDataSourcesPageOperationType,
        ReadDataSourceOperationType,
        UpdateDataSourceOperationType,
        DispatchDataSourceOperationType,
        DispatchBuilderWorkflowActionOperationType,
        DeleteBuilderWorkflowActionOperationType,
        CreateBuilderWorkflowActionOperationType,
        CreateUserSourceOperationType,
        DeleteUserSourceOperationType,
        ListUserSourcesApplicationOperationType,
        ReadUserSourceOperationType,
        UpdateUserSourceOperationType,
        OrderUserSourcesOperationType,
        AuthenticateUserSourceOperationType,
        LoginUserSourceOperationType,
        ReadPageOperationType,
        ListPagesBuilderOperationType,
        OrderPagesBuilderOperationType,
        ListDomainsBuilderOperationType,
        OrderDomainsBuilderOperationType,
        UpdateBuilderWorkflowActionOperationType,
        OrderBuilderWorkflowActionOperationType,
        SyncTableOperationType,
        ListPropertiesOperationType,
        GetIncludingPublicValuesOperationType,
        CreateWidgetOperationType,
        UpdateWidgetOperationType,
        DeleteWidgetOperationType,
        CreateDashboardDataSourceOperationType,
        DeleteDashboardDataSourceOperationType,
        UpdateDashboardDataSourceOperationType,
    ]
)
default_roles[ADMIN_ROLE_UID].extend(
    default_roles[BUILDER_ROLE_UID]
    + [
        UpdateWorkspaceOperationType,
        DeleteWorkspaceOperationType,
        DeleteDatabaseRowOperationType,
        ReadInvitationWorkspaceOperationType,
        AssignRoleWorkspaceOperationType,
        ReadRoleWorkspaceOperationType,
        DeleteWorkspaceUserOperationType,
        DeleteWorkspaceInvitationOperationType,
        UpdateWorkspaceUserOperationType,
        CreateInvitationsWorkspaceOperationType,
        ListInvitationsWorkspaceOperationType,
        UpdateWorkspaceInvitationType,
        CreateTeamOperationType,
        UpdateTeamOperationType,
        DeleteTeamOperationType,
        CreateTeamSubjectOperationType,
        DeleteTeamSubjectOperationType,
        RestoreTeamOperationType,
        RestoreWorkspaceOperationType,
        EmptyApplicationTrashOperationType,
        EmptyWorkspaceTrashOperationType,
        ReadRoleTableOperationType,
        UpdateRoleTableOperationType,
        ReadRoleApplicationOperationType,
        UpdateRoleApplicationOperationType,
        CreateSnapshotApplicationOperationType,
        RestoreApplicationSnapshotOperationType,
        ListSnapshotsApplicationOperationType,
        DeleteApplicationSnapshotOperationType,
        RestoreDomainOperationType,
        ListWorkspaceAuditLogEntriesOperationType,
    ]
)
