# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
FROM python:3.9.16-slim

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY ./app /app
RUN chmod +x /app/prestart.sh
RUN chmod +x /app/start.sh



RUN useradd --shell /bin/bash lakeshore
USER lakeshore


WORKDIR /app/

EXPOSE 8080

CMD ["/app/start.sh"]