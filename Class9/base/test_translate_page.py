import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from translate_page import TranslatePage


class TestTranslatePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("<DRIVER_PATH>"))
        self.translate_page = TranslatePage(self.driver)

    def test_translate_page(self):
        self.translate_page.click_text_area()
        self.translate_page.send_keys_to_text_area()

    def tearDown(self):
        self.driver.quit()
