FROM python:3.10.12-bullseye
WORKDIR /app
RUN apt-get update && apt-get install -y \
  && rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install --upgrade pip
COPY ./app /app
RUN pip install -r requirements

