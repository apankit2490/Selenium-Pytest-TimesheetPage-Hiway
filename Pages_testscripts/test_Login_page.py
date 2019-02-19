import time

import pytest

from pages.Hiway_page import Hiway_page
from pages.Driver import Driver
from pages.Login_page import Page_Login
from pages.Timesheet_page import Timesheet


class Test_login_page:
    @classmethod
    def setup_class(cls):
        cls.login = Page_Login()

    @classmethod
    def setup_method(cls):
        cls.driver = Driver().drivermanager()
        cls.hiway = Hiway_page()
    @classmethod
    def teardown_method(cls):
        # self.login.logout(self.driver)
        cls.driver.close()

    def test_login_oauth(self):
        self.login.initial_login(self.driver)
        self.login.enter_username(self.driver)
        self.login.enter_password(self.driver)
        self.hiway.click_on_Continue(self.driver)
        self.username=str(Driver().username)
        username =str(self.login.getname(self.driver))
        assert self.username.lower() in username.lower()

    def test_login_oauth_fail(self):
        error_message=self.login.invalid_login_uname(self.driver,Driver().invalid_email)
        assert 'Enter a valid email or phone number' in error_message





if __name__=='__main__':
    pytest.main()