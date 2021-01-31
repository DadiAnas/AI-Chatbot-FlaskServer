FROM python:3.7.9-slim

COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN chmod +x gunicorn_starter.sh


ENTRYPOINT ["./gunicorn_starter.sh"]