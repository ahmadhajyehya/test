from selenium.webdriver.common.by import By


class TranslatePage():
    def __init__(self, driver):
        self.driver = driver

    def send_text(self):
        self.driver.find_element(By.CLASS_NAME, value="er8xn").send_keys('hello')
