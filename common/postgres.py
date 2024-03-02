from common.data_access import DataAccess
from enum import Enum


class Data(Enum):
    # For hard coding the indices of table column headers
    ID = 0
    USERROLE = 1
    STATUS = 2
    USERNAME = 3
    PASSWORD = 4
    CONFIRM_PASSWORD = 4


# x = ('7369', 'SMITH', 'JOHN')
# ref_indices_for_above_tuple_x = ('ID'. 'NAME', 'LNAME')
# print(x[Data['NAME'].value])
# Output = 'SMITH'


class PostgreSQL(DataAccess):
    # DataAccess is abstract class

    def __init__(self, data_pointer):
        """
        :param data_pointer: This is the cursor to postgresql database
        :variable reading_data: Will contain the raw data which is returned from read_data method.
        """
        self.data_pointer = data_pointer
        self.reading_data = self.read_data()

    def read_data(self):
        """
        This method will read the raw data from postgresql database based on the provided sql query
        :return: This will return the above read raw data
        """
        self.data_pointer.execute("SELECT * FROM HRM_ADMIN LIMIT 1;")

        raw_data = self.data_pointer.fetchall()
        return raw_data

    def get_data(self, *column_headers):

        size = len(column_headers)

        raw_data = self.reading_data
        # print(raw_data)

        filtered_data = []

        if size == 1:
            for each in raw_data:
                return each[Data[str(column_headers[0])].value]
        else:
            for each in column_headers:
                for each_column in raw_data:
                    filtered_data.append(each_column[Data[str(each)].value])
            return filtered_data

    def write_data(self):
        pass
