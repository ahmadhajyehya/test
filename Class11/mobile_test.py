import time
from unittest import TestCase
from appium.options.android import UiAutomator2Options
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTranslatePage(TestCase):
    def setUp(self):
        options = UiAutomator2Options()
        options.platformVersion = '11'
        options.app_package = 'com.android.chrome'
        options.app_activity = 'com.google.android.apps.chrome.Main'
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', options=options)
        self.driver.implicitly_wait(10)

    def test_alert(self):
        self.driver.find_element(By.ID, value="com.android.chrome:id/terms_accept").click()
        self.driver.find_element(By.ID, value="com.android.chrome:id/negative_button").click()
        self.driver.find_element(By.ID, value="com.android.chrome:id/search_box_text").click()
        self.driver.find_element(By.ID, value="com.android.chrome:id/url_bar").send_keys('hello')
        time.sleep(5)  # to see the results

    def tearDown(self):
        self.driver.quit()
