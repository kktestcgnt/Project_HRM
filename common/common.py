import configparser
import logging
from datetime import datetime

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

    @staticmethod
    def logging():
        # Define Current time
        time_now = datetime.now()
        current_time = time_now.strftime("%d-%m-%Y--%H-%M-%S")

        # Define logger
        # name = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)

        # Define new log level
        new_log_level = 60
        logging.addLevelName(new_log_level, "new_log_level")

        # Set log level
        logger.setLevel(logging.DEBUG)

        # Set Log Format
        formatter = logging.Formatter("%(asctime)s - %(filename)s - %(lineno)s - %(funcName)s - %(levelname)s - %(message)s")

        # Define File Handler
        file_handler = logging.FileHandler("../logs/log" + current_time + ".log", mode='a')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Define Console/Stream Handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        return logger

    def logger(self):
        return self.logging()


    def get_table_data(self, page_objects_link):
        pass


