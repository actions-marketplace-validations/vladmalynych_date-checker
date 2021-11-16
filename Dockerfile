FROM python:3.8-alpine

ENV TZ=Europe/Prague
ENV LC_ALL=C.UTF-8

RUN apk add --no-cache tzdata && \
    python3 -m pip install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir python-dateutil==2.8.1

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY src/ /app/

WORKDIR /app
ENTRYPOINT ["date"]
