FROM jupyter/datascience-notebook

ARG GITHUB_USER
ARG GITHUB_TOKEN
ARG LOCAL_UID
ARG LOCAL_GID

LABEL maintainer "nashiki <niten.nashiki@sensy.ai>"

# pythonモジュールのinstall
RUN pip install -U pip \
    pathlib \
    pandas-gbq \
    tqdm \
    ipywidgets

# 日本語フォントを入れる
ENV HOME="/home/jovyan"
RUN mkdir addfont
WORKDIR addfont
RUN curl -L  "https://oscdl.ipa.go.jp/IPAexfont/ipaexg00301.zip" > font.zip && \
    unzip font.zip && \
    cp ipaexg00301/ipaexg.ttf /opt/conda/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/ipaexg.ttf && \
    echo "font.family : IPAexGothic" >>  /opt/conda/lib/python3.6/site-packages/matplotlib/mpl-data/matplotlibrc
WORKDIR $HOME
RUN rm -r ./.cache

# CSSの調整
COPY override.css /opt/conda/lib/python3.6/site-packages/notebook/static/notebook/css/override.css

# 拡張機能管理
RUN conda install -y -c conda-forge jupyter_contrib_nbextensions

WORKDIR work

# マウント書き込みエラー対策
USER root
RUN usermod -u ${LOCAL_UID} -o jovyan
RUN groupmod -g ${LOCAL_GID} users; exit 0
USER jovyan


