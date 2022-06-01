<h1 align="center">Easy Search Engine</h1>
<p align="center">Search engine backend for easy build</p>

<h2 align="center">Description</h2>
해당 프로그램은 웹사이트 또는 블로그를 직접 구축하는 사람들이 쉽게 빠르고 정확한 게시글 검색엔진 백엔드를 구축하도록 해줍니다. 

<h2 align="center">설치 방법</h2>
해당 엔진은 부분적으로 도커 설치를 지원합니다. 방법은 하단에 표시합니다. 

docker-compose.yml 파일을 우분투 임의의 디렉토리에 넣고 동일 디렉토리에서 아래의 명령어 차례대로 실행
```console
$ sudo docker-compose pull
$ sudo docker-compose -f docker-compose.yml up -d
```
도커를 사용할 수 없는 경우, elasticsearch 7.15.0 버전과 kibana 동일 버전을 수동 설치해주시기 바랍니다.

그 다음, main.py 가 있는 디렉토리에서 아래 코드를 실행 바랍니다.

```console
$ python setup.py install
$ python main.py
```
main.py 실행 중 커넥션 에러가 날 수 있습니다. elasticsearch 가 실행되기 이전 실행했을 때의 에러일 확률이 높으니, 잠시 뒤 다시 시도해주시기 바랍니다.

default host 와 port는 0.0.0.0 과 8080입니다. 변경을 희망하실 경우 main.py 최하단의 아래의 코드를 수정 바랍니다.
```python
if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8080
    workers = 1
    run("main:app", host=host, port=port, reload=True, workers=workers)
```

### 파이썬 패키지

#### [fastapi](https://pypi.org/project/fastapi/)
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

#### [elasticsearch](https://pypi.org/project/elasticsearch/)
The official Python client for Elasticsearch.

#### [uvicorn](https://pypi.org/project/uvicorn/)
Uvicorn is an ASGI web server implementation for Python.

