# This a dev image for testing your plugin when installed into the Fwego all-in-one image
FROM digitranslab/fwego:1.30.1 as base

FROM digitranslab/fwego:1.30.1

ARG PLUGIN_BUILD_UID
ENV PLUGIN_BUILD_UID=${PLUGIN_BUILD_UID:-9999}
ARG PLUGIN_BUILD_GID
ENV PLUGIN_BUILD_GID=${PLUGIN_BUILD_GID:-9999}

# Use a multi-stage copy to quickly chown the contents of Fwego to match the user
# that will be running this image.
COPY --from=base --chown=$PLUGIN_BUILD_UID:$PLUGIN_BUILD_GID /fwego /fwego

RUN groupmod -g $PLUGIN_BUILD_GID fwego_docker_group && usermod -u $PLUGIN_BUILD_UID $DOCKER_USER

# Install your dev dependencies manually.
COPY --chown=$PLUGIN_BUILD_UID:$PLUGIN_BUILD_GID ./plugins/{{ cookiecutter.project_module }}/backend/requirements/dev.txt /tmp/plugin-dev-requirements.txt
RUN . /fwego/venv/bin/activate && pip3 install -r /tmp/plugin-dev-requirements.txt && chown -R $PLUGIN_BUILD_UID:$PLUGIN_BUILD_GID /fwego/venv

COPY --chown=$PLUGIN_BUILD_UID:$PLUGIN_BUILD_GID ./plugins/{{ cookiecutter.project_module }}/ $FWEGO_PLUGIN_DIR/{{ cookiecutter.project_module }}/
RUN /fwego/plugins/install_plugin.sh --folder $FWEGO_PLUGIN_DIR/{{ cookiecutter.project_module }} --dev

ENV FWEGO_ALL_IN_ONE_DEV_MODE='true'
