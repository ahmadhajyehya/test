import unittest

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestTranslatePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("<DRIVER_PATH>"))
        self.driver.get('https://translate.google.com')

    def test_translate_page(self):
        self.driver.find_element(By.CLASS_NAME, value="er8xn").click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def tearDown(self):
        self.driver.quit()
