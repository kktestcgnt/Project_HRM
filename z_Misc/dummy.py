import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
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
driver.implicitly_wait(10)

# =================================================================================

admin_tab = (By.XPATH, "//span[text() = 'PIM']")
driver.find_element(admin_tab[0], value=admin_tab[1]).click()
time.sleep(5)

page_table = (By.XPATH, "//div[@class = 'orangehrm-container']")
page_table_header_body = (By.XPATH, "//div[@class = 'orangehrm-container']/div/div")
# page_table_rows_count =

x = driver.find_elements(page_table_header_body[0], value=page_table_header_body[1])
print(x)
print(len(x))
time.sleep(5)
print(page_table_header_body)
z = page_table_header_body

for value in range(len(x)):
    z = list(z)
    z[1] = z[1] + '[' + str(value + 1) + ']'
    print(z)
    page_table_header_att_value = driver.find_element(z[0], z[1]).get_attribute('class')
    print(page_table_header_att_value)

    if 'header' in page_table_header_att_value:
        # print("inside if --> ", z[1])
        z[1] = str(z[1]) + "/div/div"
        column_count = driver.find_elements(z[0], value=z[1])
        print(len(column_count))
        y = z[1]

        for column in range(len(column_count)):
            z[1] = z[1] + '[' + str(column + 1) + ']'
            print(z)
            page_table_column_name_text = driver.find_element(z[0], z[1]).text
            print(page_table_column_name_text)
            z[1] = y

            if 'Last' in page_table_column_name_text:
                index = column + 1
                break
        print(index)

    else:
        z[1] = str(z[1]) + "/div"
        row_count = driver.find_elements(z[0], value=z[1])
        print(len(row_count))
        y = z[1]
        select_row_num = random.randint(1, len(row_count))

        z[1] = z[1] + '[' + str(select_row_num) + ']' + '/div/div[' + str(index) + ']/div'
        emp_name = driver.find_element(z[0], z[1]).text
        print("====================")
        print(emp_name)
        name = emp_name.split(' ')
        print(name)
        print(name[0])
        print(z[1])
        print(index)

    z = page_table_header_body


def table_generic_fn(page_value, column_reference): # Above lines from 1 to 88 need tp be copied in this function and copy the same function in base class and use this generic function in test_admin_page.py
    pass
"""

# count = 0
#
#
# class MyClass:
#     count = 0
#
#     def func1(self):
#         MyClass.count = MyClass.count + 1
#         print("Func1 Count : ", MyClass.count)
#         print("Func1")
#         self.func2()
#
#     def func2(self):
#         MyClass.count = MyClass.count + 1
#         print("Func2 Count : ", MyClass.count)
#         if MyClass.count > 5:
#             exit(0)
#         print('Func2')
#         self.func1()
#
#
# obj_func2 = MyClass()
# obj_func2.func2()


import configparser

# Create configparser object
config_object = configparser.ConfigParser()
with open("../data/data.ini", "r") as file_object:
    print(config_object.read_file(file_object))
    url=config_object.get("app_login_page")
    print(url)



