import pytest

from common.postgres import PostgreSQL
from common.mongodb import MongoDB


class TestDataBase:

    def test_login_check(self, postgres):
        print(postgres.postgres_access())
        db_pointer = postgres.postgres_access()
        db_pointer.execute("SELECT * FROM EMPLOYEE_DET;")

        table_data = db_pointer.fetchall()

        for row_data in table_data:
            print(row_data)

    @pytest.mark.parametrize("mongodb_connection", [('mydb', 'sysusers')], indirect=True)
    def test_read_data_mongodb(self, mongodb_connection):
        """
        :param mongodb_connection: This is a fixture which establishes connection to mongodb database and return the database connection
        :return: This function returns None
        """

        print("\nTest Cursor : ", mongodb_connection)
        obj_mongodb = MongoDB(mongodb_connection)

    def test_read_data_postgresql(self, postgresql_connection):
        """
        :param postgresql_connection: This is a fixture which establishes connection to postgresql and return the cursor pointer
        :return: This function returns None
        """

        obj_postgresql = PostgreSQL(postgresql_connection)
        obj_postgresql.get_data('ID', 'NAME')
