from datetime import datetime


def insert_data(_id, author, title, text, directory, index, es):
    date = datetime.now()
    doc = {
        "date": date,
        "author": author,
        "title": title,
        "text": text,
        "directory": directory
    }
    result = es.index(index=index, body=doc, id=_id)
    if result["_shards"]["failed"] == 0:
        return True
    else:
        return False
