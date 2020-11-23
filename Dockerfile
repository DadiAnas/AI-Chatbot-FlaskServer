# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.8.0
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]