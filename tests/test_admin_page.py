import time

from selenium.webdriver.common.by import By

from common.common import BaseClass
from objects.admin_page_objects import AdminPageObjects


class TestAdminPage(BaseClass):

    def test_add_system_user(self):
        print("Driver from TestCase : ", self.driver)

        obj_admin_page = AdminPageObjects(self.driver)

        obj_admin_page.goto_admin_tab().click()
        #
        # admin_tab = (By.XPATH, "//span[text() = 'Admin']")
        # self.driver.find_element(admin_tab[0], value=admin_tab[1]).click()
        time.sleep(10)


