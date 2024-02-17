from abc import ABC, abstractmethod


class DataAccess(ABC):

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self):
        pass
