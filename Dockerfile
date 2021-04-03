FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /tas

ADD . /tas

COPY ./requirements.txt /tas/requirements.txt

RUN pip install -r requirements.txt
COPY . /tas