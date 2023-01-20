from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("<DRIVER_PATH>"))
driver.get("https://www.google.com")

# actions
driver.find_element(By.ID, value="watch").click()
driver.find_element(By.NAME, value="user").submit()
driver.find_element(By.CLASS_NAME, value="test").send_keys('hello')
driver.find_element(By.TAG_NAME, value="p").clear()
