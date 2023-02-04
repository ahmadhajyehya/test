from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTranslatePage(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("<DRIVER_PATH>"))
        self.driver.get('http://translate.google.com')
        # implicit wait
        self.driver.implicitly_wait(10)
        # page load timeout
        self.driver.set_page_load_timeout(10)

    def test_explicit_wait(self):
        # explicit wait
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME, "er8xn")))
        element.send_keys('helo')

    def tearDown(self):
        self.driver.quit()
