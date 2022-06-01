def es_body():
    body = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 3,
            "analysis": {
                "tokenizer": {
                    "nori_mixed": {
                        "type": "nori_tokenizer",
                        "decompound_mode": "mixed"
                    },
                    "nori_discard": {
                        "type": "nori_tokenizer",
                        "decompound_mode": "discard"
                    }
                },
                "analyzer": {
                    "index_analyzer": {
                        "type": "custom",
                        "tokenizer": "nori_mixed"
                    },
                    "search_analyzer": {
                        "type": "custom",
                        "tokenizer": "nori_discard"
                    }
                }
            }
        },

        "mappings": {
            "properties": {
                "id": {
                    "type": "keyword",
                    "index": False
                },
                "date": {"type": "date"},
                "author": {"type": "keyword"},
                "directory": {"type": "keyword"},
                "title": {
                    "type": "text",
                    "analyzer": "index_analyzer",
                    "search_analyzer": "search_analyzer"
                },
                "text": {
                    "type": "text",
                    "analyzer": "index_analyzer",
                    "search_analyzer": "search_analyzer"
                }
            }
        }
    }
    return body


def es_create(index_name, es):
    if not es.indices.exists(index=index_name):
        result = es.indices.create(index=index_name, body=es_body())
        return result["acknowledged"]
    return True


