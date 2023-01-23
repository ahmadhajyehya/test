from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("<DRIVER_PATH>"))
driver.get("https://dgotlieb.github.io/RelativeLocator/index.html")

elements = driver.find_elements(locate_with(By.TAG_NAME, "input"))
# sending text to the first element in the list
elements[0].send_keys("hello")

# iterating through the list and printing the item location (y)
for element in elements:
    print(element.location['y'])

driver.quit()
