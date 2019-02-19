import time

import pytest

from pages.Hiway_page import Hiway_page
from pages.Driver import Driver
from pages.Login_page import Page_Login
from pages.Timesheet_page import Timesheet


class Test_login_page:
    @classmethod
    def setup_method(cls):
        cls.driver = Driver().drivermanager()

    @classmethod
    def teardown_method(cls):
        # cls.driver = Driver().driver
        # self.login.logout(self.driver)
        cls.driver.close()

    def test_login_oauth(self):
        self.login = Page_Login()
        self.login.initial_login(self.driver)
        self.hiway=Hiway_page()
        self.hiway.click_on_Continue(self.driver)
        self.username=str(Driver().username)
        username =str(self.login.getname(self.driver))
        assert self.username.lower() in username.lower()

    def test_login_oauth_fail(self):
        self.login = Page_Login()
        message=self.login.invalid_login_uname(self.driver,Driver().invalid_email)





if __name__=='__main__':
    pytest.main()