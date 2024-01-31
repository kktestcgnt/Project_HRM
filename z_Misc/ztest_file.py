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

