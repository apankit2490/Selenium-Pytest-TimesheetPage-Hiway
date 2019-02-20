import time

import pytest

from pages.Hiway_page import Hiway_page
from pages.Driver import Driver
from pages.Login_page import Page_Login
from pages.Timesheet_page import Timesheet


class Test_login_page():
    @classmethod
    def setup_method(cls):
        cls.driver_object=Driver()
        cls.driver=cls.driver_object.get_driver()
        cls.login=Page_Login(cls.driver)
        cls.hiway=Hiway_page(cls.driver)
    @classmethod
    def teardown_method(cls):
        # self.login.logout()
        cls.driver.close()

    def test_login_oauth(self):
        self.login.initial_login()
        self.login.enter_username()
        self.login.enter_password()
        self.hiway.click_on_Continue()
        self.username=str(Driver().username)
        username =str(self.login.getname())
        assert self.username.lower() in username.lower()

    def test_login_oauth_fail(self):
        error_message=self.login.invalid_login_uname(self.driver_object.invalid_email)
        assert 'Enter a valid email or phone number' in error_message





if __name__=='__main__':
    pytest.main()