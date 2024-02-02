import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

username = (By.XPATH, "//input[@name = 'username']")
password = (By.XPATH, "//input[@name = 'password']")
login_btn = (By.XPATH, "//button[text() = ' Login ']")

driver.find_element(username[0], value=username[1]).send_keys("Admin")
time.sleep(3)
driver.find_element(password[0], value=password[1]).send_keys("admin123")
time.sleep(3)
driver.find_element(login_btn[0], value=login_btn[1]).click()
time.sleep(10)

admin_tab = (By.XPATH, "//span[text() = 'Admin']")
driver.find_element(admin_tab[0], value=admin_tab[1]).click()
time.sleep(10)

admin_page_validation = (By.XPATH, "//h5[text() = 'System Users']")
value = driver.find_element(admin_page_validation[0], value=admin_page_validation[1]).text
print(value)
assert value == 'System Users', 'Admin page validation is FAILED'
print("Admin page validation is Successful")
time.sleep(3)

system_user_add_btn = (By.XPATH, "//button[text() = ' Add ']")
driver.find_element(system_user_add_btn[0], value=system_user_add_btn[1]).click()
time.sleep(5)

system_user_add_page_validation = (By.XPATH, "//h6[text() = 'Add User']")
assert driver.find_element(system_user_add_page_validation[0],
                           value=system_user_add_page_validation[1]).text == 'Add User', ('Add System user page '
                                                                                          'validation FAILED.')
print('Add System user page validation Successful')
time.sleep(3)

user_dropdown = (By.XPATH, "//label[text() = 'User Role']//parent::div//following-sibling::div/div/div//following-sibling::div/i")
driver.find_element(user_dropdown[0], user_dropdown[1]).click()
time.sleep(3)

user_dropdown_select_admin = (By.XPATH, "//label[text() = 'User Role']//parent::div//following-sibling::div/div/div[2]/div[2]/span[text() = 'Admin']")
driver.find_element(user_dropdown_select_admin[0], user_dropdown_select_admin[1]).click()
time.sleep(3)

user_status_dropdown = (By.XPATH, "//label[text() = 'Status']//parent::div//following-sibling::div/div/div//following-sibling::div/i")
driver.find_element(user_status_dropdown[0], user_status_dropdown[1]).click()
time.sleep(3)

user_status_select_enabled = (By.XPATH, "//label[text() = 'Status']//parent::div//following-sibling::div/div/div[2]/div[2]/span[text()='Enabled']")
driver.find_element(user_status_select_enabled[0], user_status_select_enabled[1]).click()
time.sleep(3)

employee_name = (By.XPATH, "//label[text() = 'Employee Name']//parent::div//following-sibling::div/div/div/input")
driver.find_element(employee_name[0], employee_name[1]).send_keys("HRM KKTest")
time.sleep(7)
# ToDo - Add Validations

su_username = (By.XPATH, "//label[text() = 'Username']//parent::div//following-sibling::div/input")
# ToDo - Add Validations

driver.find_element(su_username[0], su_username[1]).send_keys("kktestadmin")
time.sleep(7)
# ToDo - Add condition for Already Exists User

su_password = (By.XPATH, "//label[text() = 'Password']//parent::div//following-sibling::div/input")
driver.find_element(su_password[0], su_password[1]).send_keys("kktestadmin1")
time.sleep(7)

su_confirm_password = (By.XPATH, "//label[text() = 'Confirm Password']//parent::div//following-sibling::div/input")
driver.find_element(su_confirm_password[0], su_confirm_password[1]).send_keys("kktestadmin1")
time.sleep(10)

su_adduser_save_btn = (By.XPATH, "//button[text() = ' Save ']")
driver.find_element(su_adduser_save_btn[0], su_adduser_save_btn[1]).click()
time.sleep(10)






