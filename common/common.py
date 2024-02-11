import configparser
import logging
from datetime import datetime

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# =======================================================================
from selenium.webdriver.common.by import By
import time
import random


file_handler = 0
console_handler = 0


@pytest.mark.usefixtures("setup")
class BaseClass:

    page_table_header_body = (By.XPATH, "//div[@class = 'orangehrm-container']/div/div")

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
        global file_handler
        if file_handler == 0:
            file_handler = logging.FileHandler("../logs/log" + current_time + ".log", mode='a')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Define Console/Stream Handler
        global console_handler
        if console_handler == 0:
            console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        return logger

    def logger(self):
        return self.logging()

    def table_generic_fn(self, page_value, column_reference):
        admin_tab = (By.XPATH, "//span[text() = '" + page_value + "']")
        self.driver.find_element(admin_tab[0], value=admin_tab[1]).click()
        self.driver.implicitly_wait(5)
        time.sleep(5)

        x = self.driver.find_elements(self.page_table_header_body[0], value=self.page_table_header_body[1])
        time.sleep(5)
        z = self.page_table_header_body

        for value in range(len(x)):
            z = list(z)
            z[1] = z[1] + '[' + str(value + 1) + ']'
            page_table_header_att_value = self.driver.find_element(z[0], z[1]).get_attribute('class')
            if 'header' in page_table_header_att_value:
                z[1] = str(z[1]) + "/div/div"
                column_count = self.driver.find_elements(z[0], value=z[1])
                y = z[1]
                for column in range(len(column_count)):
                    z[1] = z[1] + '[' + str(column + 1) + ']'
                    page_table_column_name_text = self.driver.find_element(z[0], z[1]).text
                    z[1] = y
                    if str(column_reference) in page_table_column_name_text:
                        index = column + 1
                        break
            else:
                z[1] = str(z[1]) + "/div"
                row_count = self.driver.find_elements(z[0], value=z[1])
                y = z[1]
                select_row_num = random.randint(1, len(row_count))
                z[1] = z[1] + '[' + str(select_row_num) + ']' + '/div/div[' + str(index) + ']/div'
                emp_name = self.driver.find_element(z[0], z[1]).text
                name = emp_name.split(' ')

            z = self.page_table_header_body

        return name[0]

    def get_table_data(self, page_objects_link):
        pass
