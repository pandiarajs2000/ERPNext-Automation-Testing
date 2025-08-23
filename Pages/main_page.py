from selenium.webdriver.common.by import By
from selenium.webdriver.common.log import Log
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.expand_public_div = (By.XPATH, "//div[contains(@class, 'standard-sidebar-section') and contains(@data-title, 'Personal')]/following-sibling::div[contains(@class, 'standard-sidebar-section') and contains(@data-title, 'Public')]//button[contains(@class, 'btn-reset') and contains(@aria-label, 'Toggle Section: Public')]")
        self.side_menu_option_xpath = (By.XPATH, "//div[contains(@class, 'sidebar-item-container') and contains(@item-public, '1')]/descendant::span[@class='sidebar-item-label']")
        self.side_menu_link_xpath = (By.XPATH,"//div[contains(@class, 'sidebar-item-container') and contains(@item-public, '1')]/descendant::a")
    
    def hide_side_menu(self):
        try:
            side_menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.expand_public_div))
            time.sleep(5)
            self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/before_side_menu_close.png")
            side_menu.click()
            self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/after_side_menu_close.png")
            time.sleep(5)
        except ElementClickInterceptedException as e:
            print("Element is not clickable", e)

    def side_menu_options(self):
        side_menu_list = []
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.side_menu_option_xpath))
        side_menu_text = self.driver.find_elements(*self.side_menu_option_xpath)
        for row in side_menu_text:
            text = row.text.strip()
            # print(text)
            time.sleep(1)
            side_menu_list.append(text)
        return side_menu_list
    
    def side_menu_open_new_window(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.side_menu_link_xpath))
        side_menu_link = self.driver.find_elements(*self.side_menu_link_xpath)
        links = []
        for att in side_menu_link:
            attr = att.get_attribute("href")
            links.append(attr)
            time.sleep(1)
        
        # open a url to separate window
        for new_window in links:
            self.driver.execute_script(f"window.open('{new_window}','_blank');")
            time.sleep(5)
        
        window_titles = []
        child_window = self.driver.window_handles
        for titles in child_window:
            self.driver.switch_to.window(titles)
            window_titles.append(self.driver.title)
        return links
    
    def side_menu_title(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.side_menu_link_xpath))
        side_menu_link = self.driver.find_elements(*self.side_menu_link_xpath)
        links = []
        for att in side_menu_link:
            attr = att.get_attribute("href")
            links.append(attr)
            time.sleep(1)
        
        # open a url to separate window
        for new_window in links:
            self.driver.execute_script(f"window.open('{new_window}','_blank');")
            time.sleep(5)
        
        window_titles = []
        child_window = self.driver.window_handles
        for titles in child_window:
            self.driver.switch_to.window(titles)
            window_titles.append(self.driver.title)
        return window_titles
    
    def side_menu_close_except_parent(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.side_menu_link_xpath))
        side_menu_link = self.driver.find_elements(*self.side_menu_link_xpath)
        links = []
        for att in side_menu_link:
            attr = att.get_attribute("href")
            links.append(attr)
            time.sleep(1)
        
        # open a url to separate window
        for new_window in links:
            self.driver.execute_script(f"window.open('{new_window}','_blank');")
            time.sleep(5)
        
        # define the parent window
        parent_window = self.driver.current_window_handle

        window_titles = []
        child_window = self.driver.window_handles
        for titles in child_window:
            self.driver.switch_to.window(titles)
            window_titles.append(self.driver.title)
            cur_url = self.driver.current_url
            if titles != parent_window:
                self.driver.switch_to.window(titles)
                self.driver.close()

        return window_titles