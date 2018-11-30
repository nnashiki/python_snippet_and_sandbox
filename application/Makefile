PYTHON_FILE := $(PYTHON_FILE)

USER_GH_NAME = nnashiki
IMAGE_NAME = python_application
CONTAINER_NAME = python_application

application-build:
	docker build . --build-arg GITHUB_USER=$(USER_GH_NAME)\
	 --build-arg GITHUB_TOKEN=$(GH_TOKEN)\
	 -t $(IMAGE_NAME):0.1

application-build-update-dependency:
	docker build . --build-arg GITHUB_USER=$(USER_GH_NAME)\
	 --build-arg GITHUB_TOKEN=$(GH_TOKEN)\
	 --build-arg UPDATE_LOCK=1\
	 -t $(IMAGE_NAME):0.1

application-build-no-cache:
	docker build . --no-cache \
	 --build-arg GITHUB_USER=$(USER_GH_NAME)\
	 --build-arg GITHUB_TOKEN=$(GH_TOKEN)\
	 -t $(IMAGE_NAME):0.1

application-bash: application-build
	docker run -it --rm --name $(CONTAINER_NAME) \
	-v `pwd`/main:/main \
	$(IMAGE_NAME):0.1 \
	bash

application-update-dependency: application-build-update-dependency
	docker run -it --rm --name $(CONTAINER_NAME) \
	-v `pwd`/main:/main \
	$(IMAGE_NAME):0.1 \
	pipenv lock

application-run: application-build
	docker run -it --rm --name $(CONTAINER_NAME) \
	-v `pwd`/main:/main \
	$(IMAGE_NAME):0.1 \
	python $(PYTHON_FILE)
