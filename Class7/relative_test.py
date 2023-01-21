from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("<DRIVER_PATH>"))
driver.get("https://dgotlieb.github.io/RelativeLocator/index.html")

my_button = driver.find_element(By.ID, "myButton")
driver.find_element(locate_with(By.TAG_NAME, "input").above(my_button)).send_keys('above')
driver.find_element(locate_with(By.TAG_NAME, "input").below(my_button)).send_keys('below')
driver.find_element(locate_with(By.TAG_NAME, "input").to_right_of(my_button)).send_keys('tight of')

driver.quit()
