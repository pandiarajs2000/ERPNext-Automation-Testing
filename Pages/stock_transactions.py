from selenium.webdriver.common.by import By
from selenium.webdriver.common.log import Log
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, InvalidElementStateException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import traceback
import time
from datetime import datetime
import openpyxl
import pdb
import logging

logger = logging.getLogger(__name__)

class StockTransaction:
    def __init__(self,driver):
        self.driver = driver
        self.stock_link_xpath = (By.XPATH,"//a[@title='Stock']")
        self.stock_workspace_scroll = (By.XPATH, "//div[@class='layout-main-section']")
        self.stock_transactions_cards = (By.XPATH, "//div[@card_name='Stock Transactions']")
        self.stock_transactions_cards_list = (By.XPATH, "//div[@card_name='Stock Transactions']/descendant::span[@class='link-text']")

        # xpath for Material Request Screen
        self.search_box_xpath = (By.XPATH, "//input[@id='navbar-search']")
        self.add_material_request = (By.XPATH, "//button[@data-label='Add Material Request']")


    def stock_transactions_cards_list_data(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.stock_link_xpath))
        side_menu_link = self.driver.find_element(*self.stock_link_xpath)
        side_menu_link.click()
        time.sleep(3)
        workspace_scroll = self.driver.find_element(*self.stock_workspace_scroll)
        scroll_origin = ScrollOrigin.from_element(workspace_scroll)
        ActionChains(self.driver).scroll_from_origin(scroll_origin,0, 100).perform()

        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.stock_transactions_cards))
        move_to_ele = self.driver.find_element(*self.stock_transactions_cards)
        ActionChains(self.driver).move_to_element(move_to_ele).perform()
        self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/stock_transactions_cards.png")
        time.sleep(3)
        move_to_ele.click()

        time.sleep(2)

        self.driver.execute_script("""
        document.querySelectorAll('a').forEach(a => {
            a.addEventListener('click', e => e.preventDefault());
        });
    """)

        cards_list = WebDriverWait(self.driver, 10).until(
        EC.presence_of_all_elements_located(self.stock_transactions_cards_list))

        # Fetch text safely without clicking
        card_texts = []
        for card in cards_list:
            text = self.driver.execute_script("return arguments[0].textContent;", card).strip()
            if text:
                card_texts.append(text)

        return card_texts

    def open_mr_page(self):
        logger.info("Search Box Open..")
        search_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_box_xpath))
        search_input.send_keys('Material Request List')
        logger.info("Search Box Input Send")
        time.sleep(1)
        search_input.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(3)
        add_mr = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_material_request))
        logger.info("Add Button Click")
        add_mr.click()
        logger.info("Open a Material Request Screen.")
        # take a screenshot
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"E:/Erpnext Automation/Screenshots/screenshot_{timestamp}.png"

        self.driver.save_screenshot(screenshot_path)
        return self.driver.current_url