from Pages.login_page import LoginClass
from Pages.main_page import HomePage
import pytest
import time
import allure
import logging

logging.basicConfig(
    filename="Logs/selenium_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@allure.description("To verify the sidemenu options")
@allure.step("To open a site url and give")
@allure.step("To send the email_id and password to the login form")
@allure.step("To click the submit button")
@allure.title("To verify the sidemenu options")
@allure.testcase("TC-0001")
@pytest.mark.parametrize("useremail, password", [('pandiarajs2000@gmail.com', 'Test@123')])
def test_hide_side_menu(driver, useremail, password):
    logging.info("To verify the single user login pass or fail")
    login_form = LoginClass(driver)
    login_form.login_form()
    login_form.login_form_field(useremail, password)
    login_form.alert_window_close()
    home_page = HomePage(driver)
    home_page.hide_side_menu()

@allure.description("To get the sidemenu options list")
@allure.step("To open a site url and give")
@allure.step("To send the email_id and password to the login form")
@allure.step("To click the submit button")
@allure.title("To get the sidemenu options list")
@allure.testcase("TC-0002")
@pytest.mark.parametrize("useremail, password", [('pandiarajs2000@gmail.com', 'Test@123')])
def test_list_out_the_sidemenu_options(driver, useremail, password):
    logging.info("To get the sidemenu options list")
    login_form = LoginClass(driver)
    login_form.login_form()
    login_form.login_form_field(useremail, password)
    login_form.alert_window_close()
    home_page = HomePage(driver)
    print(home_page)
    menu_data = home_page.side_menu_options()
    for data in menu_data:
        print("Menu Options",data)
    links = home_page.side_menu_open_new_window()
    for l_list in links:
        print("Menu Options",l_list)
    time.sleep(3)

@allure.description("To verify the sidemenu open as new window and get the title")
@allure.step("To open a site url and give")
@allure.step("To send the email_id and password to the login form")
@allure.step("To click the submit button")
@allure.title("To verify the sidemenu open as new window and get the title")
@allure.testcase("TC-0003")
@pytest.mark.parametrize("useremail, password", [('pandiarajs2000@gmail.com', 'Test@123')])
def test_sidemenu_window_title(driver, useremail, password):
    logging.info("To get the sidemenu options list")
    login_form = LoginClass(driver)
    login_form.login_form()
    login_form.login_form_field(useremail, password)
    login_form.alert_window_close()
    home_page = HomePage(driver)
    title = home_page.side_menu_title()
    for l_ in title:
        print("Window Title",l_)
    time.sleep(3)

@allure.description("To verify the sidemenu open as new window and close except the parent window")
@allure.title("To verify the sidemenu open as new window and close except the parent window")
@allure.testcase("TC-0004")
@pytest.mark.parametrize("useremail, password", [('pandiarajs2000@gmail.com', 'Test@123')])
def test_close_all_window_except_parent_window(driver, useremail, password):
    logging.info("To get the sidemenu options list")
    login_form = LoginClass(driver)
    login_form.login_form()
    login_form.login_form_field(useremail, password)
    login_form.alert_window_close()
    home_page = HomePage(driver)
    title = home_page.side_menu_close_except_parent()
    for l_ in title:
        print("Window Title",l_)
    time.sleep(3)