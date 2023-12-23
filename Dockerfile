FROM python:3.9-alpine3.13
LABEL maintainer="iamincognito123.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
# creates a virtual environment
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip &&\
    /py/bin/pip install -r /tmp/requirements.txt &&\
    # shell script command
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    # remove contents to save space
    rm -rf /tmp && \
    # creates a user without pass/home directory to enhance security
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user