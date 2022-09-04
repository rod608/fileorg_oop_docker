# Dockerfile, Image, Container
FROM python:3.10.0-buster
WORKDIR /root
COPY requirements.txt .
COPY . /root/home
ENV PATH="/home/myuser/.local/bin:${PATH}"
RUN apt-get update &&\
    /usr/local/bin/python3 -m pip install --upgrade pip &&\
    /usr/local/bin/python3 -m pip install -r requirements.txt &&\
    mkdir Documents &&\
    mkdir Desktop &&\
    pytest -vv