from selenium.webdriver.common.by import By


class AdminPageObjects:
    # page_value = ''

    def __init__(self, driver):
        self.driver = driver

    # admin_tab_for_table = (By.XPATH, "//span[text() = '" + page_value + "']")
    admin_tab = (By.XPATH, "//span[text() = 'Admin']")
    admin_page_validation = (By.XPATH, "//h5[text() = 'System Users']")
    system_user_add_btn = (By.XPATH, "//button[text() = ' Add ']")
    system_user_add_page_validation = (By.XPATH, "//h6[text() = 'Add User']")
    user_dropdown = (By.XPATH, "//label[text() = 'User Role']//parent::div//following-sibling::div/div/div//following-sibling::div/i")
    user_dropdown_select_admin = (By.XPATH, "//label[text() = 'User Role']//parent::div//following-sibling::div/div/div[2]/div[2]/span[text() = 'Admin']")
    user_status_dropdown = (By.XPATH, "//label[text() = 'Status']//parent::div//following-sibling::div/div/div//following-sibling::div/i")
    user_status_select_enabled = (By.XPATH, "//label[text() = 'Status']//parent::div//following-sibling::div/div/div[2]/div[2]/span[text()='Enabled']")
    employee_name = (By.XPATH, "//label[text() = 'Employee Name']//parent::div//following-sibling::div/div/div/input")
    employee_name_select = (By.XPATH, "//label[text() = 'Employee Name']//parent::div//following-sibling::div/div/div[2]/div/span")
    system_user_username = (By.XPATH, "//label[text() = 'Username']//parent::div//following-sibling::div/input")
    system_user_password = (By.XPATH, "//label[text() = 'Password']//parent::div//following-sibling::div/input")
    system_user_confirm_password = (By.XPATH, "//label[text() = 'Confirm Password']//parent::div//following-sibling::div/input")
    system_user_adduser_save_btn = (By.XPATH, "//button[text() = ' Save ']")
    system_user_adduser_success_validation = (By.XPATH, "//p[text()='Successfully Saved']")

    def validating_system_user_adduser_success_message(self):
        return self.driver.find_element(*AdminPageObjects.system_user_adduser_success_validation)

    def save_system_user(self):
        return self.driver.find_element(*AdminPageObjects.system_user_adduser_save_btn)

    def add_system_user_confirm_password(self):
        return self.driver.find_element(*AdminPageObjects.system_user_confirm_password)

    def add_system_user_password(self):
        return self.driver.find_element(*AdminPageObjects.system_user_password)

    def add_system_user_username(self):
        return self.driver.find_element(*AdminPageObjects.system_user_username)

    def selecting_employee_name(self):
        return self.driver.find_element(*AdminPageObjects.employee_name_select)

    def add_employee_name(self):
        return self.driver.find_element(*AdminPageObjects.employee_name)

    def selecting_enabled_system_status(self):
        return self.driver.find_element(*AdminPageObjects.user_status_select_enabled)

    def expanding_user_status_dropdown(self):
        return self.driver.find_element(*AdminPageObjects.user_status_dropdown)

    def selecting_admin_userrole(self):
        return self.driver.find_element(*AdminPageObjects.user_dropdown_select_admin)

    def goto_admin_tab(self):
        return self.driver.find_element(*AdminPageObjects.admin_tab)

    def validating_admin_page(self):
        return self.driver.find_element(*AdminPageObjects.admin_page_validation)

    def goto_system_user_add_page(self):
        return self.driver.find_element(*AdminPageObjects.system_user_add_btn)

    def validating_system_user_add_page(self):
        return self.driver.find_element(*AdminPageObjects.system_user_add_page_validation)

    def expanding_user_role_dropdown(self):
        return self.driver.find_element(*AdminPageObjects.user_dropdown)
