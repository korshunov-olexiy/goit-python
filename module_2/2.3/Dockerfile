# syntax=docker/dockerfile:1
FROM python:3.9.9-slim-buster
WORKDIR /
COPY src/ .
RUN python3 -m venv env
RUN . ./env/bin/activate
RUN pip3 install -r /src/personal_manager/requirements.txt
ADD pyproject.toml /
ADD setup.cfg /
ADD MANIFEST.in /
RUN python3 -m pip install build
RUN python3 -m build
RUN python3 -m pip install dist/personal-manager-0.7.tar.gz
ADD start.sh /
RUN chmod +x /start.sh
CMD [ "/start.sh" ]
