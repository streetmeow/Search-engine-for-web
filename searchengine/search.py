def search_data(data, index, es):
    body = {"size": data.size, "query": {"bool": {}}}
    if data.author is not None or data.directory is not None or data.gte is not None or data.lte is not None:
        body["query"]["bool"]["filter"] = []
        if data.author is not None:
            body["query"]["bool"]["filter"].append({"term": {"author": data.author}})
        if data.directory is not None:
            body["query"]["bool"]["filter"].append({"term": {"directory": data.directory}})
        if data.gte is not None or data.lte is not None:
            body["query"]["bool"]["filter"].append({"range": {"date": {"gte": data.gte, "lte": data.lte}}})
    if data.title is not None or data.text is not None:
        body["query"]["bool"]["should"] = []
        if data.title is not None:
            title_dict = {
                "match": {
                    "title": {
                        "query": data.title,
                        "boost": 2
                    }
                }
            }
            body["query"]["bool"]["should"].append(title_dict)
        if data.text is not None:
            text_dict = {
                "match": {
                    "text": {
                        "query": data.text,
                        "boost": 1
                    }
                }
            }
            body["query"]["bool"]["should"].append(text_dict)
    result = es.search(index=index, body=body)
    return [item["_source"] for item in result["hits"]["hits"]]
