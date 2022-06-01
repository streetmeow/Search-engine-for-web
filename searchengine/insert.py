from datetime import datetime
import pytz


def insert_data(_id, author, title, text, directory, index, es):
    tz = pytz.timezone("Asia/Seoul")
    date = datetime.now(tz)
    doc = {
        "id": _id,
        "date": date,
        "author": author,
        "title": title,
        "text": text,
        "directory": directory
    }
    result = es.index(index=index, body=doc)
    if result["_shards"]["failed"] == 0:
        return True
    else:
        return False
