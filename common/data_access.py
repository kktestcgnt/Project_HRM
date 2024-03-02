from abc import ABC, abstractmethod


class DataAccess(ABC):

    # read_data, write_data are common methods in PostgreSQL, MongoDB, IniFile
    @abstractmethod
    def read_data(self):
        """
        This function will return the raw data from its child classes (PostgreSQL / MongoDB / IniFile)
        :return: This will return None
        """

        pass

    @abstractmethod
    def write_data(self):
        """
        This function will return the success/failed status for write_data from its child classes (PostgreSQL / MongoDB / IniFile)
        :return: This will return None
        """
        pass
