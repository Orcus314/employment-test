FROM python:latest
WORKDIR /ServerTest
COPY server.py /ServerTest/
COPY scrapper.py /ServerTest/
COPY updater.py /ServerTest/
COPY requirements.txt /ServerTest/
COPY init.sql /ServerTest/
RUN pip install -r requirements.txt