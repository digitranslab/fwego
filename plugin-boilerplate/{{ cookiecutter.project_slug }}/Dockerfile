FROM digitranslab/fwego:1.30.1

COPY ./plugins/{{ cookiecutter.project_module }}/ /fwego/plugins/{{ cookiecutter.project_module }}/
RUN /fwego/plugins/install_plugin.sh --folder /fwego/plugins/{{ cookiecutter.project_module }}
