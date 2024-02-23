from common.data_access import DataAccess
from enum import Enum


class Data(Enum):
    # For hard coding the indices of table column headers
    ID = 0
    NAME = 1
    LNAME = 2

# x = ('7369', 'SMITH', 'JOHN')
# ref_indices_for_above_tuple_x = ('ID'. 'NAME', 'LNAME')
# print(x[Data['NAME'].value])
# Output = 'SMITH'


class PostgreSQL(DataAccess):
    # DataAccess is abstract class

    def __init__(self, data_pointer):
        self.data_pointer = data_pointer

        self.reading_data = self.read_data()

    def read_data(self):
        self.data_pointer.execute("SELECT * FROM EMPLOYEE_DET;")

        raw_data = self.data_pointer.fetchall()
        return raw_data

    def get_data(self, *column_headers):

        size = len(column_headers)

        raw_data = self.reading_data
        print(raw_data)

        if size == 1:
            for each in raw_data:
                print(each[Data[str(column_headers[0])].value])
        else:
            print('inside else')
            for each in column_headers:
                print(each)
                for each_column in raw_data:
                    print(each_column[Data[str(each)].value])
                print('***************************************************************')






    def write_data(self):
        pass
