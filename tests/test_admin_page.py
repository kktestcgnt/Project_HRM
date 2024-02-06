import time

from selenium.webdriver.common.by import By

from common.common import BaseClass
from objects.admin_page_objects import AdminPageObjects


class TestAdminPage(BaseClass):

    def test_add_system_user(self):
        print("Driver from TestCase : ", self.driver)

        obj_admin_page = AdminPageObjects(self.driver)

        self.driver.implicitly_wait(10)

        # Navigating to admin page from HRM home page
        obj_admin_page.goto_admin_tab().click()

        # Validating navigation to admin page
        admin_page_validation_text = obj_admin_page.validating_admin_page().text
        assert admin_page_validation_text == 'System Users', 'Admin page validation is FAILED'
        print("Admin page validation is Successful")

        # Navigating to system user add page from admin page
        obj_admin_page.goto_system_user_add_page().click()
        time.sleep(1)

        # Validating navigation to system user add page
        system_user_add_page_validation_text = obj_admin_page.validating_system_user_add_page().text
        assert system_user_add_page_validation_text == 'Add User', 'Add System user page validation FAILED.'
        print('Add System user page validation Successful')

        # To expand system user role dropdown
        obj_admin_page.expanding_user_role_dropdown().click()
        time.sleep(1)

        # Selecting admin user role from system user role dropdown
        obj_admin_page.selecting_admin_userrole().click()
        time.sleep(1)

        # To expand system user status dropdown
        obj_admin_page.expanding_user_status_dropdown().click()
        time.sleep(1)

        # Selecting enabled user status from system user status dropdown
        obj_admin_page.selecting_enabled_system_status().click()
        time.sleep(1)

        # Adding new employee name to add system user
        obj_admin_page.add_employee_name().send_keys("Coll")
        time.sleep(2)

        # Selecting employee name from employee name hints
        obj_admin_page.selecting_employee_name().click()
        time.sleep(2)

        # Adding username to add system user username field
        obj_admin_page.add_system_user_username().send_keys("kktestadmin")
        time.sleep(1)

        # Adding password to system user password field
        obj_admin_page.add_system_user_password().send_keys("kktestadmin1")
        time.sleep(1)

        # Adding confirm password to system user confirm password field
        obj_admin_page.add_system_user_confirm_password().send_keys("kktestadmin1")
        time.sleep(1)

        # Save new system user
        obj_admin_page.save_system_user().click()

        time.sleep(1)

        add_system_user_success_message_text = obj_admin_page.validating_system_user_adduser_success_message().text
        assert add_system_user_success_message_text == 'Successfully Saved', 'Add System user success validation FAILED.'
        print('Add System user success validation Successful')

        time.sleep(10)
