FROM gitpod/workspace-full

ADD requirements.txt .
RUN pip3 install -r requirements.txt
# Install custom tools, runtimes, etc.
# For example "bastet", a command-line tetris clone:
# RUN brew install bastet
#
# More information: https://www.gitpod.io/docs/config-docker/
