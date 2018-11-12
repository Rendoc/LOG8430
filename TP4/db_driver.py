from cassandra.cluster import Cluster
from cassandra.query import dict_factory

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


if __name__ == "__main__":
    main()


def add_facture(facture):
    session.execute(
        """
        INSERT INTO factures (id, title)
        VALUES (%s, %s)
        """,
        (facture["id"], facture["title"])
    )


def get_factures():
    future = session.execute("SELECT * FROM factures")
    return dict(future)
