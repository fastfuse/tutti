FROM python:3.6-slim

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py
ENV DEBUG=True
ENV FLASK_ENV=development

EXPOSE 5000

ENTRYPOINT flask run --host=0.0.0.0 --port=5000
