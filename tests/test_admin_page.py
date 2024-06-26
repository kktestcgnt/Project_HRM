import time

from selenium.webdriver.common.by import By

from common.common import BaseClass
from common.postgres import PostgreSQL
from objects.admin_page_objects import AdminPageObjects


class TestAdminPage(BaseClass):

    def test_add_system_user(self, postgresql_connection):
        """
        This test case will login to application, navigates to

        :param postgresql_connection: This is a fixture which is called from tests/conftest, which establishes postgresql connection.
        :return: This method returns None
        """

        # PostgreSQL class contains methods to read and write data from/to the postgresql database.
        obj_postgresql = PostgreSQL(postgresql_connection)

        obj_admin_page = AdminPageObjects(self.driver)

        self.driver.implicitly_wait(10)

        # Delete existing user function call ---> here
        self.table_element_delete('Admin', 'Username', obj_postgresql.get_data('USERNAME'))

        # Selecting Employee Name dynamically from existing System Users table
        name = self.table_generic_fn('Admin', 'Employee')
        print("Selected Employee name : ", name)

        # Navigating to admin page from HRM home page
        obj_admin_page.goto_admin_tab().click()

        self.explicit_wait_hrm(5, obj_admin_page.admin_page_validation)

        # Validating navigation to admin page
        admin_page_validation_text = obj_admin_page.validating_admin_page().text
        assert admin_page_validation_text == 'System Users', self.logging().error('Admin page validation is FAILED')
        self.logging().info("Admin page validation is Successful")

        # Navigating to system user add page from admin page
        obj_admin_page.goto_system_user_add_page().click()

        self.explicit_wait_hrm(5, obj_admin_page.system_user_add_page_validation)

        # Validating navigation to system user add page
        system_user_add_page_validation_text = obj_admin_page.validating_system_user_add_page().text
        assert system_user_add_page_validation_text == 'Add User', self.logging().error('Add System user page validation FAILED.')
        self.logging().info('Add System user page validation Successful')

        # To expand system user role dropdown
        obj_admin_page.expanding_user_role_dropdown().click()

        self.explicit_wait_hrm(5, obj_admin_page.user_dropdown_select_admin)

        # Selecting admin user role from system user role dropdown
        obj_admin_page.selecting_admin_userrole().click()

        # To expand system user status dropdown
        obj_admin_page.expanding_user_status_dropdown().click()

        self.explicit_wait_hrm(3, obj_admin_page.user_status_select_enabled)

        # Selecting enabled user status from system user status dropdown
        obj_admin_page.selecting_enabled_system_status().click()

        # Adding new employee name to add system user
        obj_admin_page.add_employee_name().send_keys(name)

        self.explicit_wait_hrm(3, obj_admin_page.employee_name_select)

        # Selecting employee name from employee name hints
        obj_admin_page.selecting_employee_name().click()

        # Adding username to add system user username field
        obj_admin_page.add_system_user_username().send_keys(obj_postgresql.get_data('USERNAME'))

        # Adding password to system user password field
        obj_admin_page.add_system_user_password().send_keys(obj_postgresql.get_data('PASSWORD'))

        # Adding confirm password to system user confirm password field
        obj_admin_page.add_system_user_confirm_password().send_keys(obj_postgresql.get_data('CONFIRM_PASSWORD'))

        # Save new system user
        obj_admin_page.save_system_user().click()

        self.explicit_wait_hrm(3, obj_admin_page.system_user_adduser_success_validation)

        add_system_user_success_message_text = obj_admin_page.validating_system_user_adduser_success_message().text
        assert add_system_user_success_message_text == 'Successfully Saved', self.logging().error('Add System user success validation FAILED.')
        self.logging().info('Add System user success validation Successful')

        time.sleep(10)


