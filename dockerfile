FROM python:3.13


ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt