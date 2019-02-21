import re
import time

from colormap import rgb2hex
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.Driver import Driver
from pages.Login_page import Page_Login
from pages.Hiway_page import Hiway_page



class Timesheet_page:
    # test_driver=Driver().get_driver()
    def __init__(self,driver):#!!!!DONT FORGET TO REMOVE AFTER TESTTTTTTTTT
        self.driver=driver
        self.locator_timesheet_button='/html/body/div/md-toolbar/div/div[2]/span[4]/a'
        self.locator_name_in_header='/html/body/md-content/div/div/div[1]/h2'
        self.locator_name_in_email='span.username-position.hide-sm.hide-xs.ng-binding.ng-scope'
        self.locator_next_button='/html/body/md-content/div/div/div[2]/button[2]'
        self.locator_previous_button='/html/body/md-content/div/div/div[2]/button[1]'
        self.locator_project_code='input[type="search"]'
        self.locator_project_code_dropdown='//ul/li[1]/md-autocomplete-parent-scope/span[1]/span'
        self.locator_datepicker='body > md-content > div > div > div.md-title.layout-align-space-between-center.layout-row > span'
        self.locator_type_dropdown='//md-select[@ng-model="newEntry.type"]'
        self.locator_type_choice='//div[@class="md-select-menu-container md-active md-clickable"]/md-select-menu/md-content/md-option[1]/div'
        self.locator_hours='newEntry.hrs'
        self.locator_mins='newEntry.min'
        self.locator_description='newEntry.description'
        self.locator_hit_add= '/html/body/md-content/div/div/md-card/md-card-text/form/div[1]/button'
        self.locator_color_header='.md-bar.md-bar2'
        self.locator_delete_button='//form/div[1]/div[1]/div[1]/md-icon-button/md-icon/i'
        self.locator_description_from_display='//form//div//md-input-container/input[@ng-model="entry.description"]'
        self.locator_sl_no='//div/div/form/div[1]/div[1]/div[1]/div[1]'



    def timesheet_page(self):
        time.sleep(5)
        timesheet = self.driver.find_element_by_xpath(self.locator_timesheet_button).click()

    def get_name_in_header(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.locator_name_in_header)))
        return self.driver.find_element_by_xpath(self.locator_name_in_header)

    def get_name_from_email(self):
        return  str(self.driver.find_element_by_css_selector \
                (self.locator_name_in_email).text).split('@')[0].replace('.', ' ')

    def get_current_date(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.locator_datepicker)))
        text=str(self.driver.find_element_by_css_selector(self.locator_datepicker).text)
        date=text[12:]
        return date

    def get_next_button_status(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.locator_next_button)))
        next_button = self.driver.find_element_by_xpath(self.locator_next_button).is_enabled()
        return next_button

    def click_previous_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.locator_previous_button)))
        prev_button = self.driver.find_element_by_xpath(self.locator_previous_button).click()

    def create_entry_projectcode(self,text='bat'):
        project_code=self.driver.find_element_by_css_selector(self.locator_project_code)
        project_code.clear()
        project_code.send_keys(text)

    def create_entry_type(self,type="Debug"):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.locator_type_dropdown)))
        select=self.driver.find_element_by_xpath(self.locator_type_dropdown)
        select.send_keys(type)

    def create_entry_hours(self,hours='05'):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.locator_hours)))
        self.hour=self.driver.find_element_by_name(self.locator_hours).send_keys(hours)

    def create_entry_mins(self,mins='30'):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.locator_mins)))
        self.mins=self.driver.find_element_by_name(self.locator_mins).send_keys(mins)

    def create_entry_description(self,description='default description'):
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, self.locator_description)))
        self.description=self.driver.find_element_by_name(self.locator_description).send_keys(description)

    def create_entry_hit_add(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_hit_add)))
        # time.sleep(3)
        add=self.driver.find_element_by_xpath(self.locator_hit_add).click()

    def create_entry_complete(self,text='ARU-CCUI-DEL',hours='6',mins='25',desc='default desc'):
        self.driver.implicitly_wait(3)
        self.create_entry_projectcode(text)
        self.create_entry_type()
        self.create_entry_hours(hours)
        self.create_entry_mins(mins)
        self.create_entry_description(desc)
        self.create_entry_hit_add()


    def get_color_rgb_value(self):
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of((By.CSS_SELECTOR, self.locator_color_header)))
        time.sleep(3)
        self.color=self.driver.find_element_by_css_selector(self.locator_color_header).value_of_css_property('background-color')
        return str(self.color)

    def delete_task(self):
        while(True):
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,self.locator_delete_button)))
                delete=self.driver.find_element_by_xpath(self.locator_delete_button).click()
                time.sleep(3)


            except:
                return

    def get_slno_from_display(self):
        time.sleep(5)
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of((By.XPATH, self.locator_description_from_display)))
        self.description_display=str(self.driver.find_element_by_xpath(self.locator_sl_no).text)
        return self.description_display

    def get_hexcode_from_rgb(self,rgb):
        m = re.search('rgba\((.+?)\)', rgb)
        if m:
            found = m.group(1)
        r,g,b=found.split(',')[:3]
        return rgb2hex(int(r),int(g),int(b))



# obj=Timesheet_page()
# obj.get_hexcode_from_rgb('rgb(255,64,129)')
# Page_Login(obj.driver).login_complete()
# Hiway_page(obj.driver).click_on_Continue()
# obj.timesheet_page()
# obj.create_entry()

