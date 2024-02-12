import random
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
driver.implicitly_wait(10)

# =================================================================================

admin_tab = (By.XPATH, "//span[text() = 'PIM']")
driver.find_element(admin_tab[0], value=admin_tab[1]).click()
time.sleep(5)

page_table = (By.XPATH, "//div[@class = 'orangehrm-container']")
page_table_header_body = (By.XPATH, "//div[@class = 'orangehrm-container']/div/div")
popup_delete_button = (By.XPATH, "//p[text() = 'Are you Sure?']//parent::div//following-sibling::div[2]/button[text() = ' Yes, Delete ']")
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

# ==================================================================================================


for value in range(len(x)):
    z = list(z)
    z[1] = z[1] + '[' + str(value + 1) + ']'
    page_table_header_att_value = driver.find_element(z[0], z[1]).get_attribute('class')
    if 'header' in page_table_header_att_value:
        z[1] = str(z[1]) + "/div/div"
        column_count = driver.find_elements(z[0], value=z[1])
        y = z[1]
        for column in range(len(column_count)):
            z[1] = z[1] + '[' + str(column + 1) + ']'
            page_table_column_name_text = driver.find_element(z[0], z[1]).text
            z[1] = y
            if str('User') in page_table_column_name_text:
                index = column + 1
            if str('Actions') in page_table_column_name_text:
                delete_index = column + 1
    else:
        z[1] = str(z[1]) + "/div"
        row_count = driver.find_elements(z[0], value=z[1])
        y = z[1]
        for each_row in range(row_count + 1):
            z[1] = z[1] + '[' + str(each_row) + ']' + '/div/div[' + str(index) + ']/div'
            element_name = driver.find_element(z[0], z[1]).text
            print("Selected Username : ", element_name)
            if element_name == 'kktestadmins':
                row_value = each_row
                break
        z[1] = z[1] + '[' + str(each_row) + ']' + '/div/div[' + str(delete_index) + ']/div/button'

        # z[1] = //div[@class = 'orangehrm-container']/div/div[2]/div
        # each_row = 3
        # delete_index = 6
        # //div[@class = 'orangehrm-container']/div/div[2]/div[3]/div/div[6]/div

        actions_column_icons_count = driver.find_elements(z[0], value=z[1])
        print(len(actions_column_icons_count))
        for action_column_icon in range(len(actions_column_icons_count)):
            action_column_icon_attr_value = z[1] + '[' + str(action_column_icon) + ']/i'
            if 'trash' in driver.find_element(z[0], z[1]).get_attribute('class'):
                driver.find_element(z[0], z[1]).click()
                break

        driver.find_element(popup_delete_button[0], popup_delete_button[1]).click()
        time.sleep(10)

        system_user_delete_success_validation = (By.XPATH, "//p[text()='Successfully Deleted']")



    # z = page_table_header_body

