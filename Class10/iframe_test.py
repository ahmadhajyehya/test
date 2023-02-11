import time
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestTranslatePage(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service('<DRIVER_PATH>'))
        cls.driver.get('https://dgotlieb.github.io/Selenium-Extra/iFrames.html')

    def test_alert(self):
        self.driver.find_element(By.ID, value="alert").click()

        time.sleep(3)  # todo this is here just to slow down test!
        self.driver.switch_to.alert.accept()

    def test_fail(self):
        print("We know it will fail...")
        self.driver.find_element(By.ID, value="iframe_alert").click()

    def test_iframe(self):
        print("Switching to iFrame...")
        self.driver.switch_to.frame('my_frame')
        self.driver.find_element(By.ID, value="iframe_alert").click()
        self.driver.switch_to.alert.accept()

    def test_switch_back(self):
        print("Switching back...")
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, value="alert").click()
        self.driver.switch_to.alert.accept()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
