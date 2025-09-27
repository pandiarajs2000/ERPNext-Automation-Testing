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
    rows = 3
    response = stock_page.add_item(excel_sheet, sheet_name, rows)
    expected_msg = "Enabled"
    try:
        if response.get("success"):

            assert response.get("success") == expected_msg, f"Actual Error Message {response.get('success')}, Expected Message: {response.get('error')}"
            # logger.info("Response", response.get("success"))
            status = "PASS"
            comment = response['success']
        elif response.get("error"):
            status = "FAIL"
            comment= response.get("error")
            assert False, f"Unexpected Error Message: {response.get('error')}"
        else:
            status = "Error"
            comment = "None of these above"
            assert False, "Neither success nor error message was returned"
    except Exception as e:
        status = "Fail"
        comment = str(e)
        raise
    
    write_data(excel_sheet,sheet_name, row=rows, column=28,data = status,col2=30, value2=comment)


@allure.description("Create a new Item without barcode")
@allure.title("Create a new Item without barcode")
@allure.testcase("TC-0002")
@pytest.mark.parametrize("useremail, password", [('pandiarajs2000@gmail.com', 'Test@123')])
def test_create_new_item_without_barcode(driver, useremail, password, excel_sheet):
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
    rows = 3
    response = stock_page.add_item(excel_sheet, sheet_name, rows)
    expected_msg = "Enabled"
    try:
        if response.get("success"):
            assert response.get("success") == expected_msg, f"Actual Error Message {response.get('success')}, Expected Message: {response.get('error')}"
            logger.info("Response", response.get("success"))
            status = "PASS"
            comment = response['success']
        elif response.get("error"):
            status = "FAIL"
            comment= response.get("error")
            assert False, f"Unexpected Error Message: {response.get('error')}"
        else:
            status = "Error"
            comment = "None of these above"
            assert False, "Neither success nor error message was returned"
    except Exception as e:
        status = "Fail"
        comment = str(e)
        raise
    
    write_data(excel_sheet,sheet_name, row=rows, column=28,data = status,col2=30, value2=comment)


@allure.description("Existing Item Should not be added")
@allure.title("Existing Item Should not be added")
@allure.testcase("TC-0003")
@pytest.mark.parametrize("useremail, password", [('pandiarajs2000@gmail.com', 'Test@123')])
def test_existing_item_validation(driver, useremail, password, excel_sheet):
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
    rows = 4
    response = stock_page.add_item(excel_sheet, sheet_name, rows)
    expected_msg = "Enabled"
    try:
        if response.get("success"):
            assert response.get("success") == expected_msg, f"Actual Error Message {response.get('success')}, Expected Message: {response.get('error')}"
            logger.info("Response", response.get("success"))
            status = "PASS"
            comment = response['success']
        elif response.get("error"):
            status = "FAIL"
            comment= response.get("error")
            assert False, f"Unexpected Error Message: {response.get('error')}"
        else:
            status = "Error"
            comment = "None of these above"
            assert False, "Neither success nor error message was returned"
    except Exception as e:
        status = "Fail"
        comment = str(e)
        raise
    
    write_data(excel_sheet,sheet_name, row=rows, column=28,data = status,col2=30, value2=comment)


@allure.description("Without Item Code the document should not be saved")
@allure.title("Without Item Code the document should not be saved")
@allure.testcase("TC-0004")
@pytest.mark.parametrize("useremail, password", [('pandiarajs2000@gmail.com', 'Test@123')])
def test_existing_item_validation(driver, useremail, password, excel_sheet):
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
    rows = 4
    response = stock_page.add_item(excel_sheet, sheet_name, rows)
    expected_msg = "Enabled"
    try:
        if response.get("success"):
            assert response.get("success") == expected_msg, f"Actual Error Message {response.get('success')}, Expected Message: {response.get('error')}"
            logger.info("Response", response.get("success"))
            status = "PASS"
            comment = response['success']
        elif response.get("error"):
            status = "FAIL"
            comment= response.get("error")
            assert False, f"Unexpected Error Message: {response.get('error')}"
        else:
            status = "Error"
            comment = "None of these above"
            assert False, "Neither success nor error message was returned"
    except Exception as e:
        status = "Fail"
        comment = str(e)
        raise
    finally:
        write_data(excel_sheet,sheet_name, row=rows, column=28,data = status,col2=30, value2=comment)


import logging
import time
import pytest
import allure

logger = logging.getLogger(__name__)

@allure.description("Create an Item without Opening Stock")
@allure.title("Create an Item without Opening Stock")
@allure.testcase("TC-0005")
@pytest.mark.parametrize("useremail, password", [('pandiarajs2000@gmail.com', 'Test@123')])
def test_without_opening_stock(driver, useremail, password, excel_sheet):
    logger.info("==== Test Case: Create an Item without Opening Stock (TC-0005) STARTED ====")

    try:
        # Login
        logger.info("Step 1: Logging in with user: %s", useremail)
        login_form = LoginClass(driver)
        login_form.login_form()
        login_form.login_form_field(useremail, password)
        login_form.alert_window_close()
        logger.info("Login successful and alert window closed.")

        # Navigate to Stock Workspace
        logger.info("Step 2: Navigating to Stock Workspace.")
        stock_page = StockManagement(driver)
        stock_page.stock_page_access()
        time.sleep(5)
        logger.info("Stock Workspace opened successfully.")

        # Add Item
        logger.info("Step 3: Adding item from Excel sheet.")
        sheet_name = "Item"
        rows = 6
        response = stock_page.add_item(excel_sheet, sheet_name, rows)
        logger.info("Response from add_item(): %s", response)

        expected_msg = "Enabled"

        if response.get("success"):
            logger.info("Validation: Checking success message.")
            assert response.get("success") == expected_msg, (
                f"Actual: {response.get('success')} | Expected: {expected_msg}"
            )
            logger.info("Item created successfully with status: %s", response.get("success"))
            status = "PASS"
            comment = response['success']

        elif response.get("error"):
            logger.error("Item creation failed. Error: %s", response.get("error"))
            status = "FAIL"
            comment = response.get("error")
            assert False, f"Unexpected Error Message: {response.get('error')}"

        else:
            logger.error("Neither success nor error returned in response.")
            status = "ERROR"
            comment = "No valid response"
            assert False, "Neither success nor error message was returned"

    except Exception as e:
        status = "FAIL"
        comment = str(e)
        logger.exception("Exception occurred during test execution: %s", e)
        raise

    finally:
        logger.info("Step 4: Writing test result to Excel. Status: %s, Comment: %s", status, comment)
        write_data(
            excel_sheet,
            sheet_name,
            row=rows,
            column=28,
            data=status,
            col2=30,
            value2=comment
        )
        logger.info("==== Test Case: TC-0005 COMPLETED with Status: %s ====", status)
