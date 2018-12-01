from cassandra.cluster import Cluster
from cassandra.query import dict_factory
import json

KEYSPACE = 'factures_keyspace'
cluster = Cluster()
session = cluster.connect()
session.row_factory = dict_factory


def main():
    session.execute(
        """
        CREATE KEYSPACE IF NOT EXISTS %s
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
        """ % KEYSPACE
    )

    session.set_keyspace(KEYSPACE)

    session.execute(
        """
        CREATE TABLE IF NOT EXISTS factures (
            id int,
            title text,
            PRIMARY KEY (id)
        )
        """
    )


def add_facture(facture):
    session.execute(
        """
        INSERT INTO factures (id, title)
        VALUES (%s, %s)
        """,
        (facture["id"], facture["title"])
    )


def get_factures():
    factures = []
    rows = session.execute("SELECT * FROM factures")
    for row in rows:
        factures.append(row)
    return factures


def get_facture(id):
    factures = []
    rows = session.execute("SELECT * FROM factures WHERE id = {0}".format(id))
    for row in rows:
        factures.append(row)
    return factures


if __name__ == "__main__":
    main()
