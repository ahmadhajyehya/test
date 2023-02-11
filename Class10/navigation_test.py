import time
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestTranslatePage(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service('<DRIVER_PATH>'))
        cls.driver.get('https://dgotlieb.github.io/Selenium-Extra/js-popups.html')

    def test_alert(self):
        self.driver.find_element(By.ID, value="alert").click()
        time.sleep(3)  # todo this is here just to slow down test!
        self.driver.switch_to.alert.accept()

    def test_confirm(self):
        self.driver.find_element(By.ID, value="confirm").click()
        time.sleep(3)  # todo this is here just to slow down test!
        self.driver.switch_to.alert.dismiss()

    def test_prompt(self):
        self.driver.find_element(By.ID, value="prompt").click()
        time.sleep(3)  # todo this is here just to slow down test!
        self.driver.switch_to.alert.send_keys("jack")
        time.sleep(3)  # todo this is here just to slow down test!
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
