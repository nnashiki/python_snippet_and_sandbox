# Pythonは公式イメージ
FROM python_application_base:0.1

LABEL  maintainer="nnashiki <n.nashiki.work@gmail.com>"

COPY app /usr/src/app
WORKDIR /usr/src/app

COPY app/Pipfile Pipfile
COPY app/Pipfile.lock Pipfile.lock

# systemのpipを使うために、pipenv syncではなく --system --deploy を使用している
RUN set -x && \
    pipenv install --system --deploy
