from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from translate_page import TranslatePage


class TestTranslatePage(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("<DRIVER_PATH>"))
        self.driver.get('http://translate.google.com')
        self.translate_page = TranslatePage(self.driver)

    def test_translate_box(self):
        self.translate_page.send_text('hello')

    def tearDown(self):
        self.driver.quit()
