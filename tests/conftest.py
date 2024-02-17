import psycopg2
import pytest


@pytest.fixture()
def postgres():
    class Database:

        def postgres_access(self):
            hostname = '192.168.29.72'
            database = 'testdb'
            username = 'postgres'
            password = 'postgres'
            port = 5432

            # psql_conn = None
            # psql_cursor = None

            psql_conn = psycopg2.connect(host=hostname,
                                         dbname=database,
                                         user=username,
                                         password=password,
                                         port=port)

            print(psql_conn)  # Add Assert statement here.
            print("Connection is Successful")

            psql_cursor = psql_conn.cursor()
            return psql_cursor

    obj_asdf1 = Database()
    return obj_asdf1


def procedural_call():
    hostname = '192.168.29.72'
    database = 'testdb'
    username = 'postgres'
    password = 'postgres'
    port = 5432

    # psql_conn = None
    # psql_cursor = None

    psql_conn = psycopg2.connect(host=hostname,
                                 dbname=database,
                                 user=username,
                                 password=password,
                                 port=port)

    print(psql_conn)  # Add Assert statement here.
    print("Connection is Successful")

    psql_cursor = psql_conn.cursor()
    return psql_cursor


@pytest.fixture()
def postgres2():
    x = procedural_call()
    return x


@pytest.fixture()
def postgres3():
    def call1():
        hostname = '192.168.29.72'
        database = 'testdb'
        username = 'postgres'
        password = 'postgres'
        port = 5432

        # psql_conn = None
        # psql_cursor = None

        psql_conn = psycopg2.connect(host=hostname,
                                     dbname=database,
                                     user=username,
                                     password=password,
                                     port=port)

        print(psql_conn)  # Add Assert statement here.
        print("Connection is Successful")

        psql_cursor = psql_conn.cursor()
        return psql_cursor

    return call1()
