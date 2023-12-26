FROM python:3-alpine3.9

WORKDIR /usr/src/app

RUN apk upgrade && apk add --no-cache --virtual .build-deps

RUN pip install Flask && \
    pip install psycopg2-binary && \
    pip install psycopg2 && \
    pip install requests && \
    pip install redis && \
    pip install boto3 && \
    apk --purge del .build-deps

COPY main.py main.py
COPY routes/ routes

CMD ["python3", "main.py"]
