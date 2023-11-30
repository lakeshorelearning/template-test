
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
from starlette_exporter import PrometheusMiddleware, handle_metrics
from starlette_exporter.optional_metrics import response_body_size, request_body_size

from log import logger
from config import Configuration
from etl import Extract, Transform, Load
import json

app = FastAPI(
    title= template-test.replace("-", " ").title(),
    description="",
    version="0.0.1",)

config = Configuration()

app.add_middleware(
    PrometheusMiddleware, 
    app_name=template-test,
    group_paths=True,
    optional_metrics=[response_body_size, request_body_size],
    skip_paths=['/health', "/readiness"],
    )
app.add_route("/metrics", handle_metrics)


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>Lakeshore Microservice</title>
        </head>
        <body>
            <h1>Lakeshore Data Engineering Microservice!</h1>
        </body>
    </html>
    """


@app.get("/readiness", tags=["Kubernetes"])
def is_ready():
    return {"ready": True}


@app.get("/health", tags=["Kubernetes"])
def is_alive():
    return {'healthy': True}


logger.info("\U0001F680 Worker launched!")