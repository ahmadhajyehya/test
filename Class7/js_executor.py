
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("<DRIVER_PATH>"))
driver.get('https://dgotlieb.github.io/RelativeLocator/index.html')
element = driver.find_element(By.ID, value="bottom")
driver.execute_script("arguments[0].scrollIntoView();", element)

driver.execute_script('alert("This is an alert!!");')

driver.quit()
