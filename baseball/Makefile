SHELL=/bin/bash

IMAGE_NAME = python_37_app
CONTAINER_NAME = ${IMAGE_NAME}

# appのイメージ
app-update-depedencies:
	echo '' > requirements.lock
	docker build . -f docker/Dockerfile \
	--build-arg UPDATE_LOCK=1 --no-cache -t ${CONTAINER_NAME}
	docker run -it --rm ${CONTAINER_NAME} pip freeze > requirements.lock

app-build:
	docker build . -f docker/Dockerfile -t ${CONTAINER_NAME}

app-bash:
	docker run -it --rm ${CONTAINER_NAME}

app-abe:
	docker run -it --rm -p 5050:5050  python_37_app python3 api/app3.py

app-bokeh-js:
	docker run -it --rm -p 5050:5050  python_37_app python3 api/bokeh_js.py
