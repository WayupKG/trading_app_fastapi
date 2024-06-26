FROM python:3.12 as python-base

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

RUN mkdir app

WORKDIR  /app

COPY /pyproject.toml /app

RUN poetry install

COPY . .

