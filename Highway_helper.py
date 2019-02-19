import json
import time
from pprint import pprint

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# driver=webdriver.Chrome("/home/ankit_kumar/PycharmProjects/Selenium_automation/Drivers/chromedriver")
# driver.maximize_window()
# driver.get("https://qa.hiway.hashedin.com/")

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



    def logout(self,driver):
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.username-position.hide-sm.hide-xs.ng-binding.ng-scope')))
        username=driver.find_element_by_css_selector('span.username-position.hide-sm.hide-xs.ng-binding.ng-scope').click()
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="menu_container_1"]/md-menu-content/md-menu-item/a')))
        logout_button=driver.find_element_by_xpath('//*[@id="menu_container_1"]/md-menu-content/md-menu-item/a').click()
        driver.get(self.home_url)


# initial_login()

# x="hello how are u"
# pprint(x.split(" ")[2:4])
# y=['Time Sheet for Ankit Patnaik']
# z='Time.Sheet@gmail.com'.split('@')[0].replace('.',' ')
# print(z)
# print(z.split('@')[0].replace('.',' ') in y)
# l=Login()
# l.initial_login()
# l.logout()