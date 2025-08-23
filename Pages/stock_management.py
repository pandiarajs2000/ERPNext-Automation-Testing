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
        # self.filter_input_xpath = (By.XPATH, "//div[contains(@class, 'list_filter') and contains(@class, 'row')]/descendant::input[contains(@class, 'form-control') and contains(@class, 'input-xs')]")
        self.filters_input_xpath = (By.XPATH, "//div[@class='awesomplete']/child::input[contains(@class, 'form-control') and contains(@class, 'input-xs') and contains(@role, 'combobox') and contains(@aria-owns, 'awesomplete_list_13')]")
        self.filter_condition_xpath = (By.XPATH, "//div[contains(@class, 'list_filter')  and contains(@class, 'row')]/child::div[contains(@class, 'col-sm-3') and contains(@class, 'form-group')]//select")
    
    def stock_page_access(self, filter,equal,value):
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
        
        # filter input
        filter_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.filters_input_xpath))
        filter_input.clear()

        filter_input.send_keys(filter)

        filter_condition = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.filter_condition_xpath))
        select = Select(filter_condition)
        select.select_by_value(equal)

        

        # filters_access = self.driver.find_elements(*self.filters_list_xpath)
        # data = []
        # for i in filters_access:
        #     print(i.text)
        #     data.append(i.text)
        # return data