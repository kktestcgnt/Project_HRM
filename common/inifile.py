from common.data_access import DataAccess


class IniFile(DataAccess):

    def __init__(self, data_pointer):
        self.data_pointer = data_pointer
        self.read_data()

    def read_data(self):
        return self.data_pointer.sections()

    def write_data(self):
        pass
