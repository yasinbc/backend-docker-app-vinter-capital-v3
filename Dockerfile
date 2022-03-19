FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3.9 python3.9-dev curl python3.9-distutils postgresql-client-12 

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

RUN python3.9 get-pip.py

ENV PYTHONUNBUFFERED 1



# syntax=docker/dockerfile:1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/