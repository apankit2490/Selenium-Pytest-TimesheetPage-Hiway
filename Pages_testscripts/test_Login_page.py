import time
import pytest
from pages.Hiway_page import Hiway_page
from pages.Driver import Driver
from pages.Login_page import Page_Login
from pages.Timesheet_page import Timesheet_page
from Utility.csv_loader import get_csv_data
from ddt import ddt,data,unpack
import unittest
path = "/home/ankit_kumar/PycharmProjects/Selenium_automation/data/test_data.csv"
invalid_cred_path="/home/ankit_kumar/PycharmProjects/Selenium_automation/data/test_data_invalid_cedentials.csv"


@ddt
class Test_login_page(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver_object=Driver()
        cls.driver=cls.driver_object.get_driver()
        cls.login=Page_Login(cls.driver)
        cls.hiway=Hiway_page(cls.driver)
    @classmethod
    def setup_class(cls):
        pass
    @classmethod
    def teardown_class(cls):
        pass

    @classmethod
    def tearDown(cls):
        # self.login.logout()
        cls.driver.close()

    @data(*get_csv_data(path))
    @unpack
    def test_login_oauth(self, username, password):
        self.login.initial_login()
        self.login.enter_username(username)
        self.login.enter_password(password)
        self.hiway.click_on_Continue()
        self.usernamee=str(Driver().username)
        usernameee =str(self.login.getname())
        assert self.usernamee.lower() in usernameee.lower()

    @data(*get_csv_data(invalid_cred_path))
    @unpack
    def test_login_oauth_fail(self,username):
        error_message=self.login.invalid_login_uname(username)
        assert 'Enter a valid email or phone number' in error_message



if __name__=='__main__':
    pytest.main()