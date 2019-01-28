FROM python:3.7

LABEL  maintainer="nnashiki <n.nashiki.work@gmail.com>"

ARG UPDATE_LOCK

WORKDIR /usr/src/app

COPY requirements.txt requirements.lock ./

RUN if [ -z "$UPDATE_LOCK" ]; then pip install --no-cache-dir -r requirements.lock; fi
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["/bin/bash"]
