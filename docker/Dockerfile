FROM python:3.7-slim

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /var/www/code
WORKDIR /var/www/code

COPY ./requirements.txt /var/www/code/requirements.txt
RUN pip install -r requirements.txt

COPY . /var/www/code/