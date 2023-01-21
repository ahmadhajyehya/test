from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service("<PATH_TO_DRIVER>"))
driver.get('https://dgotlieb.github.io/CountryList/index.html')
select = Select(driver.find_element(By.ID, value="country"))
select.select_by_value('IL')
select.select_by_index(100)
select.select_by_visible_text('Italy')
driver.quit()
