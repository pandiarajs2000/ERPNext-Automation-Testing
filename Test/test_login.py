from Pages.login_page import LoginClass
import pytest
import time
import allure
import logging

logging.basicConfig(
    filename="test_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# logger = logging.getLogger('selenium')

@allure.description("To verify the login page")
@allure.step("To open a site url and give")
@allure.title("To verify the single user login success or fail")
@allure.testcase("TC-0001")
@pytest.mark.parametrize("useremail, password", [('pandiarajs2000@gmail.com', 'Test@123')])
def test_login_page(driver, useremail, password):
    logging.info("To verify the single user login pass or fail")
    login_form = LoginClass(driver)
    res = login_form.login_form()
    login_form.login_form_field(useremail, password)
    actual_text = login_form.alert_window_handle(password)
    time.sleep(3)
    expected_text = "Login Success"
    print("Site Url", res)
    print(actual_text)
    assert actual_text in expected_text, f"Expected as 'Login Success' but got '{actual_text}'"

@allure.description("To verify the login page with skip the popup window")
@allure.step("To open a site url and give")
@allure.step("To send the email_id and password to the login form")
@allure.step("To click the submit button")
@allure.title("To verify the another user login success or fail")
@allure.testcase("TC-0002")
@pytest.mark.parametrize("useremail, password", [('pandiarajs2000@gmail.com', 'Test@123')])
def test_login_page_success_case(driver, useremail, password):
    logging.info("To verify the single user login pass or fail")
    login_form = LoginClass(driver)
    login_form.login_form()
    login_form.login_form_field(useremail, password)
    login_form.alert_window_close()
    time.sleep(3)

@allure.description("To verify the home page navbar")
@allure.step("To open a site url and give")
@allure.step("To send the email_id and password to the login form")
@allure.step("To click the submit button")
@allure.step("Enter a Doctype to the search box")
@allure.title("To verify the another user login success or fail")
@allure.testcase("TC-0003")
@pytest.mark.parametrize("useremail, password, search_data", [('pandiarajs2000@gmail.com', 'Test@123', "Lead List")])
def test_search_box(driver, useremail, password, search_data):
    logging.info("To verify the single user login pass or fail")
    login_form = LoginClass(driver)
    login_form.login_form()
    login_form.login_form_field(useremail, password)
    login_form.alert_window_close()
    login_form.home_page(search_data)
    time.sleep(3)