# Pull base image
FROM python:3.8

#setting environment variables
# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /code/

#ENTRYPOINT celery -A tasks worker --loglevel=info