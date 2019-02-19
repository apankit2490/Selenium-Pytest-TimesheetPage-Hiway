import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.Driver import Driver

from pages.Driver import *
class Page_Login:
    def __init__(self):
        self.locator_login_button='a.btn.btn-danger.btn-lg'
        self.locator_username='identifierId'
        self.locator_next_button='//*[@id="identifierNext"]//span[contains(text(), "Next")]'
        self.locator_password_by_id='password'
        self.locator_password_entry='//*[@id="password"]//input[@type="password"]'
        self.locator_next_password='//*[@id="passwordNext"]//span[contains(text(), "Next")]'
        self.locator_error_message='//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[2]/div[2]/div'
        self.locator_getname='span.username-position.hide-sm.hide-xs.ng-binding.ng-scope'

    def initial_login(self,driver):
        Login_button=driver.find_element_by_css_selector(self.locator_login_button).click()
    def enter_username(self,driver,uname=Driver().username):
        Username=driver.find_element_by_id(self.locator_username).send_keys(uname)
        next=driver.find_element_by_xpath(self.locator_next_button).click()
    def enter_password(self,driver,password=Driver().password):
        element=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,self.locator_password_by_id)))
        password=driver.find_element_by_xpath(self.locator_password_entry).send_keys(password)
        next_password=driver.find_element_by_xpath(self.locator_next_password).click()

    def invalid_login_uname(self, driver, uname):
        self.initial_login(driver)
        self.enter_username(driver,uname)
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.locator_error_message)))
        message=driver.find_element_by_xpath(self.locator_error_message)
        return str(message.text)



    def getname(self,driver):
        time.sleep(5)
        return driver.find_element_by_css_selector(self.locator_getname).text
