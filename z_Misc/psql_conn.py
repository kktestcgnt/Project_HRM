import psycopg2

hostname = '192.168.0.171'
database = 'testdb'
username = 'postgres'
password = 'postgres'
port = 5432

psql_conn = None
psql_cursor = None

try:
    psql_conn = psycopg2.connect(host=hostname,
                                 dbname=database,
                                 user=username,
                                 password=password,
                                 port=port)

    print(psql_conn)    # Add Assert statement here.
    print("Connection is Successful")

    psql_cursor = psql_conn.cursor()

    psql_cursor.execute("SELECT * FROM HRM_ADMIN;")

    table_data = psql_cursor.fetchall()

    for row_data in table_data:
        print(row_data)


except Exception as error:
    print(error)
finally:
    if psql_cursor is not None:
        psql_cursor.close()
    if psql_conn is not None:
        psql_conn.close()
        print("psql connection is closed.")



