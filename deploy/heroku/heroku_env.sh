#!/bin/bash

set -euo pipefail

export FWEGO_PUBLIC_URL=${FWEGO_PUBLIC_URL:-https://$HEROKU_APP_NAME.herokuapp.com}
export FWEGO_CADDY_ADDRESSES=":$PORT"
export REDIS_URL=${REDIS_TLS_URL:-$REDIS_URL}
export DJANGO_SETTINGS_MODULE='fwego.config.settings.heroku'
export FWEGO_RUN_MINIMAL=yes
export DISABLE_EMBEDDED_PSQL=yes
export DISABLE_EMBEDDED_REDIS=yes
export SYNC_TEMPLATES_ON_STARTUP="${SYNC_TEMPLATES_ON_STARTUP:-false}"
export FWEGO_TRIGGER_SYNC_TEMPLATES_AFTER_MIGRATION=${FWEGO_TRIGGER_SYNC_TEMPLATES_AFTER_MIGRATION:-$SYNC_TEMPLATES_ON_STARTUP}
export MIGRATE_ON_STARTUP="${MIGRATE_ON_STARTUP:-false}"
# Heroku does not support mounting volumes!
export DISABLE_VOLUME_CHECK=yes

export FWEGO_AMOUNT_OF_WORKERS=${FWEGO_AMOUNT_OF_WORKERS:-1}
export FWEGO_AMOUNT_OF_GUNICORN_WORKERS=${FWEGO_AMOUNT_OF_GUNICORN_WORKERS:-$FWEGO_AMOUNT_OF_WORKERS}

# Disable auto https redirect because otherwise it will make Caddy bind on port 80.
# This is not allowed by Heroku, and will prevent it from starting.
export FWEGO_CADDY_GLOBAL_CONF="auto_https disable_redirects
http_port $PORT"

export EMAIL_SMTP="true"
export EMAIL_SMTP_USE_TLS=""
export FROM_EMAIL="no-reply@$MAILGUN_DOMAIN"

export EMAIL_SMTP_HOST=$MAILGUN_SMTP_SERVER
export EMAIL_SMTP_PORT=$MAILGUN_SMTP_PORT
export EMAIL_SMTP_USER=$MAILGUN_SMTP_LOGIN
export EMAIL_SMTP_PASSWORD=$MAILGUN_SMTP_PASSWORD
# Heroku generates a random user who runs this container, set DOCKER_USER to that user
# so we can setup the DATA_DIR.
DOCKER_USER=$(whoami)
export DOCKER_USER

# We must run the caddy user as the docker user to prevent supervisord errors
export FWEGO_CADDY_USER="${FWEGO_CADDY_USER:-$DOCKER_USER}"
