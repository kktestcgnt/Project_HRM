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


# postgresql = {'postgresql_connection': None, 'postgresql_pointer': 0}
postgresql = {}


@pytest.fixture()
def postgresql_connection():
    global postgresql

    def establishing_connection():
        global postgresql
        hostname = '192.168.29.72'
        database = 'testdb'
        username = 'postgres'
        password = 'postgres'
        port = 5432

        postgresql['db_connection'] = psycopg2.connect(host=hostname,
                                                       dbname=database,
                                                       user=username,
                                                       password=password,
                                                       port=port)
        print(postgresql['db_connection'])  # Add Assert statement here.
        print("Connection is Successful")

        postgresql['db_cursor'] = postgresql['db_connection'].cursor()
        return postgresql['db_cursor']

    yield establishing_connection()
    postgresql['db_cursor'].close()
    postgresql['db_connection'].close()
