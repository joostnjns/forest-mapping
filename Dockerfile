# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

RUN mkdir /app

ENV POETRY_VERSION=1.1.13 \
    POETRY_VIRTUALENVS_CREATE=false

# Install SSH 
RUN apt-get update && apt-get install -y openssh-client

# Install Git
RUN apt-get update \
    && apt-get install -y git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY poetry.lock /app
COPY pyproject.toml /app
COPY README.md /app 

# Copy Python code to the Docker image
COPY forest_mapping/ /app/forest_mapping/

# Install poetry
RUN pip3 install "poetry==1.3.2"
RUN poetry config virtualenvs.create false

# Project initialization:
RUN poetry install --no-interaction

CMD [ "python", "/app/forest_mapping/foo.py"]