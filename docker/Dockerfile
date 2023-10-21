FROM python:3.10
LABEL maintainer="ffoctopus@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

RUN python -m pip install --upgrade pip
RUN python -m pip install poetry
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi
