# wait for element to disappear
element = WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "er8xn")))

# move focus to element
my_button = self.driver.find_element(By.ID, value="myButton")
        ActionChains(self.driver).move_to_element(my_button).perform()

# force press using javascript_executor
element = self.driver.find_element(By.ID, value="bottom")
    self.driver.execute_script("arguments[0].click();", element)
