import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from common.common import BaseClass


def test_handling_page_alerts(alerts_setup):
    driver = alerts_setup

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
