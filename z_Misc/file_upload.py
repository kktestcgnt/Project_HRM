import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller

"""
Reference links:
https://www.youtube.com/watch?v=szb7hmv6kG4
https://www.youtube.com/watch?v=szb7hmv6kG4
https://stackabuse.com/bytes/get-the-root-project-directory-path-in-python/
https://www.youtube.com/watch?v=jLfQHIPulyQ
"""


def file_upload():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)

    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(10)

    username = (By.XPATH, "//input[@name = 'username']")
    password = (By.XPATH, "//input[@name = 'password']")
    login_btn = (By.XPATH, "//button[text() = ' Login ']")
    pim_tab = (By.XPATH, "//span[text() = 'PIM']")
    pim_user_add_btn = (By.XPATH, "//button[text() = ' Add ']")
    pim_user_upload_file_btn = (By.XPATH, "//button[contains(@class, 'employee-image-action')]/i")

    driver.find_element(username[0], value=username[1]).send_keys("Admin")
    time.sleep(3)
    driver.find_element(password[0], value=password[1]).send_keys("admin123")
    time.sleep(3)
    driver.find_element(login_btn[0], value=login_btn[1]).click()
    time.sleep(5)
    driver.find_element(pim_tab[0], value=pim_tab[1]).click()
    time.sleep(3)
    driver.find_element(pim_user_add_btn[0], pim_user_add_btn[1]).click()
    time.sleep(3)
    driver.find_element(pim_user_upload_file_btn[0], pim_user_upload_file_btn[1]).click()
    time.sleep(5)

    keyboard = Controller()

    # keyboard.type("../z_Misc/files/upload_pim_picture.png")
    root_dir = os.path.dirname(os.path.abspath(__file__))
    print(root_dir)
    # keyboard.type("H:\\Python_Projects\\Project_HRM\\z_Misc\\files\\upload_pim_picture.png")
    keyboard.type(root_dir + "\\files\\upload_pim_picture.png")
    time.sleep(5)
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.release(Key.enter)
    time.sleep(5)


file_upload()
