import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from common.common import BaseClass


@pytest.fixture()
def setup(request):
    read_data = BaseClass()
    login_creds = read_data.get_data()

    app_url = login_creds['app_login_page']["app_url"]
    usr_name = login_creds['app_login_page']["user_id"]
    usr_pwd = login_creds['app_login_page']["user_pwd"]

    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)

    driver.maximize_window()
    driver.get(app_url)
    time.sleep(5)

    username = (By.XPATH, "//input[@name = 'username']")
    password = (By.XPATH, "//input[@name = 'password']")
    login_btn = (By.XPATH, "//button[text() = ' Login ']")

    driver.find_element(username[0], value=username[1]).send_keys(usr_name)
    time.sleep(3)
    driver.find_element(password[0], value=password[1]).send_keys(usr_pwd)
    time.sleep(3)
    driver.find_element(login_btn[0], value=login_btn[1]).click()
    time.sleep(5)

    request.cls.driver = driver
    print("Driver from Fixture : ", driver)

    yield
    # add teardown code
