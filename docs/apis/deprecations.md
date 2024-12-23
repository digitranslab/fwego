# Deprecations

## API deprecations

Fwego may, from time to time, deprecate functionality in its REST and/or Websocket 
API. To ensure that your application runs smoothly, and without downtime, we will use this
page to inform API integrators of what features are deprecated, and how long we'll
support compatibility for.


## PostgreSQL Database Deprecations

| Version | End of support       | Last Fwego version |
|---------|----------------------|----------------------|
| 12      | December 31, 2024    | 1.30.1               |
| 11      | March 31, 2024       | 1.24.0               |


**Note**: Fwego will stop creating images for PostgreSQL 11 starting with Fwego 
v1.30.1. It will always be possible to upgrade Postgres to version 15 following the 
instructions here:
[Upgrading postgresql from a previous version](../installation%2Finstall-with-docker.md#upgrading-postgresql-database-from-a-previous-version)
