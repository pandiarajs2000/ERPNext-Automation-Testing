from Pages.login_page import LoginClass
from Pages.main_page import HomePage
from Pages.stock_management import StockManagement
import pytest
import time
import allure
import logging
import pandas as pd


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
    logging.info("To get the sidemenu options list")
    login_form = LoginClass(driver)
    login_form.login_form()
    login_form.login_form_field(useremail, password)
    login_form.alert_window_close()
    stock_page = StockManagement(driver)
    stock_page.stock_page_access()
    data_sheet = excel_sheet
    