import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class Timesheet_page:
    def __init__(self,driver):
        self.driver=driver
        self.locator_timesheet_button='/html/body/div/md-toolbar/div/div[2]/span[4]/a'
        self.locator_name_in_header='/html/body/md-content/div/div/div[1]/h2'
        self.locator_name_in_email='span.username-position.hide-sm.hide-xs.ng-binding.ng-scope'
        self.locator_next_button='/html/body/md-content/div/div/div[2]/button[2]'
        self.locator_previous_button='/html/body/md-content/div/div/div[2]/button[1]'


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
    def get_current_url(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.locator_previous_button)))
        url=str(self.driver.current_url)
        return url
    def get_next_button_status(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.locator_next_button)))
        next_button = self.driver.find_element_by_xpath(self.locator_next_button).is_enabled()
        return next_button
    def click_previous_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.locator_previous_button)))
        prev_button = self.driver.find_element_by_xpath(self.locator_previous_button).click()
