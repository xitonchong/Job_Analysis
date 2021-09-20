FROM jupyter/scipy-notebook


USER root

COPY requirements.txt /tmp/
RUN apt-get update &&  \
    pip install --requirement /tmp/requirements.txt  


USER 1000

