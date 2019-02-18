import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def initial_login():
    driver=webdriver.Chrome("/home/ankit_kumar/PycharmProjects/Selenium_automation/Drivers/chromedriver")
    driver.get("https://qa.hiway.hashedin.com/")
    btn=driver.find_element_by_css_selector('a.btn.btn-danger.btn-lg')
    btn.click()
    uname=driver.find_element_by_id('identifierId')
    uname.send_keys('ankit.patnaik@hashedin.com')
    next=driver.find_element_by_xpath('//*[@id="identifierNext"]//span[contains(text(), "Next")]')
    next.click()
    element=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"password")))
    pwd=driver.find_element_by_xpath('//*[@id="password"]//input[@type="password"]')
    pwd.send_keys('ANKi@2490')
    next_pwd=driver.find_element_by_xpath('//*[@id="passwordNext"]//span[contains(text(), "Next")]')
    next_pwd.click()
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.navbar-brand")))
    hiway_login=driver.find_element_by_css_selector('a.h3.btn')
    hiway_login.click()
initial_login()