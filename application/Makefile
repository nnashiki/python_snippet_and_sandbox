PYTHON_FILE := $(PYTHON_FILE)

USER_GH_NAME = nnashiki
IMAGE_NAME = python_application
IMAGE_NAME_BASE = $(IMAGE_NAME)_base
IMAGE_NAME_PIPENV = $(IMAGE_NAME)_pipenv
CONTAINER_NAME = python_application

# -------------------
# アプリケーションビルド

app-build-base:
	docker build . -f docker/Dockerfile_base\
	 --build-arg GITHUB_USER=$(USER_GH_NAME)\
	 --build-arg GITHUB_TOKEN=$(GH_TOKEN)\
	 -t $(IMAGE_NAME_BASE):0.1

app-build:
	docker build . -f docker/Dockerfile\
	 -t $(IMAGE_NAME):0.1

app-build-no-cache:
	docker build . -f docker/Dockerfile\
	 --no-cache \
	 -t $(IMAGE_NAME):0.1

# -------------------
# pipenv.lock を更新

app-build-update-dependency: app-build-base
	docker build . -f docker/Dockerfile_update_dependency\
	 -t $(IMAGE_NAME):0.1

app-update-dependency: app-build-update-dependency
	docker run -it --rm --name $(CONTAINER_NAME) \
	-v `pwd`/app:/usr/src/app \
	$(IMAGE_NAME):0.1 \
	pipenv lock --pre

# -------------------
# pipenv-gragh

app-build-pipenv-gragh: app-build-base
	docker build . -f docker/Dockerfile_pipenv_gragh\
	 --no-cache \
	 -t $(IMAGE_NAME_PIPENV):0.1

app-graph: app-build-pipenv-gragh
	docker run -it --rm --name $(CONTAINER_NAME) \
	-v `pwd`/app:/usr/src/app \
	$(IMAGE_NAME_PIPENV):0.1 \
	pipenv graph --json-tree > graph.json


app-bash: app-build
	docker run -it --rm --name $(CONTAINER_NAME) \
	-v `pwd`/app:/usr/src/app \
	$(IMAGE_NAME):0.1 \
	bash

app-run: app-build
	docker run -it --rm --name $(CONTAINER_NAME) \
	-v `pwd`/app:/usr/src/app \
	$(IMAGE_NAME):0.1 \
	python $(PYTHON_FILE)

responder-run: app-build
	- docker stop $(CONTAINER_NAME)
	docker run -it --rm \
	--name $(CONTAINER_NAME) \
	-v `pwd`/app:/usr/src/app \
	-p 5042:5042 \
	$(IMAGE_NAME):0.1 \
	python api/app.py

app-test: app-build
	docker run -it --rm --name $(CONTAINER_NAME) \
	-v `pwd`/app:/usr/src/app \
	$(IMAGE_NAME):0.1 \
	python test/test.py

