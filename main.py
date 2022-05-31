from uvicorn import run
from fastapi import FastAPI
from elasticsearch import Elasticsearch
from pydantic import BaseModel
from os import environ

app = FastAPI()


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
