FROM ubuntu:18.10

RUN apt-get update

RUN apt-get install -y python3-dev python3-pip

WORKDIR /app

COPY . .

RUN python3 setup.py install


