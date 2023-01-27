# Selenium webdriver

## 1. Download ChromeDriver:

###   A. Check your Google Chrome version:
![alt text](https://github.com/Dgotlieb/Selenium-Java/blob/master/images/About.png)

![alt text](https://github.com/Dgotlieb/Selenium-Java/blob/master/images/version.png)


###   B. Download the ChromeDriver matching your Google Chrome from:
https://sites.google.com/chromium.org/driver/downloads


----------------------------------------------------------------------------

## 2. Add Selenium Webdriver libraries:
### A. Go to [selenium PyPi page](https://pypi.org/project/selenium/) to check for the latest version 
### B. Run `$ poetry add selenium==4.7.2`


* we can of course use `$ pip install selenium`
----------------------------------------------------------------------------

## 3. Add WebDriver code:
### A. Create a new file and name it: WebTest
### B. Copy the below code into tour class:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("<PATH_TO_CHROMEDRIVER>"))
```
    
### C. Change the <PATH_TO_CHROMEDRIVER> to the real path your chromedriver.exe file is in (without deleting chromedriver.exe).

