import pytest
import unittest
from Highway_helper import *
from pytest import *
from selenium import webdriver

class Test_timesheet:
    @classmethod
    def setup_class(self):
        self.driver=webdriver.Chrome("/home/ankit_kumar/PycharmProjects/Selenium_automation/Drivers/chromedriver")
        self.driver.maximize_window()
        self.driver.get("https://qa.hiway.hashedin.com/")
        self.login=Login()
    @classmethod
    def teardown_class(self):
        self.login.logout(self.driver)
        self.driver.close()

    def test_name_on_timesheet(self):
        self.login.initial_login(self.driver)
        time.sleep(10)
        timesheet=self.driver.find_element_by_xpath('/html/body/div/md-toolbar/div/div[2]/span[4]/a').click()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/md-content/div/div/div[1]/h2')))
        header_displayed=self.driver.find_element_by_xpath('/html/body/md-content/div/div/div[1]/h2')
        name_from_email=str(self.driver.find_element_by_css_selector\
            ('span.username-position.hide-sm.hide-xs.ng-binding.ng-scope').text).split('@')[0].replace('.',' ')
        assert name_from_email.lower() in str(header_displayed.text).lower()



if __name__=='__main__':
    pytest.main()
