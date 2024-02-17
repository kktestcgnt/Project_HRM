from common.data_access import DataAccess
from enum import Enum


class Data(Enum):
    ID = 0
    NAME = 1
    LNAME = 2


x = ('7369', 'SMITH', 'JOHN')
print(x[Data['NAME'].value])


class PostgreSQL(DataAccess):

    def __init__(self, data_pointer):
        self.data_pointer = data_pointer

        self.reading_data = self.read_data()

    def read_data(self):
        self.data_pointer.execute("SELECT * FROM EMPLOYEE_DET;")

        raw_data = self.data_pointer.fetchall()
        return raw_data

        # for row_data in table_data:
        #     print(row_data)

    def get_data(self, z):
        y = self.reading_data
        print(y)
        for each in y:
            print(each[Data[str(z)].value])





    def write_data(self):
        pass
