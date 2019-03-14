FROM python:3.6-alpine
MAINTAINER ExcelE

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# Installing Postgres and its dependencies
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-dev \
    gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt
# Removing Postgres dependencies, minimizing the container
RUN apk del .tmp-build-dev

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user