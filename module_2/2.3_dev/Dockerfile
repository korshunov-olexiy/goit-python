# syntax=docker/dockerfile:1
FROM python:3.9.9-slim-buster
WORKDIR /
COPY src/ /src/
RUN pip3 install -r /src/personal_manager/requirements.txt
COPY pyproject.toml .
COPY setup.cfg .
COPY MANIFEST.in .
RUN python3 -m pip install build
RUN python3 -m build
RUN pip3 install dist/personal-manager-0.7.tar.gz
CMD [ "personal-manager" ]
