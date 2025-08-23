from selenium.webdriver.common.by import By
from selenium.webdriver.common.log import Log
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class LoginClass:
    def __init__(self, driver):
        self.driver = driver
        self.email_field_xpath = (By.XPATH, "//form/descendant::input[@id='login_email']")
        self.password_field_xpath = (By.XPATH, "//form/descendant::input[@id='login_password']")
        self.password_show_xpath = (By.XPATH, "//form[contains(@class, 'form-signin') and contains(@class, 'form-login')]/descendant::div[@class='password-field']//span")
        self.login_btn_xpath = (By.XPATH, "//form[contains(@class, 'form-signin') and contains(@class, 'form-login')]/descendant::div[@class='page-card-actions']//button")
        self.popup_input = (By.XPATH, "//div[@class='form-group']/descendant::input[contains(@data-fieldname, 'password')]")
        self.popup_password_show = (By.XPATH, "//div[@class='form-group']/descendant::div[@class='toggle-password']")
        self.popup_submit_btn = (By.XPATH, "//div[@class='form-group']/descendant::button[contains(@data-fieldname, 'submit')]")
        self.popup_label = (By.XPATH, "//div[@class='form-group']/child::div[@class='clearfix']//label[@class='control-label reqd']")
        self.invalid_login = (By.XPATH, "//div[@class='modal-header']/descendant::h4[contains(text(), 'Invalid Credentials')]")
        self.popup_close_xpath = (By.XPATH, "//div[@class='modal-actions']/descendant::button[@data-dismiss='modal']")
        self.search_box_xpath = (By.XPATH, "//form[contains(@role, 'search')]/descendant::input[@id='navbar-search']")

    # login function
    def login_form(self):
        self.driver.get("http://127.0.0.1:8000/#login")
        time.sleep(3)
        self.driver.get_screenshot_as_file("E:\\Erpnext Automation\\Screenshots\\login.png")
        site_url = self.driver.current_url
        return site_url
    def login_form_field(self, user_email, password):
        self.driver.find_element(*self.email_field_xpath).send_keys(user_email)
        self.driver.find_element(*self.password_field_xpath).send_keys(password)
        print("User Email",user_email)
        login_btn = self.driver.find_elements(*self.login_btn_xpath)
        for login in login_btn:
            print("Login Text",login.text)
            if login.text.strip() == "Login":
                login.click()
        self.driver.get_screenshot_as_file("E:\\Erpnext Automation\\Screenshots\\login_success.png")
        time.sleep(10)
    def alert_window_handle(self, password):
        try:
            print("Alert Window")
            popup_password_box = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.popup_input))
            popup_password_box.send_keys(password)
            self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/missing_password_popup_filled.png")
            popup_submit = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.popup_submit_btn))
            popup_submit.click()
            time.sleep(10)
            self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/password_failed.png")
            invalid_login_data = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.invalid_login))
            print(f"Invalid Login => {invalid_login_data.text}")
            actual_text = invalid_login_data.text.strip()
            time.sleep(5)
            return actual_text
        except Exception as e:
            print('Message -> No Prompt Alert Presented..')
            self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/missing_password_popup_error.png")

    # alert window close
    def alert_window_close(self):
        try:
            print("Alert Window")
            self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/before _close_popup.png")
            popup_close = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.popup_close_xpath))
            popup_close.click()
            time.sleep(5)
            self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/after_popup_closed.png")
        except Exception as e:
            print('Message -> No Prompt Alert Presented..')
            self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/pop_up_not_close.png")
    
    def home_page(self,search_input_data):
        self.driver.implicitly_wait(5)
        self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/main_page.png")
        search_input = self.driver.find_element(*self.search_box_xpath)
        search_input.send_keys(search_input_data)
        time.sleep(5)
        search_input.send_keys(Keys.ENTER)
        time.sleep(5)