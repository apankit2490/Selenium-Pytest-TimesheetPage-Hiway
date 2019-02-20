import time

from selenium import webdriver

from pages.Hiway_page import Hiway_page
from pages.Login_page import Page_Login
from pages.Timesheet_page import Timesheet_page

# browser=webdriver.Chrome("/home/ankit_kumar/PycharmProjects/Selenium_automation/Drivers/chromedriver")
# browser.get("https://qa.hiway.hashedin.com/")
# browser.maximize_window()
# assert 'Google'.lower() in browser.title.lower()
# browser.close()
# driver=webdriver.Firefox(executable_path="/home/ankit_kumar/PycharmProjects/Selenium_automation/Drivers/geckodriver")
# driver.get("https://hashedin.com/")
# driver.maximize_window()
# assert 'hashedin' in driver.title.lower()
# driver.close()

obj=Timesheet_page()
Page_Login(obj.driver).login_complete()
Hiway_page(obj.driver).click_on_Continue()
obj.timesheet_page()
# obj.create_entry_projectcode()
# obj.create_entry_type()
# obj.create_entry_hours()
obj.create_entry_complete()