# Pythonは公式イメージ
FROM python:3.7

LABEL  maintainer "nnashiki <n.nashiki.work@gmail.com>"

COPY main /main
WORKDIR main

RUN pip install --upgrade pip && pip --version
RUN pip install pipenv && pipenv --version

COPY main/Pipfile Pipfile
COPY main/Pipfile.lock Pipfile.lock

ARG UPDATE_LOCK
RUN pipenv install --system



