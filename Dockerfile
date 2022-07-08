FROM python:3.9-slim-buster

ENV FLASK_APP=python-api/app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . ./python-api

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000"]


