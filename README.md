<h1 align="center">Easy Search Engine</h1>
<p align="center">Search engine backend for easy build</p>

<h2 align="center">Description</h2>
해당 프로그램은 웹사이트 또는 블로그를 직접 구축하는 사람들이 쉽게 빠르고 정확한 게시글 검색엔진 백엔드를 구축하도록 해줍니다. 

<h2 align="center">Install</h2>
해당 엔진은 도커 설치를 지원합니다. 방법은 하단에 표시합니다. 

# 도커 설치
docker-compose.yml 파일을 우분투 임의의 디렉토리에 넣고 동일 디렉토리에서 아래의 명령어 차례대로 실행
```console
$ sudo docker-compose pull
$ sudo docker-compose -f docker-compose.yml up -d
```

# 직접 설치
직접 코드 수정을 희망하실 경우 하단의 라이브러리 및 프로그램을 설치 바랍니다. 

_⚠ Python 3.6+ 필수, Ubuntu 18.04+ 권장_



### 파이썬 패키지

#### [fastapi](https://pypi.org/project/fastapi/)
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

#### [pymysql](https://pypi.org/project/PyMySQL/)
This package contains a pure-Python MySQL client library, based on PEP 249.

#### [elasticsearch](https://pypi.org/project/elasticsearch/)
The official Python client for Elasticsearch.

#### [uvicorn](https://pypi.org/project/uvicorn/)
Uvicorn is an ASGI web server implementation for Python.

