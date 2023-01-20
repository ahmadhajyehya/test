from selenium import webdriver
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service("<DRIVER_PATH>"))
driver.get("https://www.google.com")
print(driver.current_url)
print(driver.title)
print(driver.page_source)
driver.close()
driver.quit()
driver.forward()
driver.back()
driver.refresh()
