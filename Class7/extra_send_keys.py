from selenium.webdriver.common.keys import Keys

# send a keyboard key to element
driver.find_element(By.ID, value="element").send_keys(Keys.ENTER)


# send a file
driver.find_element(By.ID, value="element").send_keys('C:\\Users\\user\\Desktop\\1.txt')
