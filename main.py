from uvicorn import run
from fastapi import FastAPI
from elasticsearch import Elasticsearch
from pydantic import BaseModel
import pymysql
from os import environ
from searchengine import *

app = FastAPI()
es = Elasticsearch(environ.get("ES_HOST", "http://0.0.0.0:9200"))
es_create(index_name=environ.get("ES_INDEX", "posts"), es=es)


@app.get("/health/")
async def health_check():
    """
    헬스 체크. 정상 시 200 리턴
    """
    return 200


if __name__ == "__main__":
    host = environ.get("HOST", "0.0.0.0")
    port = int(environ.get("PORT", "8080"))
    workers = int(environ.get("WORKERS", "1"))
    run("main:app", host="0.0.0.0", port=port, reload=True, workers=workers)
