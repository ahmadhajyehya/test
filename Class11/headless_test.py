from unittest import TestCase
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestTranslatePage(TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service('driver_path'), options=chrome_options)
        self.driver.get('https://translate.google.com')

    def test_alert(self):
        self.driver.find_element(By.CLASS_NAME, value="er8xn").click()

    def tearDown(self):
        self.driver.quit()
