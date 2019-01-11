PYTHON_FILE := $(PYTHON_FILE)

USER_GH_NAME = nnashiki
IMAGE_NAME = python_application
IMAGE_NAME_BASE = $(IMAGE_NAME)_base
IMAGE_NAME_PIPENV = $(IMAGE_NAME)_pipenv
CONTAINER_NAME = python_application

# -------------------
# アプリケーションビルド

application-build-base:
	docker build . -f docker/Dockerfile_base\
	 --build-arg GITHUB_USER=$(USER_GH_NAME)\
	 --build-arg GITHUB_TOKEN=$(GH_TOKEN)\
	 -t $(IMAGE_NAME_BASE):0.1

application-build: application-build-base
	docker build . -f docker/Dockerfile\
	 -t $(IMAGE_NAME):0.1

application-build-no-cache:
	docker build . -f docker/Dockerfile\
	 --no-cache \
	 -t $(IMAGE_NAME):0.1

# -------------------
# pipenv.lock を更新

application-build-update-dependency: application-build-base
	docker build . -f docker/Dockerfile_update_dependency\
	 -t $(IMAGE_NAME):0.1

application-update-dependency: application-build-update-dependency
	docker run -it --rm --name $(CONTAINER_NAME) \
	-v `pwd`/main:/main \
	$(IMAGE_NAME):0.1 \
	pipenv lock

# -------------------
# pipenv-gragh

application-build-pipenv-gragh: application-build-base
	docker build . -f docker/Dockerfile_pipenv_gragh\
	 --no-cache \
	 -t $(IMAGE_NAME_PIPENV):0.1

application-graph: application-build-pipenv-gragh
	docker run -it --rm --name $(CONTAINER_NAME) \
	-v `pwd`/main:/main \
	$(IMAGE_NAME_PIPENV):0.1 \
	pipenv graph


application-bash: application-build
	docker run -it --rm --name $(CONTAINER_NAME) \
	-v `pwd`/main:/main \
	$(IMAGE_NAME):0.1 \
	bash

application-run: application-build
	docker run -it --rm --name $(CONTAINER_NAME) \
	-v `pwd`/main:/main \
	$(IMAGE_NAME):0.1 \
	python $(PYTHON_FILE)

application-test: application-build
	docker run -it --rm --name $(CONTAINER_NAME) \
	-v `pwd`/main:/main \
	$(IMAGE_NAME):0.1 \
	python test.py

