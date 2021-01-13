# https://hub.docker.com/_/python
FROM python:3.8-slim

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["/app/entry.sh"]