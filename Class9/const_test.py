from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Constants:
    BUTTON_CLASS = "er8xn"


class TestTranslatePage(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("<DRIVER_PATH>"))
        self.driver.get('http://translate.google.com')

    def test_consts(self):
        self.driver.find_element(By.ID, value=Constants.BUTTON_CLASS).send_keys('er8xn')

    def tearDown(self):
        self.driver.quit()
