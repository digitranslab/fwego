# This a dev image for testing your plugin when installed into the Fwego web-frontend image
FROM fwego/web-frontend:1.30.1 as base
FROM fwego/web-frontend:1.30.1

USER root

ARG PLUGIN_BUILD_UID
ENV PLUGIN_BUILD_UID=${PLUGIN_BUILD_UID:-9999}
ARG PLUGIN_BUILD_GID
ENV PLUGIN_BUILD_GID=${PLUGIN_BUILD_GID:-9999}

# If we aren't building as the same user that owns all the files in the base
# image/installed plugins we need to chown everything first.
COPY --from=base --chown=$PLUGIN_BUILD_UID:$PLUGIN_BUILD_GID /fwego /fwego
RUN groupmod -g $PLUGIN_BUILD_GID node && usermod -u $PLUGIN_BUILD_UID $DOCKER_USER

COPY --chown=$PLUGIN_BUILD_UID:$PLUGIN_BUILD_GID ./plugins/{{ cookiecutter.project_module }}/ $FWEGO_PLUGIN_DIR/{{ cookiecutter.project_module }}/
RUN /fwego/plugins/install_plugin.sh --folder $FWEGO_PLUGIN_DIR/{{ cookiecutter.project_module }} --dev

USER $PLUGIN_BUILD_UID:$PLUGIN_BUILD_GID
CMD ["nuxt-dev"]
