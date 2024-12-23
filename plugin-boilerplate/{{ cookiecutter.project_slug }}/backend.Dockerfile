FROM fwego/backend:1.30.1

USER root

COPY ./plugins/{{ cookiecutter.project_module }}/ $FWEGO_PLUGIN_DIR/{{ cookiecutter.project_module }}/
RUN /fwego/plugins/install_plugin.sh --folder $FWEGO_PLUGIN_DIR/{{ cookiecutter.project_module }}

USER $UID:$GID
