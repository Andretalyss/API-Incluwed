FROM python:3.8.3-slim-buster

WORKDIR /usr/src/app

RUN apt-get update

RUN pip install Flask && \
    pip install psycopg2-binary && \
    pip install python-dotenv && \
    pip install bcrypt && \
    pip install pyjwt && \
    pip install gunicorn

COPY main.py main.py
COPY config/ config
COPY src/ src

CMD ["gunicorn","-w", "2", "-b", "0.0.0.0:8000", "main:api", "--log-level", "debug"]