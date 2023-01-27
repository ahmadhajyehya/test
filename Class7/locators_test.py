from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("<DRIVER_PATH>"))
driver.get("https://www.google.com")

# locators
driver.find_element(By.ID, value="watch")
driver.find_element(By.NAME, value="user")
driver.find_element(By.CLASS_NAME, value="test")
driver.find_element(By.TAG_NAME, value="p")

# find multiple elements
elements = driver.find_elements(By.TAG_NAME, value="p")

# text locators
driver.find_element(By.LINK_TEXT, value="Click")
driver.find_element(By.PARTIAL_LINK_TEXT, value="Click Now")

# CSS selector
driver.find_element(By.CSS_SELECTOR, value="div[value=en]")

# XPATH
driver.find_element(By.XPATH, value="//input[@type='submit']")
