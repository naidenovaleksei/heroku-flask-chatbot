# https://hub.docker.com/_/python
FROM python:3.8-slim

WORKDIR /app
COPY heroku-flask-chatbot/* ./
COPY deploy/* ./
RUN pip install --no-cache-dir -r requirements.txt

CMD /app/entypoint.sh