from selenium.webdriver.common.by import By
from selenium.webdriver.common.log import Log
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time

class StockManagement:
    def __init__(self, driver):
        self.driver = driver
        self.stock_link_xpath = (By.XPATH,"//div[contains(@class, 'sidebar-item-container') and contains(@item-public, '1')]/descendant::a[contains(@title, 'Stock')]")
        self.stock_workspace_scroll = (By.XPATH, "//div[@class='col layout-main-section-wrapper']/child::div[@class='layout-main-section']")
        self.item_click_xpath = (By.XPATH, "//div[@class='ce-block__content']/child::div[contains(@shortcut_name, 'Item')]/descendant::span[contains(@title, 'Item') and contains(@class, 'ellipsis')]")
        self.filter_set_xpath = (By.XPATH, "//div[@class='filter-selector']/descendant::button[contains(@class, 'filter-button') and contains(@class, 'btn-primary-light')]")
        self.add_filter_btn = (By.XPATH, "//div[contains(@class, 'popover-body') and contains(@class, 'popover-content')]/descendant::div[contains(@class, 'filter-action-buttons') and contains(@class, 'mt-2')]//button[contains(text(), '+ Add a Filter')]")

        # add item btn
        self.item_add_btn = (By.XPATH, "//button[contains(@data-label,'Add Item')]")
        self.item_add_full_form = (By.XPATH, "//div[@class='modal-dialog']//div[@class='modal-content']/child::div[@class='modal-footer']//div[@class='custom-actions']//button")
        self.item_code_xpath = (By.XPATH, "//div[contains(@data-fieldname,'__section_1')]//descendant::form//div[contains(@class, 'frappe-control') and contains(@class, 'input-max-width') and contains(@data-fieldname, 'item_code')]/descendant::div[@class='control-input']//input[contains(@data-fieldname, 'item_code') and contains(@type, 'text') and contains(@data-doctype, 'Item')]")
        self.item_group_xpath = (By.XPATH, "//div[contains(@data-fieldname,'__section_1')]/descendant::form//div[contains(@class, 'frappe-control') and contains(@class, 'input-max-width') and contains(@data-fieldname, 'item_group')]/descendant::div[@class='awesomplete']//input[contains(@data-fieldname, 'item_group') and contains(@type, 'text') and contains(@data-doctype, 'Item')]")
        self.save_btn_xpath = (By.XPATH, "//div[@class='container']/child::div[contains(@class, 'row') and contains(@class, 'flex') and contains(@class, 'align-center') and contains(@class, 'justify-between') and contains(@class, 'page-head-content')]/child::div[contains(@class, 'col') and contains(@class, 'flex') and contains(@class, 'justify-content-end') and contains(@class, 'page-actions')]/descendant::button[contains(@data-label, 'Save')]")
    
    def stock_page_access(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.stock_link_xpath))
        side_menu_link = self.driver.find_element(*self.stock_link_xpath)
        side_menu_link.click()
        time.sleep(3)
        workspace_scroll = self.driver.find_element(*self.stock_workspace_scroll)
        scroll_origin = ScrollOrigin.from_element(workspace_scroll)
        ActionChains(self.driver).scroll_from_origin(scroll_origin,0, 100).perform()

        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.item_click_xpath))
        move_to_ele = self.driver.find_element(*self.item_click_xpath)
        ActionChains(self.driver).move_to_element(move_to_ele).perform()
        self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/item_text.png")
        time.sleep(3)
        move_to_ele.click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.filter_set_xpath))
        time.sleep(2)
        self.driver.find_element(*self.filter_set_xpath).click()
        self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/filter_access.png")
        time.sleep(5)

    def add_item(self, item_group, item_code):
        add_item = self.driver.find_element(*self.item_add_btn)
        add_item.click()
        time.sleep(5)
        item_popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.item_add_full_form))
        item_popup.click()
        self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/item_add_full_form.png")
        time.sleep(5)

        item_code = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.item_code_xpath))
        item_code.send_keys(item_code)
        
        item_group = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.item_group_xpath))
        item_group.send_keys(item_group)

        time.sleep(5)

        self.driver.find_element(self.save_btn_xpath).click()
        time.sleep(5)