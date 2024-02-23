from common.postgres import PostgreSQL


class TestDataBase:

    def test_login_check(self, postgres):
        print(postgres.postgres_access())
        db_pointer = postgres.postgres_access()
        db_pointer.execute("SELECT * FROM EMPLOYEE_DET;")

        table_data = db_pointer.fetchall()

        for row_data in table_data:
            print(row_data)

    def test_login_check2(self, postgres2):
        postgres2.execute("SELECT * FROM EMPLOYEE_DET;")

        table_data = postgres2.fetchall()

        for row_data in table_data:
            print(row_data)

    def test_read_data_postgresql(self, postgresql_connection):
        """
        :param postgresql_connection: This is a fixture which establishes connection to postgresql and return the cursor pointer
        :return: This function returns None
        """

        obj_postgresql = PostgreSQL(postgresql_connection)
        obj_postgresql.get_data('ID', 'NAME')
