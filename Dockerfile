FROM python:3
USER root

COPY requirements.txt .

RUN apt install ghostscript

RUN apt-get update && apt-get install -y \
  libpq-dev \
  libgl1-mesa-dev \
  && pip install --upgrade pip \
  && pip install -r requirements.txt


