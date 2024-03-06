import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)

username = (By.XPATH, "//input[@name = 'username']")
password = (By.XPATH, "//input[@name = 'password']")
login_btn = (By.XPATH, "//button[text() = ' Login ']")

driver.find_element(username[0], value=username[1]).send_keys("Admin")
time.sleep(3)
driver.find_element(password[0], value=password[1]).send_keys("admin123")
time.sleep(3)
# driver.find_element(login_btn[0], value=login_btn[1]).click()
time.sleep(3)

# help_button = (By.XPATH, "//i[@class = 'oxd-icon bi-question-lg']")
hrm_main_page = (By.XPATH, "//a[@href = 'http://www.orangehrm.com']")
# hrm_open_source_page = (By.XPATH, "//a[@href = '/en/orangehrm-starter-open-source-software/' and contains(text(), 'Open Source HRMS')]")

parent_window_handle = driver.current_window_handle
print(parent_window_handle)

driver.find_element(hrm_main_page[0], value=hrm_main_page[1]).click()
time.sleep(5)


child_window_handles = driver.window_handles
print("=================================")
print(child_window_handles)
print(id(child_window_handles))

for handle in child_window_handles:
    if handle != parent_window_handle:
        driver.switch_to.window(handle)
        print("first switch HRM MAIN Page - ", driver.current_window_handle)
        time.sleep(10)
        hrm_open_source_page = (By.XPATH, "//a[@href = '/en/orangehrm-starter-open-source-software/' and contains(text(), 'Open Source HRMS')]")
        hrm_open_source_page_element = driver.find_element(hrm_open_source_page[0], hrm_open_source_page[1])
        # print("scroll for click")
        # w = WebDriverWait(driver, 15)
        # w.until(expected_conditions.presence_of_element_located(hrm_open_source_page))
        # w.until(expected_conditions.element_to_be_clickable(hrm_open_source_page))
        # print(driver.find_element(hrm_open_source_page[0], hrm_open_source_page[1]).text)
        # driver.find_element(hrm_open_source_page[0], hrm_open_source_page[1]).click()

        # Actions
        # action = ActionChains(driver)
        # print("before actions click")
        # time.sleep(3)
        # action.click(on_element=hrm_open_source_page_element)
        # action.perform()

        driver.execute_script("arguments[0].scrollIntoView(true);", hrm_open_source_page_element)
        # driver.execute_script("arguments[0].click();", hrm_open_source_page_element)
        print("before execute script click")
        time.sleep(3)
        print("after time sleep")
        hrm_open_source_page_element.click()

        time.sleep(15)
        child_window_handles2 = driver.window_handles
        print("Child handles 2   ==========================", child_window_handles2)
        child_window_handles.append(child_window_handles2[-1])
        print(id(child_window_handles))
        print(driver.current_window_handle)

        parent_window_handle = child_window_handles2[-1]

    else:
        print("in else")

time.sleep(10)




