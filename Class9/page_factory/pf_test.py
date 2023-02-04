from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from translate_page import TranslatePage


class TestTranslatePage(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("<DRIVER_PATH>"))
        self.driver.get('http://translate.google.com')

    def test_translate(self):
        translate_page = TranslatePage(self.driver)
        translate_page.set_translate_text()

    def tearDown(self):
        self.driver.quit()
