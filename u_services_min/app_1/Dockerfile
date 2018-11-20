FROM python:3.6-slim
RUN echo 'Dockerfile-App-1'
RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=__init__.py
EXPOSE 5001

ENTRYPOINT flask run --host=0.0.0.0 --port=5001
# ENTRYPOINT gunicorn -w 4 application:app -b 0.0.0.0:5001
