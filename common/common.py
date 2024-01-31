import configparser


class BaseClass:

    def get_data(self):
        data = configparser.ConfigParser()
        data.read("../data/data.ini")
        # data.read("E:/python_projects/Project_Transform/data/data.ini")
        print(data.sections())
        return data

