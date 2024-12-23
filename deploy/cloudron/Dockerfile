ARG FROM_IMAGE=digitranslab/fwego:1.30.1
# This is pinned as version pinning is done by the CI setting FROM_IMAGE.
# hadolint ignore=DL3006
FROM $FROM_IMAGE as image_base

# We need to move the conf at build time due to cloudrons readonly filesystem.
RUN apt-get remove -y "postgresql-$POSTGRES_VERSION" && \
    mv /fwego/supervisor/includes/disabled/embedded-redis.conf /fwego/supervisor/includes/enabled/embedded-redis.conf

COPY deploy/cloudron/cloudron_env.sh /fwego/supervisor/env/cloudron_env.sh
