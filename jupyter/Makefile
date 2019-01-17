USER_GH_NAME =
JUPYTER_IMAGE_NAME = python_sand
JUPYTER_CONTAINER_NAME = python_sand

jupyter-build:
	docker build . --build-arg GITHUB_USER=$(USER_GH_NAME) --build-arg GITHUB_TOKEN=$(GH_TOKEN) --build-arg LOCAL_UID=`id -u $(USER)` --build-arg LOCAL_GID=`id -g $(USER)` -t $(JUPYTER_IMAGE_NAME):0.1

jupyter-build-no-cache:
	ls

jupyter-run: jupyter-build
	docker run -it --rm --name $(JUPYTER_CONTAINER_NAME) \
	-p 8888:8888 \
	-v `pwd`/note:/home/jovyan/work -v `pwd`/config:/home \
	--link baseball_db:baseball_db \
	 $(JUPYTER_IMAGE_NAME):0.1 \
	jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10

jupyter-bash: jupyter-build
	docker run -it --rm --name $(JUPYTER_CONTAINER_NAME) -p 7777:8888 \
	-v `pwd`/note:/home/jovyan/work -v `pwd`/config:/home \
	--link baseball_db:baseball_db \
	 $(JUPYTER_IMAGE_NAME):0.1 \
	 bash
