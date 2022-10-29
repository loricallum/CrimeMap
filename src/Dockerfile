FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install GDAL and libpq dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev gdal-bin

RUN apt-get upgrade libpq-dev -y
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./localcrimesmap /app/