FROM python:3.10

WORKDIR /app

COPY tests /app/tests
COPY Pipfile /app
COPY Pipfile.lock /app
COPY asgi.py /app
COPY .env /app/.env
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install psycopg2-binary
RUN pipenv install --system --deploy --ignore-pipfile --${PIPENV_ARGS}

RUN cat /etc/ssl/certs/ca-certificates.crt >> `python -m certifi`

COPY api/ /app/api
COPY entrypoint.sh /app/entrypoint.sh

EXPOSE 8080
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["uvicorn", "asgi:api", "--host", "0.0.0.0", "--port", "8080"]