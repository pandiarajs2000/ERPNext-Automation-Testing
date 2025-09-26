from selenium import webdriver
import time
import pytest
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("test_log.log"),   # write to file
        logging.StreamHandler()                # print to console
    ]
)
logger = logging.getLogger(__name__)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    print("Setup the Browser")
    logger.info("Browser is open..")
    driver.maximize_window()
    yield driver
    print("\nTear Down for closing the browser")
    logger.info("Site was closed")
    driver.quit()

@pytest.fixture
def excel_sheet():
    excel_path = "E:\Erpnext Automation\Master_Data.xlsx"
    return excel_path