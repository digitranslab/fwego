# syntax = docker/dockerfile:1.3
FROM debian:bookworm-slim as base

ARG UID
ENV UID=${UID:-9999}
ARG GID
ENV GID=${GID:-9999}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# We might be running as a user which already exists in this image. In that situation
# Everything is OK and we should just continue on.
RUN groupadd -g $GID fwego_docker_group || exit 0
RUN useradd --shell /bin/bash -u $UID -g $GID -o -c "" -m fwego_docker_user -l || exit 0
ENV DOCKER_USER=fwego_docker_user
ENV POSTGRES_VERSION=15
ENV FWEGO_IMAGE_TYPE="backend"

RUN apt-get update &&  \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    lsb-release \
    ca-certificates \
    curl \
    gnupg2 \
    libpq-dev \
    dos2unix \
    tini \
    && \
    # Postgresql repository has to be added manually to get pre-13 versions.
    echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && \
    apt-get update && \
    apt-get install --no-install-recommends -y \
    postgresql-client-$POSTGRES_VERSION \
    gettext \
    procps \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv\
    git \
    gosu \
    xmlsec1 \
    && apt-get autoclean \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

USER $UID:$GID

# In slim docker images, mime.types is removed and we need it for mimetypes guessing
COPY --chown=$UID:$GID ./backend/docker/mime.types /etc/

# Install non-dev base dependencies into a virtual env.
COPY --chown=$UID:$GID ./backend/requirements/base.txt /fwego/requirements/
RUN python3 -m venv /fwego/venv

ENV PIP_CACHE_DIR=/tmp/fwego_pip_cache
# hadolint ignore=SC1091,DL3042
RUN --mount=type=cache,mode=777,target=$PIP_CACHE_DIR,uid=$UID,gid=$GID . /fwego/venv/bin/activate && pip3 install  -r /fwego/requirements/base.txt

# Build a dev_deps stage which also has the dev dependencies for use by the dev layer.
FROM base as dev_deps

COPY ./backend/requirements/dev.txt /fwego/requirements/
# hadolint ignore=SC1091,DL3042
RUN --mount=type=cache,mode=777,target=$PIP_CACHE_DIR,uid=$UID,gid=$GID . /fwego/venv/bin/activate && pip3 install -r /fwego/requirements/dev.txt

# The core stage contains all of Fwegos source code and sets up the entrypoint
FROM base as core

# Copy over backend code.
COPY --chown=$UID:$GID ./docs /fwego/docs
# TODO - This copy also re-copies the requirements above, meaning this will be re-run
#        and not cached even though we already have separate layers above.
COPY --chown=$UID:$GID ./backend /fwego/backend
COPY --chown=$UID:$GID ./premium/backend /fwego/premium/backend
COPY --chown=$UID:$GID ./enterprise/backend /fwego/enterprise/backend

WORKDIR /fwego/backend

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

COPY --chown=$UID:$GID ./deploy/plugins/*.sh /fwego/plugins/

RUN dos2unix /fwego/backend/docker/docker-entrypoint.sh && \
    chmod a+x /fwego/backend/docker/docker-entrypoint.sh && \
    /fwego/venv/bin/pip install --no-cache-dir -e /fwego/backend/ && \
    /fwego/venv/bin/pip install --no-cache-dir -e /fwego/premium/backend/ && \
    /fwego/venv/bin/pip install --no-cache-dir -e /fwego/enterprise/backend/

HEALTHCHECK --interval=60s CMD ["/bin/bash", "/fwego/backend/docker/docker-entrypoint.sh", "backend-healthcheck"]
ENTRYPOINT ["/usr/bin/tini", "--", "/bin/bash", "/fwego/backend/docker/docker-entrypoint.sh"]

FROM core as dev

COPY --chown=$UID:$GID ./tests /fwego/tests/

USER root
RUN apt-get update &&  \
    apt-get install -y --no-install-recommends \
    graphviz apache2-utils \
    && apt-get autoclean \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*
USER $UID:$GID

# Override virtualenv with one containing dev dependencies.
COPY --chown=$UID:$GID --from=dev_deps /fwego/venv /fwego/venv

# Override env variables and initial cmd to start up in dev mode.
ENV DJANGO_SETTINGS_MODULE='fwego.config.settings.dev'
CMD ["django-dev"]

FROM core as local

ENV DJANGO_SETTINGS_MODULE='fwego.config.settings.base'
CMD ["gunicorn"]

