import time

from selenium.webdriver.common.by import By
from common.common import BaseClass


def test_handling_multiple_windows(multiple_window_setup):

    driver = multiple_window_setup
    obj_baseclass = BaseClass()
    obj_baseclass.driver = driver

    hrm_main_page = (By.XPATH, "//a[@href = 'http://www.orangehrm.com']")

    parent_window_handle = driver.current_window_handle
    print(parent_window_handle)

    driver.find_element(hrm_main_page[0], value=hrm_main_page[1]).click()
    driver.implicitly_wait(5)
    # time.sleep(5)

    child_window_handles = driver.window_handles

    for handle in child_window_handles:
        if handle != parent_window_handle:
            driver.switch_to.window(handle)
            # Add Validation
            # driver.implicitly_wait(5)
            # time.sleep(5)
            hrm_open_source_page = (By.XPATH, "//a[@href = '/en/orangehrm-starter-open-source-software/' and contains(text(), 'Open Source HRMS')]")
            hrm_open_source_page_element = driver.find_element(hrm_open_source_page[0], hrm_open_source_page[1])

            driver.execute_script("arguments[0].scrollIntoView(true);", hrm_open_source_page_element)
            # driver.implicitly_wait(3)
            # time.sleep(3)
            obj_baseclass.explicit_wait_hrm(10, hrm_open_source_page)
            # Explicit and Implicit waits are not working. Check WHY ?


            hrm_open_source_page_element.click()

            # time.sleep(5)
            child_window_handles2 = driver.window_handles
            driver.switch_to.window(driver.window_handles[-1])
            # Add Validation
            child_window_handles.append(child_window_handles2[-1])
            parent_window_handle = child_window_handles2[-1]

    time.sleep(5)
    print("Child handles 2   ==========================", child_window_handles2)
    for each in child_window_handles2[::-1]:
        if each != child_window_handles2[0]:
            print(each)
            driver.switch_to.window(each)
            driver.close()
            time.sleep(5)

    driver.switch_to.window(child_window_handles2[0])

    time.sleep(10)

