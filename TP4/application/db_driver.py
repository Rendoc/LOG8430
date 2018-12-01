from pymongo import MongoClient
from bson.json_util import dumps
import json

client = MongoClient('localhost', 27017)
db = client["database"]
factures = db["factures"]

# KEYSPACE = 'factures_keyspace'
# cluster = Cluster()
# session = cluster.connect()
# session.row_factory = dict_factory

""" facture = {
    id,
    title,
    articles : [
        {id:,name:, qty}, ...
    ]
} """


def add_facture(obj):
    try:
        facture = {"id": obj["id"], "title": obj["title"],
                   "articles": obj["articles"]}
        factures.insert_one(facture)
    except Exception as e:
        print(e)


def get_factures():
    # print (factures.find())
    return dumps(factures.find())


def get_facture(id):
    return dumps(factures.find_one({"id": id}))


if __name__ == "__main__":
    main()
