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
import openpyxl

class StockManagement:
    def __init__(self, driver):
        self.driver = driver
        self.stock_link_xpath = (By.XPATH,"//div[contains(@class, 'sidebar-item-container') and contains(@item-public, '1')]/descendant::a[contains(@title, 'Stock')]")
        self.stock_workspace_scroll = (By.XPATH, "//div[@class='col layout-main-section-wrapper']/child::div[@class='layout-main-section']")
        self.item_click_xpath = (By.XPATH, "//div[@class='ce-block__content']/child::div[contains(@shortcut_name, 'Item')]/descendant::span[contains(@title, 'Item') and contains(@class, 'ellipsis')]")
        # self.filter_set_xpath = (By.XPATH, "//div[@class='filter-selector']/descendant::button[contains(@class, 'filter-button') and contains(@class, 'btn-primary-light')]")
        # self.add_filter_btn = (By.XPATH, "//div[contains(@class, 'popover-body') and contains(@class, 'popover-content')]/descendant::div[contains(@class, 'filter-action-buttons') and contains(@class, 'mt-2')]//button[contains(text(), '+ Add a Filter')]")

        # add item btn
        self.item_add_btn = (By.XPATH, "//button[contains(@data-label,'Add Item')]")
        self.item_add_full_form = (By.XPATH, "//div[@class='modal-dialog']//div[@class='modal-content']/child::div[@class='modal-footer']//div[@class='custom-actions']//button")
        self.add_item_popup = (By.CSS_SELECTOR, "div.modal.show div.modal-dialog")
        self.item_save_popup = (By.XPATH, "//div[@role='dialog']//button[@type='button'][normalize-space()='Save']")
        self.item_code__two_xpath = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'item_code')]")
        self.item_code_xpath = (By.XPATH,"//div[@role='dialog']//div//div//div//div//div//div//div//div//div//form//div[@data-fieldtype='Data']//div//div//div//input[@type='text']")
        self.item_group_xpath = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'item_group')]")
        self.item_group_options = (By.XPATH, "//div[@class='awesomplete']/child::ul[@id='awesomplete_list_3']//div[@role='option']//p")
        self.uom = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'stock_uom')]")
        self.is_stock_item = (By.XPATH, "//div[contains(@data-fieldname, 'column_break0')]/child::form//div[contains(@data-fieldname,'is_stock_item')]")
        self.opening_stock =(By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'opening_stock')]")
        self.valuation_rate = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'valuation_rate')]")
        self.selling_rate = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'standard_rate')]")
        self.collapse_disable = (By.XPATH, "//div[@data-fieldname='section_break_11']/child::div[contains(@class,'section-head') and contains(@class, 'collapsed')]")
        self.collapse_enable = (By.XPATH, "//div[@data-fieldname='section_break_11']/child::div[contains(@class,'section-head') and contains(@class, 'collapsible')]")
        self.description = (By.XPATH, "//div[@class='ql-container ql-snow']//div[@class='ql-editor ql-blank']")
        self.inventory_tab = (By.XPATH, "//ul[@id='form-tabs']/li[contains(@class, 'nav-item') and contains(@class, 'show')]//a[@data-fieldname='inventory_section']")
        self.shelf_days = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'shelf_life_in_days')]")
        self.end_of_life = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'end_of_life')]")
        self.default_mr_type = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[contains(@class, 'control-input')and contains(@class,'flex') and contains(@class, 'align-center')]//select[contains(@data-fieldname,'default_material_request_type')]")
        self.valuation_method = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[contains(@class, 'control-input')and contains(@class,'flex') and contains(@class, 'align-center')]//select[contains(@data-fieldname,'valuation_method')]")
        self.warranty_period = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'warranty_period')]")
        self.weight_per_unit = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'weight_per_unit')]")
        self.weight_uom = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'weight_uom')]")
        self.barcode_row_add_btn = (By.XPATH, "//div[@data-fieldname='barcodes']//button[@type='button'][normalize-space()='Add Row']")
        self.child_table_edit_btn = (By.XPATH, "//div[@class='grid-body']//div[@class='rows']//div[@class='grid-row']//div[contains(@class,'data-row') and contains(@class,'row')]//div[@class='col']")
        self.barcode_popup = (By.XPATH, "//div[@class='form-in-grid']")
        self.barcode_sn = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'barcode')]")
        self.barcode_type = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[contains(@class, 'control-input')and contains(@class,'flex') and contains(@class, 'align-center')]//select[contains(@data-fieldname,'barcode_type')]")
        self.barcode_uom = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'uom')and contains(@data-doctype, 'Item Barcode')]")
        self.auto_reorder_collapse_click = (By.XPATH, "//div[@data-fieldname='reorder_section']/child::div[contains(@class,'section-head') and contains(@class, 'collapsed')]")
        self.auto_reorder_collapse_click = (By.XPATH, "//div[@data-fieldname='reorder_section']/child::div[contains(@class,'section-head') and contains(@class, 'collapsible')]")
        self.auto_reorder_add_row = (By.XPATH, "//div[@data-fieldname='reorder_levels']//button[@type='button'][normalize-space()='Add Row']")
        self.reorder_warehouse = (By.XPATH,"//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'warehouse_group')]")
        self.order_warehouse_option = (By.XPATH,"//div[@class='awesomplete']/child::ul[@id='awesomplete_list_23']//div[@role='option']//p")
        self.reorder_request_for = (By.XPATH, "//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'warehouse') and contains(@aria-owns,'awesomplete_list_24')]")
        self.reorder_request_for_option = (By.XPATH,"//div[@class='awesomplete']/child::ul[@id='awesomplete_list_24']//div[@role='option']//p")
        self.reorder_warehouse_qty = (By.XPATH,"\//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[@class='control-input']//input[contains(@data-fieldname,'warehouse_reorder_qty')]")
        self.reorder_purpose = (By.XPATH,"//div[@class='form-group']/child::div[@class='control-input-wrapper']//div[contains(@class, 'control-input')and contains(@class,'flex') and contains(@class, 'align-center')]//select[contains(@data-fieldname,'material_request_type') and contains(@data-doctype,'Item Reorder')]")


        # self.save_btn_xpath = (By.XPATH, "//div[@class='container']/child::div[contains(@class, 'row') and contains(@class, 'flex') and contains(@class, 'align-center') and contains(@class, 'justify-between') and contains(@class, 'page-head-content')]/child::div[contains(@class, 'col') and contains(@class, 'flex') and contains(@class, 'justify-content-end') and contains(@class, 'page-actions')]/descendant::button[contains(@data-label, 'Save')]")
        self.save_btn_xpath = (By.XPATH, "//div[@id='page-Item']//button[@data-label='Save']")
    
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

    def add_item(self, excel_sheet_path, sheet_name):
        add_item = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.item_add_btn))
        self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/add_item_btn_click.png")
        add_item.click()
        
        # check popup open
        # popup = WebDriverWait(self.driver, 20).until(
        #     EC.visibility_of_element_located(self.add_item_popup)
        # )
        # self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/item_popup.png")
        # popup.find_element(*self.item_code_xpath).send_keys("Sony Earbuds")
        # print("Popup Element is Visible..")

        # time.sleep(5)
        # save_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.item_save_popup))
        # save_btn.click()

        full_form_open = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.item_add_full_form))
        full_form_open.click()
        item_datas = get_item_master_datas(excel_sheet_path, sheet_name)
        print("Item Datas", item_datas)
        for item in item_datas:
            item_code = self.driver.find_element(*self.item_code__two_xpath)
            item_code.send_keys(item['code'])
            # item_group = self.driver.find_element(*self.item_group_xpath)
            item_group = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.item_group_xpath))
            item_group.clear()
            item_group.send_keys(item['group'])
            item_group.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
            item_group.send_keys(Keys.ENTER)
            time.sleep(2)

            uom = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.uom))
            uom.clear()
            uom.send_keys(item['uom'])
            uom.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
            uom.send_keys(Keys.ENTER)
            time.sleep(2)

            opening_stock = self.driver.find_element(*self.opening_stock)
            opening_stock.send_keys(item['opening_stock'])

            maintain_stock = self.driver.find_element(*self.is_stock_item)
            if maintain_stock.is_selected():
                print("The checkbox is selected")
            else:
                maintain_stock.click()
                print("The checkbox is not selected.")

            value_rate = self.driver.find_element(*self.valuation_rate)
            value_rate.send_keys(item['valuation_rate'])

            selling_rate = self.driver.find_element(*self.selling_rate)
            selling_rate.send_keys(item['selling_rate'])
            open_desc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.collapse_disable))
            open_desc.click()
            time.sleep(2)
            open_enable = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.collapse_enable))
            self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/description.png")
            time.sleep(2)
            description = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.description))
            description.clear()
            description.click()
            ActionChains(self.driver).move_to_element(description)
            description.send_keys(item['description'])

            ActionChains(self.driver).scroll_by_amount(0,-100).perform()
            time.sleep(2)

            # inventory tab
            inv_tab = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.inventory_tab))
            inv_tab.click()
            self.driver.get_screenshot_as_file("E:/Erpnext Automation/Screenshots/inventory_tab.png")

            

            # save_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_btn_xpath))
            # save_btn.click()
            time.sleep(3)

        time.sleep(3)

def get_item_master_datas(excel_file_path, sheet_name):
    workbook = openpyxl.load_workbook(excel_file_path)
    sheet = workbook[sheet_name]

    item_data = []
    for i in range(2, sheet.max_row+1):
        item_ = {
            "code" : sheet.cell(row=i, column=1).value,
            "item_name" : sheet.cell(row=i, column=2).value,
            "uom" : sheet.cell(row=i, column=3).value,
            "description" : sheet.cell(row=i, column=4).value,
            "group" : sheet.cell(row=i, column=5).value,
            "opening_stock" : sheet.cell(row=i, column=6).value,
            "valuation_rate" : sheet.cell(row=i, column=7).value,
            "selling_rate" : sheet.cell(row=i, column=8).value
        }

        item_data.append(item_)
    return item_data