import configparser

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_data(self):
        data = configparser.ConfigParser()
        data.read("../data/data.ini")
        # data.read("E:/python_projects/Project_HRM/data/data.ini")
        print(data.sections())
        return data

    def explicit_wait_hrm(self, timeout, element_id):
        # Need to implement python exceptions
        w = WebDriverWait(self.driver, timeout)
        w.until(expected_conditions.presence_of_element_located(element_id))
        print("Element is Present")

    def get_table_data(self, page_objects_link):
        pass


