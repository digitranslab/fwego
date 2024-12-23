# This a dev image for testing your plugin when installed into the Fwego backend image
FROM fwego/backend:1.30.1 as base

FROM fwego/backend:1.30.1

USER root

ARG PLUGIN_BUILD_UID
ENV PLUGIN_BUILD_UID=${PLUGIN_BUILD_UID:-9999}
ARG PLUGIN_BUILD_GID
ENV PLUGIN_BUILD_GID=${PLUGIN_BUILD_GID:-9999}

# If we aren't building as the same user that owns all the files in the base
# image/installed plugins we need to chown everything first.
COPY --from=base --chown=$PLUGIN_BUILD_UID:$PLUGIN_BUILD_GID /fwego /fwego
RUN groupmod -g $PLUGIN_BUILD_GID fwego_docker_group && usermod -u $PLUGIN_BUILD_UID $DOCKER_USER

# Install your dev dependencies manually.
COPY --chown=$PLUGIN_BUILD_UID:$PLUGIN_BUILD_GID ./plugins/{{ cookiecutter.project_module }}/backend/requirements/dev.txt /tmp/plugin-dev-requirements.txt
RUN . /fwego/venv/bin/activate && pip3 install -r /tmp/plugin-dev-requirements.txt

COPY --chown=$PLUGIN_BUILD_UID:$PLUGIN_BUILD_GID ./plugins/{{ cookiecutter.project_module }}/ $FWEGO_PLUGIN_DIR/{{ cookiecutter.project_module }}/
RUN /fwego/plugins/install_plugin.sh --folder $FWEGO_PLUGIN_DIR/{{ cookiecutter.project_module }} --dev

USER $PLUGIN_BUILD_UID:$PLUGIN_BUILD_GID
ENV DJANGO_SETTINGS_MODULE='fwego.config.settings.dev'
CMD ["django-dev"]
