from Pages.login_page import LoginClass
from Pages.main_page import HomePage
from Pages.stock_management import StockManagement
import pytest
import time
import allure
import logging

@allure.description("To open a stock management page")
@allure.title("To open a stock management page")
@allure.testcase("TC-0001")
@pytest.mark.parametrize("useremail, password, filter, equal, value", [('pandiarajs2000@gmail.com', 'Test@123', 'Disabled','Equals','Yes')])
def test_sidemenu_window_title(driver, useremail, password,filter,equal,value):
    logging.info("To get the sidemenu options list")
    login_form = LoginClass(driver)
    login_form.login_form()
    login_form.login_form_field(useremail, password)
    login_form.alert_window_close()
    stock_page = StockManagement(driver)
    response = stock_page.stock_page_access(filter,equal,value)
    for i in str(response):
        print("Filter Data", i)
    time.sleep(3)