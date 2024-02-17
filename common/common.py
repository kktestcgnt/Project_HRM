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
    popup_delete_button = (By.XPATH, "//p[text() = 'Are you Sure?']//parent::div//following-sibling::div[2]/button[text() = ' Yes, Delete ']")

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
        hrm_tab = (By.XPATH, "//span[text() = '" + page_value + "']")
        self.driver.find_element(hrm_tab[0], value=hrm_tab[1]).click()
        self.driver.implicitly_wait(5)
        time.sleep(5)

        page_table_header_body_elements = self.driver.find_elements(self.page_table_header_body[0], value=self.page_table_header_body[1])
        time.sleep(5)
        hrm_table_ref = self.page_table_header_body

        for value in range(len(page_table_header_body_elements)):
            # Converting Tuple into List for edit access/ update
            hrm_table_ref = list(hrm_table_ref)
            # hrm_table_ref[1] is selected to point to the header tag
            hrm_table_ref[1] = hrm_table_ref[1] + '[' + str(value + 1) + ']'
            # page_table_header_att_value is loaded with header tag attribute (class) value. Eg: page_table_header_att_value = oxd-table-header
            page_table_header_att_value = self.driver.find_element(hrm_table_ref[0], hrm_table_ref[1]).get_attribute('class')
            if 'header' in page_table_header_att_value:
                # adding /div/div to get the number of column header tags. Eg: checkbox, Username, Emp ID, Actions ....
                hrm_table_ref[1] = str(hrm_table_ref[1]) + "/div/div"
                # Getting all column header tags into column_count variable
                column_count = self.driver.find_elements(hrm_table_ref[0], value=hrm_table_ref[1])
                # hrm_table_dummy_ref is the dummy reference for column header tags.
                hrm_table_dummy_ref = hrm_table_ref[1]
                for column in range(len(column_count)):
                    # Iterating each column header tag
                    hrm_table_ref[1] = hrm_table_ref[1] + '[' + str(column + 1) + ']'
                    # Getting header tag name text
                    page_table_column_name_text = self.driver.find_element(hrm_table_ref[0], hrm_table_ref[1]).text
                    hrm_table_ref[1] = hrm_table_dummy_ref
                    # To get the column index/ number with reference to column reference name
                    if str(column_reference) in page_table_column_name_text:
                        index = column + 1
                        break
            else:  # for page_table_body
                # /div is appended to select table body
                hrm_table_ref[1] = str(hrm_table_ref[1]) + "/div"
                # Total row count in table body
                row_count = self.driver.find_elements(hrm_table_ref[0], value=hrm_table_ref[1])
                # hrm_table_dummy_ref is the dummy reference for column header tags.
                # hrm_table_dummy_ref = hrm_table_ref[1]
                # Selecting random row number
                select_row_num = random.randint(1, len(row_count))
                # To retrieve particular tag(row, column) from above selected random row
                hrm_table_ref[1] = hrm_table_ref[1] + '[' + str(select_row_num) + ']' + '/div/div[' + str(index) + ']/div'
                # To retrieve particular element text(row, column) from above selected random row
                emp_name = self.driver.find_element(hrm_table_ref[0], hrm_table_ref[1]).text
                name = emp_name.split(' ')
            # tag for page table header body
            hrm_table_ref = self.page_table_header_body
        # Returning portion of selected element text. This is used to
        return name[0]

    def table_element_delete(self, page_value, column_reference, element_value):
        hrm_tab = (By.XPATH, "//span[text() = '" + page_value + "']")
        self.driver.find_element(hrm_tab[0], value=hrm_tab[1]).click()
        self.driver.implicitly_wait(5)
        time.sleep(5)

        page_table_header_body_elements = self.driver.find_elements(self.page_table_header_body[0], value=self.page_table_header_body[1])
        time.sleep(5)
        hrm_table_ref = self.page_table_header_body

        for value in range(len(page_table_header_body_elements)):
            hrm_table_ref = list(hrm_table_ref)
            hrm_table_ref[1] = hrm_table_ref[1] + '[' + str(value + 1) + ']'
            page_table_header_att_value = self.driver.find_element(hrm_table_ref[0], hrm_table_ref[1]).get_attribute('class')
            if 'header' in page_table_header_att_value:
                hrm_table_ref[1] = str(hrm_table_ref[1]) + "/div/div"
                column_count = self.driver.find_elements(hrm_table_ref[0], value=hrm_table_ref[1])
                y = hrm_table_ref[1]
                for column in range(len(column_count)):
                    hrm_table_ref[1] = hrm_table_ref[1] + '[' + str(column + 1) + ']'
                    page_table_column_name_text = self.driver.find_element(hrm_table_ref[0], hrm_table_ref[1]).text
                    hrm_table_ref[1] = y
                    if str(column_reference) in page_table_column_name_text:
                        print("=============== >>>> ", column_reference)
                        index = column + 1
                    if str('Actions') in page_table_column_name_text:
                        delete_index = column + 1
            else:
                hrm_table_ref[1] = str(hrm_table_ref[1]) + "/div"
                row_count = self.driver.find_elements(hrm_table_ref[0], value=hrm_table_ref[1])
                y = hrm_table_ref[1]
                for each_row in range(len(row_count)):
                    hrm_table_ref[1] = hrm_table_ref[1] + '[' + str(each_row + 1) + ']' + '/div/div[' + str(index) + ']/div'
                    print("========================= >>>>>>> ", hrm_table_ref[1])
                    element_name = self.driver.find_element(hrm_table_ref[0], hrm_table_ref[1]).text
                    print("Selected Username : ", element_name)
                    if element_name in element_value:
                        print("==========  Inside IF")
                        row_value = each_row
                        hrm_table_ref[1] = y
                        hrm_table_ref[1] = hrm_table_ref[1] + '[' + str(each_row + 1) + ']' + '/div/div[' + str(delete_index) + ']/div/button'
                        print(hrm_table_ref[1])
                        y = hrm_table_ref[1]

                        # hrm_table_ref[1] = //div[@class = 'orangehrm-container']/div/div[2]/div
                        # each_row = 3
                        # delete_index = 6
                        # //div[@class = 'orangehrm-container']/div/div[2]/div[3]/div/div[6]/div

                        actions_column_icons_count = self.driver.find_elements(hrm_table_ref[0], value=hrm_table_ref[1])
                        print(len(actions_column_icons_count))
                        for action_column_icon in range(len(actions_column_icons_count)):
                            hrm_table_ref[1] = hrm_table_ref[1] + '[' + str(action_column_icon + 1) + ']/i'
                            print("Button : ", hrm_table_ref[1])
                            # print(action_column_icon_attr_value)
                            print("Trash attr value : ", self.driver.find_element(hrm_table_ref[0], hrm_table_ref[1]).get_attribute('class'))

                            if 'trash' in self.driver.find_element(hrm_table_ref[0], hrm_table_ref[1]).get_attribute('class'):
                                self.driver.find_element(hrm_table_ref[0], hrm_table_ref[1]).click()
                                print("Delete Icon path : ", hrm_table_ref[1])
                                break
                            hrm_table_ref[1] = y
                        time.sleep(5)
                        self.driver.find_element(self.popup_delete_button[0], self.popup_delete_button[1]).click()
                        time.sleep(5)

                        system_user_delete_success_validation = (By.XPATH, "//p[text()='Successfully Deleted']")
                        # print(system_user_delete_success_validation)

                        break
                    hrm_table_ref[1] = y
                else:
                    print("User to be deleted is not found. Adding new User")

            hrm_table_ref = self.page_table_header_body
