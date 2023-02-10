from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json


class TestTranslatePage(TestCase):
    def setUp(self):
        json_file = open('config.json', 'r')
        data = json.load(json_file)
        browser = data['browserType']
        if browser == 'chrome':
            self.driver = webdriver.Chrome(service=Service('<CHROMEDRIVER_PATH>'))
        elif browser == 'firefox':
            self.driver = webdriver.Firefox(service=Service('FIREFOXDRIVER_PATH'))

        self.driver.get('https://translate.google.com')

    def test_waits(self):
        self.driver.find_element(By.CLASS_NAME, value="er8xn").click()

    def tearDown(self):
        self.driver.quit()
