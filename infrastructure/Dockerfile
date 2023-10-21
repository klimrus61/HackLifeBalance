FROM python:3.11-alpine as builder-base

LABEL authors='Shorochov Lucky Klim' version=1.0

RUN apk update && apk add  gcc libffi-dev g++ py-pip --no-cache cargo

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip && pip install "poetry==1.6.1" && poetry config virtualenvs.create false && poetry install --no-cache --without dev

COPY ../backend ./