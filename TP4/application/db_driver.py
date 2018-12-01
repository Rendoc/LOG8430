from pymongo import MongoClient
from bson.json_util import dumps
import json

client = MongoClient('localhost', 27017)
db = client["database"]
factures = db["factures"]
#KEYSPACE = 'factures_keyspace'
#cluster = Cluster()
#session = cluster.connect()
#session.row_factory = dict_factory


def main():
    print()
    
def add_facture(facture):
    facture = { "id": facture.id, "title": facture.title }
    factures.insert_one(facture)


def get_factures():
    print(dumps(factures.find()))
    #print (factures.find())
    return factures.find()


def get_facture(id):
    return factures.find_one({"id": id})


if __name__ == "__main__":
    main()
