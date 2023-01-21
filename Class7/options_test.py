from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(service=Service("/Users/danielgotlieb/Downloads/chromedriver"), options=chrome_options)
driver.get("https://translate.google.com/")
driver.quit()
