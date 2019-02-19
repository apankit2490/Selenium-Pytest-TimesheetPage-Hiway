# import time
# from datetime import timedelta
# import datetime
#
# import pytest
#
# from pages import Timesheet_page
# from pages.Driver import *
# from pages.Timesheet_page import Timesheet
#
# now = datetime.datetime.now()
# import unittest
# from pages.Login_page import *
# from pytest import *
#
#
# class Test_timesheet:
#     with open('data.json', 'r') as data:
#         data = json.load(data)
#     chrome_path=data['chromedriver_path']
#     home_url=data['home_url']
#     username = data['uname']
#     password = data['password']
#     @classmethod
#     def setup_method(self):
#         self.driver=Driver().driver
#         self.login=Page_Login()
#         self.login.initial_login(self.driver)
#         self.driver.implicitly_wait(3)
#         self.timesheet=Timesheet()
#         self.timesheet.timesheet_page(self.driver)
#
#
#     @classmethod
#     def teardown_method(self):
#         # self.login.logout(self.driver)
#         self.driver.close()
#
#     def test_name_on_timesheet(self):
#         element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/md-content/div/div/div[1]/h2')))
#         header_displayed=self.driver.find_element_by_xpath('/html/body/md-content/div/div/div[1]/h2')
#         name_from_email=str(self.driver.find_element_by_css_selector\
#             ('span.username-position.hide-sm.hide-xs.ng-binding.ng-scope').text).split('@')[0].replace('.',' ')
#         assert name_from_email.lower() in str(header_displayed.text).lower()
#
#
#     '''def test_default_currentdate(self):
#         url=str(self.driver.current_url)
#         assert now.strftime("%Y-%m-%d") in url
#
#
#     def test_next_button_disabled(self):
#         next_button=self.driver.find_element_by_xpath('/html/body/md-content/div/div/div[2]/button[2]')
#         assert next_button.is_enabled() == False
#     def test_prev_button_to_previous_date(self):
#         for i in range(1,4):
#             prev_button = self.driver.find_element_by_xpath('/html/body/md-content/div/div/div[2]/button[1]').click()
#             time.sleep(3)
#             url = str(self.driver.current_url)
#             prev_date=now-timedelta(days=i)
#             assert prev_date.strftime("%Y-%m-%d") in url
#     # def test_colorchange_orange_blue_after8hrs(self):
#     #     time.sleep(10)
#     #     project_code=self.driver.find_element_by_xpath('//*[@id="input-432"]').click()
#     #     time.sleep(10)
#     def test_login_oauth(self):
#         incongnito_window=webdriver.ChromeOptions()
#         incongnito_window.add_argument("--incognito")
#         driver=webdriver.Chrome(chrome_options=incongnito_window,executable_path=self.chrome_path)
#         driver.get(self.home_url)
#         self.login.initial_login(driver)
#         username=self.driver.find_element_by_css_selector('span.username-position.hide-sm.hide-xs.ng-binding.ng-scope').text
#         assert self.username in username'''
#
#
#
# if __name__=='__main__':
#     pytest.main()
