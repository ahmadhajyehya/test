import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service("<DRIVER_PATH>"))
    driver.get('https://dgotlieb.github.io/RelativeLocator/index.html')
    yield driver
    driver.quit()


def test_double_click(driver):
    action = ActionChains(driver)
    my_button = driver.find_element(By.ID, value="myButton")
    action.double_click(my_button)
    action.perform()


def test_move_to_element(driver):
    action = ActionChains(driver)
    my_button = driver.find_element(By.ID, value="myButton")
    action.move_to_element(my_button)
    action.perform()


def test_select_multiple(driver):
    action = ActionChains(driver)
    my_button = driver.find_element(By.ID, value="myButton")
    action.click_and_hold(on_element=my_button).click_and_hold(on_element=my_button)
    action.perform()
