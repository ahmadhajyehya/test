import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestTranslatePage(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service('<DRIVER_PATH>'))
        cls.driver.get('https://translate.google.com')
        cls.handle = cls.driver.current_window_handle

    def test_handles(self):
        self.driver.switch_to.new_window('tab')
        time.sleep(3)  # todo this is here just to slow down test!
        self.driver.switch_to.window(self.handle)
        time.sleep(3)  # todo this is here just to slow down test!

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
