import time
from datetime import timedelta
import datetime

import pytest

from pages import Timesheet_page
from pages.Driver import Driver
from pages.Hiway_page import Hiway_page
from pages.Timesheet_page import Timesheet_page

now = datetime.datetime.now()
import unittest
from pages.Login_page import *
from pytest import *


class Test_timesheet:

    @classmethod
    def setup_method(cls):
        cls.driver_object = Driver()
        cls.driver = cls.driver_object.get_driver()
        cls.login = Page_Login(cls.driver)
        cls.login.login_complete()
        cls.hiway = Hiway_page(cls.driver)
        cls.hiway.click_on_Continue()
        cls.timesheet=Timesheet_page(cls.driver)
        cls.timesheet.timesheet_page()


    @classmethod
    def teardown_method(self):
        # self.login.logout(self.driver)
        self.driver.close()

    def test_name_on_timesheet(self):
        header_displayed=self.timesheet.get_name_in_header()
        name_from_email=self.timesheet.get_name_from_email()
        assert name_from_email.lower() in str(header_displayed.text).lower()


    def test_default_currentdate(self):
        assert now.strftime("%a, %b %d") in self.timesheet.get_current_date()


    def test_next_button_disabled(self):
        assert self.timesheet.get_next_button_status() == False

    def test_prev_button_to_previous_date(self):
        for i in range(1,4):
            self.timesheet.click_previous_button()
            date = self.timesheet.get_current_date()
            prev_date=now-timedelta(days=i)
            assert prev_date.strftime("%a, %b %d") in date
    def test_colorchange_orange_blue_after8hrs(self):
        '''make entry
        check orange color
        increase time
        check color'''
    def test_add_task(self):
        self.timesheet.delete_task()
        self.timesheet.create_entry_complete(desc='testing from testcase')
        assert self.timesheet.get_slno_from_display() == '1.'




if __name__=='__main__':
    pytest.main()
