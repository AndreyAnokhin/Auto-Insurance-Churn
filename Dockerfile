FROM python:3.6
LABEL maintainer='Andrey Anokhin'
RUN apt-get update -y
RUN pip install pipenv
COPY . /app
WORKDIR /app
RUN pipenv lock --requirements > requirements.txt
RUN pip3 install -r requirements.txt
ENTRYPOINT  gunicorn --bind 0.0.0.0:5000 app:app
