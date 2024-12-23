FROM fwego

# Install dev dependencies manually.
COPY --chown=$UID:$GID ./backend/requirements/dev.txt /tmp/dev-requirements.txt
RUN . /fwego/venv/bin/activate && pip3 install -r /tmp/dev-requirements.txt

ENV FWEGO_ALL_IN_ONE_DEV_MODE='true'
