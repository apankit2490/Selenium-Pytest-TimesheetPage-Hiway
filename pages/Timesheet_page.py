import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.Driver import Driver
from pages.Login_page import Page_Login
from pages.Hiway_page import Hiway_page



class Timesheet_page:
    test_driver=Driver().get_driver()
    def __init__(self,driver=test_driver):#!!!!DONT FORGET TO REMOVE AFTER TESTTTTTTTTT
        self.driver=driver
        self.locator_timesheet_button='/html/body/div/md-toolbar/div/div[2]/span[4]/a'
        self.locator_name_in_header='/html/body/md-content/div/div/div[1]/h2'
        self.locator_name_in_email='span.username-position.hide-sm.hide-xs.ng-binding.ng-scope'
        self.locator_next_button='/html/body/md-content/div/div/div[2]/button[2]'
        self.locator_previous_button='/html/body/md-content/div/div/div[2]/button[1]'
        self.locator_project_code='input-20'
        self.locator_project_code_dropdown='//*[@id="ul-20"]/li/md-autocomplete-parent-scope/span[1]/span'
        self.locator_datepicker='body > md-content > div > div > div.md-title.layout-align-space-between-center.layout-row > span'
        self.locator_type_dropdown='//*/div//md-select'
        self.locator_type_choice='//*/div//md-select-menu/md-content/md-option/div[1]'


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
        date=text.replace(',','').split(" ")
        required_date=date[3:7]
        required_date_as_string=""
        for i in required_date:
            required_date_as_string+=i+" "
        return required_date_as_string

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
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.locator_project_code)))
        project_code=self.driver.find_element_by_id(self.locator_project_code)
        project_code.send_keys(text)
        waittobeclickable = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,self.locator_project_code_dropdown)))
        self.driver.find_element_by_xpath(self.locator_project_code_dropdown).click()

    def create_entry_type(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,self.locator_type_dropdown)))
        select=self.driver.find_element_by_xpath(self.locator_type_dropdown).click()
        choice=self.driver.find_element_by_xpath(self.locator_type_choice).click()



# obj=Timesheet_page()
# Page_Login(obj.driver).login_complete()
# Hiway_page(obj.driver).click_on_Continue()
# obj.timesheet_page()
# obj.create_entry()

