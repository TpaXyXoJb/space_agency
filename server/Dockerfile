FROM python:3.9-slim AS server


RUN mkdir /server && apt update &&  apt install -y libmariadb-dev && apt-get install -y default-libmysqlclient-dev && apt-get install -y gcc

WORKDIR /server

COPY ./server/req.pip /server/
RUN pip install --upgrade pip && pip install -r req.pip

COPY ./server /server
