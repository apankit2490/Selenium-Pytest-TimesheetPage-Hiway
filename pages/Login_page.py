from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.Driver import *
class Login:
    with open('data.json','r') as data:
        data=json.load(data)
    username=data['uname']
    password=data['password']
    home_url = data['home_url']


    def initial_login(self,driver):
        Login_button=driver.find_element_by_css_selector('a.btn.btn-danger.btn-lg').click()
        Username=driver.find_element_by_id('identifierId').send_keys(self.username)
        next=driver.find_element_by_xpath('//*[@id="identifierNext"]//span[contains(text(), "Next")]').click()
        element=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"password")))
        password=driver.find_element_by_xpath('//*[@id="password"]//input[@type="password"]').send_keys(self.password)
        next_password=driver.find_element_by_xpath('//*[@id="passwordNext"]//span[contains(text(), "Next")]').click()
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.h3.btn")))
        hiway_login=driver.find_element_by_css_selector('a.h3.btn').click()