import time

from selenium import webdriver
# browser=webdriver.Chrome("/home/ankit_kumar/PycharmProjects/Selenium_automation/Drivers/chromedriver")
# browser.get("https://www.google.com/")
# browser.maximize_window()
# assert 'Google'.lower() in browser.title.lower()
# browser.close()
driver=webdriver.Firefox(executable_path="/home/ankit_kumar/PycharmProjects/Selenium_automation/Drivers/geckodriver")
driver.get("https://hashedin.com/")
driver.maximize_window()
assert 'hashedin' in driver.title.lower()
driver.close()