from pymongo import MongoClient
from bson.json_util import dumps
import json

client = MongoClient('localhost', 27017)
db = client["conception"]
factures = db["factures"]

# KEYSPACE = 'factures_keyspace'
# cluster = Cluster()
# session = cluster.connect()
# session.row_factory = dict_factory

""" facture = {
    articles : [
        {name:,unit_price}, ...
    ]
} """


def add_facture(obj):
    print("obj db driver:"+dumps(obj))
    try:
        facture = {"articles": obj["articles"]}
        res = factures.insert_one(facture)
    except Exception as e:
        print(e)
    return res.inserted_id


def get_factures():
    # print (factures.find())
    return dumps(factures.find())


def get_facture(id):
    return dumps(factures.find_one({"id": id}))

if __name__ == "__main__":
    print(add_facture({"articles":[{"product_name":"arthur","product_price":12212}]}))
