def update_data(data, index, es):
    body = {
        "doc": {
            "author": data.author,
            "title": data.title,
            "text": data.text,
            "directory": data.directory
        }
    }
    result = es.update(index=index, id=data.id, body=body)
    if result["_shards"]["failed"] == 0:
        return True
    return False


def delete_data(_id, index, es):
    result = es.delete(index=index, id=_id)
    if result["_shards"]["failed"] == 0:
        return True
    return False
