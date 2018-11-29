# Pythonは公式イメージ
FROM python:3.7

LABEL  maintainer "nnashiki <n.nashiki.work@gmail.com>"

COPY main /main

WORKDIR main

RUN pip install --upgrade pip
RUN pip install pipenv

COPY main/Pipfile Pipfile

ARG UPDATE_LOCK
RUN if [ -z "$UPDATE_LOCK" ]; then pipenv install --system --deploy\
    else pipenv install --system --skip-lock;fi


