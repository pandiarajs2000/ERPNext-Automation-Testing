from selenium import webdriver
import time
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    print("Setup the Browser")
    driver.maximize_window()
    yield driver
    print("\nTear Down for closing the browser")
    driver.quit()