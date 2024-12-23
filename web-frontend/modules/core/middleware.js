import settings from '@fwego/modules/core/middleware/settings'
import authentication from '@fwego/modules/core/middleware/authentication'
import authenticated from '@fwego/modules/core/middleware/authenticated'
import staff from '@fwego/modules/core/middleware/staff'
import workspacesAndApplications from '@fwego/modules/core/middleware/workspacesAndApplications'
import pendingJobs from '@fwego/modules/core/middleware/pendingJobs'
import urlCheck from '@fwego/modules/core/middleware/urlCheck'
import impersonate from '@fwego/modules/core/middleware/impersonate'

/* eslint-disable-next-line */
import Middleware from './middleware'

Middleware.settings = settings
Middleware.authentication = authentication
Middleware.authenticated = authenticated
Middleware.staff = staff
Middleware.workspacesAndApplications = workspacesAndApplications
Middleware.pendingJobs = pendingJobs
Middleware.urlCheck = urlCheck
Middleware.impersonate = impersonate
