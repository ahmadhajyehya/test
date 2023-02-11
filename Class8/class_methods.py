from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestTranslatePage(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service('<DRIVER_PATH>'))
        cls.driver.get('https://translate.google.com')

    def test_alert(self):
        self.driver.find_element(By.CLASS_NAME, value="er8xn").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
