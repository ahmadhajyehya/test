import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture
def get_element():
    driver = webdriver.Chrome(service=Service("<DRIVER_PATH>"))
    driver.get("https://translate.google.com")
    element = driver.find_element(By.CLASS_NAME, value="er8xn")
    return element


def test_example(get_element):
    assert get_element.location['x'] == 10
