import time

from common.common import BaseClass
from common.postgres import PostgreSQL
from objects.pim_page_objects import PimPageObjects


class TestPimPage(BaseClass):

    def test_pim_add_employee(self, postgresql_connection):
        obj_postgresql = PostgreSQL(postgresql_connection)

        obj_pim_page = PimPageObjects(self.driver)

        self.driver.implicitly_wait(10)

        obj_pim_page.goto_pim_tab().click()

        self.explicit_wait_hrm(5, obj_pim_page.pim_page_validation)

        # Validating navigation to admin page
        pim_page_validation_text = obj_pim_page.validating_pim_page().text
        assert pim_page_validation_text == 'Employee Information', self.logging().error('Pam page validation is FAILED')
        self.logging().info("Pim page validation is Successful")

        # Navigating to system user add page from admin page
        obj_pim_page.goto_pim_add_employee_page().click()

        obj_pim_page.add_employee_upload_image_file()

        obj_pim_page.validating_add_employee_uploaded_image_file()

        time.sleep(5)


