from Pages.login_page import LoginClass
from Pages.main_page import HomePage
from Pages.stock_management import StockManagement
from Utils.utils import read_data,write_data
import pytest
import time
import allure
import logging
import pandas as pd
import logging

logger = logging.getLogger(__name__)


@allure.description("To open a stock management page")
@allure.title("To open a stock management page")
@allure.testcase("TC-0001")
@pytest.mark.parametrize("useremail, password", [('pandiarajs2000@gmail.com', 'Test@123')])
def test_sidemenu_window_title(driver, useremail, password):
    logging.info("To get the sidemenu options list")
    login_form = LoginClass(driver)
    login_form.login_form()
    login_form.login_form_field(useremail, password)
    login_form.alert_window_close()
    stock_page = StockManagement(driver)
    response = stock_page.stock_page_access()
    for i in str(response):
        print("Filter Data", i)
    time.sleep(3)

@allure.description("To create an New Item")
@allure.title("To open a stock management page")
@allure.testcase("TC-0001")
@pytest.mark.parametrize("useremail, password", [('pandiarajs2000@gmail.com', 'Test@123')])
def test_create_new_item(driver, useremail, password, excel_sheet):
    logger.info("Login")
    login_form = LoginClass(driver)
    login_form.login_form()
    login_form.login_form_field(useremail, password)
    login_form.alert_window_close()
    logger.info("Alert Window Closed..")
    stock_page = StockManagement(driver)
    logger.info("Open a Stock Workspace.")
    stock_page.stock_page_access()
    time.sleep(5)
    excel_sheet = excel_sheet
    sheet_name = "Item"
    response = stock_page.add_item(excel_sheet, sheet_name)
    expected_msg = "Saved"
    if response["success"]:
        logger.info("Response", response['success'])
        status = "PASS"
        comment = response['success']
        assert response["success"] == expected_msg, f"Actual Error Message {response['success']}"
    elif response["error_msg"]:
        status = "FAIL"
        comment= response["error_msg"]
    else:
        status = "Error"
        comment = "None of these above"

    write_data(excel_sheet,sheet_name, row=2, column=28,data = status,col2=30, value2=comment)