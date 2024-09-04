from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from common.common import BaseClass
import os
import time


class PimPageObjects:
    # page_value = ''

    def __init__(self, driver):
        self.driver = driver

    pim_tab = (By.XPATH, "//span[text() = 'PIM']")
    pim_page_validation = (By.XPATH, "//h5[text() = 'Employee Information']")
    pim_add_employee_btn = (By.XPATH, "//button[text() = ' Add ']")
    pim_add_employee_upload_image_btn = (By.XPATH, "//button[contains(@class, 'employee-image-action')]/i")
    pim_add_employee_uploaded_image_validation = (By.XPATH, "//img[contains(@src, 'data')]")

    def validating_add_employee_uploaded_image(self):
        return self.driver.find_element(*PimPageObjects.pim_add_employee_uploaded_image_validation)

    def add_employee_upload_image(self):
        return self.driver.find_element(*PimPageObjects.pim_add_employee_upload_image_btn)

    def goto_pim_add_employee_page(self):
        return self.driver.find_element(*PimPageObjects.pim_add_employee_btn)

    def validating_pim_page(self):
        return self.driver.find_element(*PimPageObjects.pim_page_validation)

    def goto_pim_tab(self):
        return self.driver.find_element(*PimPageObjects.pim_tab)

    def add_employee_upload_image_file(self):

        self.add_employee_upload_image().click()
        keyboard_action = Controller()
        time.sleep(3)

        # keyboard.type("../z_Misc/files/upload_pim_picture.png")
        # root_dir = os.path.dirname(os.path.abspath(__file__))
        # print(root_dir)
        keyboard_action.type("H:\\Python_Projects\\Project_HRM\\z_Misc\\files\\upload_pim_picture.png")
        # keyboard_action.type(root_dir + "\\files\\upload_pim_picture.png")
        time.sleep(5)
        keyboard_action.press(Key.enter)
        time.sleep(5)
        keyboard_action.release(Key.enter)
        time.sleep(5)

    def validating_add_employee_uploaded_image_file(self):
        req_text = self.validating_add_employee_uploaded_image().get_attribute('src')
        req_text_list = req_text.split(':')
        final_req_text = req_text_list[0].strip()
        print('Final text: ', final_req_text)

        assert final_req_text == 'data', BaseClass.logging().error('Pim uploaded image validation is FAILED')
        BaseClass.logging().info("Pim uploaded image validation is Successful")




