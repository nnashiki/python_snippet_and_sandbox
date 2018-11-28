USER_GH_NAME =
APPLICATION_IMAGE_NAME = python_application
APPLICATION_CONTAINER_NAME = python_application

application-build:
	docker build . --build-arg GITHUB_USER=$(USER_GH_NAME) --build-arg GITHUB_TOKEN=$(GH_TOKEN) --build-arg LOCAL_UID=`id -u $(USER)` --build-arg LOCAL_GID=`id -g $(USER)` -t $(APPLICATION_IMAGE_NAME):0.1

jupyter-build-no-cache:
	ls

application-run: application-build
	docker run -it --rm --name $(APPLICATION_CONTAINER_NAME) \
	 $(APPLICATION_CONTAINER_NAME):0.1 \
	bash
