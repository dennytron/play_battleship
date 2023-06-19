FROM python:3.11

COPY requirements.txt /app/requirements.txt
RUN python3.11 -m pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app
