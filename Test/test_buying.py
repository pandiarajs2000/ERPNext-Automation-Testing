from Pages.login_page import LoginClass
from Pages.main_page import HomePage
from Pages.stock_transactions import StockTransaction
from Utils.utils import read_data,write_data
import pytest
import time
import allure
import logging
import pandas as pd
import logging

logger = logging.getLogger(__name__)

@allure.description("To open a stock management page")
@allure.title("To open a stock management page and get all the link for the stock transactions")
@allure.step("1. Go to the local site")
@allure.step("2. Enter the end user email and password and click to the login button")
@allure.step("3. Search the Stock module in the sidemenu")
@allure.step("4. Click the Stock module and access the workspace in the right side and scroll to the stock transaction cards list")
@allure.testcase("TC-0001")
@pytest.mark.parametrize("useremail, password", [('pandiarajs2000@gmail.com', 'Test@123')])
def test_get_stock_trans_link(driver, useremail, password):
    login_form = LoginClass(driver)
    login_form.login_form()
    login_form.login_form_field(useremail, password)
    login_form.alert_window_close()
    stock_page = StockTransaction(driver)
    response = stock_page.stock_page_access()
    print(response)
    time.sleep(3)