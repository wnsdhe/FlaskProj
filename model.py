import json


def load_db():
    with open("puppyList_db.json") as f:
        return json.load(f)


def get_url(l_json):
    url_list = []
    for i in l_json:
        url_list.append(i["url"])
    return url_list


db = load_db()
puppyUrlList = get_url(db)
