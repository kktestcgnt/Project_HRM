import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
Reference links:
https://demo.guru99.com/test/delete_customer.php
https://stackoverflow.com/questions/11349189/handling-pop-up-with-many-buttons-using-selenium-webdriver
"""


def handling_alerts():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)

    driver.maximize_window()
    driver.get("https://demo.guru99.com/test/delete_customer.php")
    time.sleep(5)

    obj_alert = Alert(driver)

    driver.find_element(by=By.XPATH, value="//input[@name = 'cusid']").send_keys('12345')
    driver.find_element(by=By.XPATH, value="//input[@name = 'submit']").click()
    time.sleep(2)

    obj_alert.accept()
    time.sleep(3)
    obj_alert.accept()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="//input[@name = 'cusid']").send_keys('34567')
    driver.find_element(by=By.XPATH, value="//input[@name = 'submit']").click()
    time.sleep(3)

    obj_alert.dismiss()

    time.sleep(5)


handling_alerts()
