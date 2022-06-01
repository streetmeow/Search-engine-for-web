from uvicorn import run
from typing import Optional
from fastapi import FastAPI, Body
from elasticsearch import Elasticsearch
from pydantic import BaseModel
from os import environ
from searchengine import *

app = FastAPI(title="Easy Search Engine", description="Easy Search Engine for backend users", version="1.0.0")
es = Elasticsearch("http://0.0.0.0:9200")
index = "posts"
es_create(index_name=index, es=es)


class Insert(BaseModel):
    id: str
    author: str
    title: str
    text: str
    directory: str


class Search(BaseModel):
    author: Optional[str] = None
    title: Optional[str] = None
    text: Optional[str] = None
    directory: Optional[str] = None
    lte: Optional[str] = None
    gte: Optional[str] = None
    size: Optional[int] = 1


@app.get("/health/")
async def health_check():
    """
    헬스 체크. 정상 시 200 리턴
    """
    return 200


@app.post("/insert/")
async def insert_item(item: Insert = Body(
    example={
        "id": "unique 한 id 값 (data sync 를 위해 입력 받으며, update, delete 에 필요. str)",
        "author": "작성자",
        "title": "글 제목",
        "text": "글 내용",
        "directory": "글 위치 또는 카테고리"
    }
)):
    """
    검색값 추가
    return:
        성공 시 True, 실패 시 False
    """
    result = insert_data(_id=item.id, author=item.author, title=item.title, text=item.text, directory=item.directory,
                         index=index, es=es)
    return result


@app.post("/update/")
async def update_item(item: Insert = Body(
    example={
        "id": "unique 한 id 값 (data sync 를 위해 입력 받으며, update, delete 에 필요. str)",
        "author": "작성자",
        "title": "글 제목",
        "text": "글 내용",
        "directory": "글 위치 또는 카테고리"
    }
)):
    """
    기존값 업데이트. id 기준으로 수정하며, author, title, text, directory 모두 새로 입력해야 함
    return:
        성공 시 True, 실패 시 False
    """
    result = update_data(data=item, index=index, es=es)
    return result


@app.get("/delete/")
def delete_item(_id: str):
    """
    id 값 입력 시 해당 도큐먼트 삭제
    """
    result = delete_data(_id=_id, index=index, es=es)
    return result


@app.post("/search/")
async def search_item(data: Search = Body(
    example={
        "author": "작성자",
        "title": "글 제목",
        "text": "글 내용",
        "directory": "글 위치 또는 카테고리, str",
        "lte": "최대 날짜 (2020-02-02 등 날짜 포맷에 맞게 보낼 것, str)",
        "gte": "최소 날짜 (2020-02-02 등 날짜 포맷에 맞게 보낼 것, str)",
        "size": "검색 결과 최대 개수 제한 (default 1, integer)"
    }
)):
    """
    검색 진행. 모든 값은 필수가 아니며, 필요한 값만 보내면 됨
    :return:
        검색 결과 list
    """
    result = search_data(data=data, index=index, es=es)
    return result


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8080
    workers = 1
    run("main:app", host=host, port=port, reload=True, workers=workers)
