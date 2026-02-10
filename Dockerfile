FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code


COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt


RUN adduser --disabled-password --gecos "" django
USER django

COPY . /code/


CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]