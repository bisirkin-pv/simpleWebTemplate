FROM python:3.9.1-slim-buster

WORKDIR /project
COPY . /project
RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app