import pytest

from common.postgres import PostgreSQL
from common.mongodb import MongoDB
from common.inifile import IniFile


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
        print(obj_postgresql.get_data('USERROLE'))
        print(obj_postgresql.get_data('USERROLE', 'STATUS', 'USERNAME', 'PASSWORD', 'CONFIRM_PASSWORD'))

    @pytest.mark.parametrize("inifile_connection", [('../data/data.ini', 'dummy_string')], indirect=True)   # In list[(tuple)], second element is compulsory. So dummy_string is considered.
    def test_read_data_inifile(self, inifile_connection):
        """
        :param inifile_connection: This is a fixture which establishes connection to inifile and return the ini file cursor pointer
        :return: This function returns None
        """

        # print(inifile_connection.sections())
        obj_inifile = IniFile(inifile_connection)
        print('in test - ', obj_inifile.read_data())

        # obj_postgresql.get_data('ID', 'NAME')