from common.postgres import PostgreSQL

class TestLoginPage:

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

    def test_login_check3(self, postgres3):
        # postgres3.execute("SELECT * FROM EMPLOYEE_DET;")
        #
        # table_data = postgres3.fetchall()
        #
        # for row_data in table_data:
        #     print(row_data)

        obj_postgresql = PostgreSQL(postgres3)
        obj_postgresql.get_data('ID')




