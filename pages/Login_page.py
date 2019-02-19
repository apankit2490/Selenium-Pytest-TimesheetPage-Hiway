import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.Driver import Driver

from pages.Driver import *
class Page_Login:


    def initial_login(self,driver,uname=Driver().username,password=Driver().password):
        Login_button=driver.find_element_by_css_selector('a.btn.btn-danger.btn-lg').click()
        Username=driver.find_element_by_id('identifierId').send_keys(uname)
        next=driver.find_element_by_xpath('//*[@id="identifierNext"]//span[contains(text(), "Next")]').click()
        element=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"password")))
        password=driver.find_element_by_xpath('//*[@id="password"]//input[@type="password"]').send_keys(password)
        next_password=driver.find_element_by_xpath('//*[@id="passwordNext"]//span[contains(text(), "Next")]').click()

    def invalid_login_uname(self, driver, uname=Driver().username):
        Login_button = driver.find_element_by_css_selector('a.btn.btn-danger.btn-lg').click()
        Username = driver.find_element_by_id('identifierId').send_keys(uname)
        next = driver.find_element_by_xpath('//*[@id="identifierNext"]//span[contains(text(), "Next")]').click()
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[2]/div[2]/div')))
        message=driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[2]/div[2]/div')
        return str(message.text)



    def getname(self,driver):
        time.sleep(5)
        return driver.find_element_by_css_selector(
            'span.username-position.hide-sm.hide-xs.ng-binding.ng-scope').text
