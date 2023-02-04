from selenium.webdriver.common.by import By
from base_page import BasePage


class TranslatePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver.get('http://translate.google.com')

    def click_text_area(self):
        self.click_element(By.CLASS_NAME, 'er8xn')

    def send_keys_to_text_area(self):
        self.enter_text(By.CLASS_NAME, 'er8xn', 'hello')
