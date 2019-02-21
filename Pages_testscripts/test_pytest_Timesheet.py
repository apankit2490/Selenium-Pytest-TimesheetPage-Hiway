import time
from datetime import timedelta
import datetime

import pytest

from Utility.constants import *
from pages import Timesheet_page
from pages.Dashboard import Dashboard_Page
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
        cls.dashboard=Dashboard_Page(cls.driver)
        cls.dashboard.navigate_to_timesheet_page()


    # @classmethod
    # def teardown_method(self):
    #     # self.login.logout(self.driver)
    #     self.driver.close()

    def test_name_on_timesheet(self):
        header_displayed=self.timesheet.get_name_in_header()
        name_from_email=self.timesheet.get_name_from_email()
        assert name_from_email.lower() in str(header_displayed.text).lower()


    def test_default_currentdate(self):
        assert now.strftime(assert_date_format) in self.timesheet.get_current_date()


    def test_next_button_disabled(self):
        assert self.timesheet.get_next_button_status() == False

    def test_prev_button_to_previous_date(self):
        for i in range(1,4):
            self.timesheet.click_previous_button()
            date = self.timesheet.get_current_date()
            prev_date=now-timedelta(days=i)
            assert prev_date.strftime(assert_date_format) in date
    def test_colorchange_orange_blue_after8hrs(self):
        self.timesheet.delete_task()
        self.timesheet.create_entry_complete(hours=six_hours)
        self.init_color=self.timesheet.get_hexcode_from_rgb(self.timesheet.get_color_rgb_value())
        assert orange_hexcode == self.init_color
        self.timesheet.create_entry_complete(hours=two_hours)
        self.init_color = self.timesheet.get_hexcode_from_rgb(self.timesheet.get_color_rgb_value())
        assert blue_hexcode == self.init_color

    def test_colorchange_blue_pink_after9hrs(self):
        self.timesheet.delete_task()
        self.timesheet.create_entry_complete(hours=eight_hours)
        self.init_color=self.timesheet.get_hexcode_from_rgb(self.timesheet.get_color_rgb_value())
        assert blue_hexcode == self.init_color
        self.timesheet.create_entry_complete(hours=two_hours)
        self.init_color = self.timesheet.get_hexcode_from_rgb(self.timesheet.get_color_rgb_value())
        assert pink_hexcode == self.init_color

    def test_add_task(self):
        self.timesheet.delete_task()
        self.timesheet.create_entry_complete(desc=description)
        assert self.timesheet.get_slno_from_display() == '1.'

    def test_delete(self):
        self.timesheet.delete_task()
        # message=self.timesheet.get_delete_status()
        # assert message == delete_message

    def test_working_hours_added(self):
        self.timesheet.delete_task()
        self.timesheet.create_entry_complete(hours=six_hours)
        working_hours=self.timesheet.get_working_hours_from_header()
        assert six_hours in working_hours

    def test_sharedwith_entry(self):
        self.timesheet.delete_task()
        self.timesheet.create_entry_complete()
        self.timesheet.click_shared_with()
        self.timesheet.enter_name_sharedwith()
        self.timesheet.save_sharedwith_entry()
        sharedwith_name=self.timesheet.get_name_from_sharedwith_entry()
        assert shared_with_username in sharedwith_name

    def test_add_button_unclickable(self):
        self.timesheet.delete_task()
        self.timesheet.create_entry_projectcode('')
        self.timesheet.create_entry_type('')
        self.timesheet.create_entry_hours('')
        self.timesheet.create_entry_mins('')
        self.timesheet.create_entry_description('')
        assert False == self.timesheet.get_add_button_createtask_clickable_status()

    def test_task_entry_suggested(self):
        self.timesheet.logout()
        self.timesheet.login_as_testuser()
        self.hiway.click_on_Continue()
        self.dashboard.navigate_to_timesheet_page()
        self.timesheet.delete_task()
        self.timesheet.save_sharedwith_complete('ankit')
        self.timesheet.logout()
        self.login.login_complete()
        self.hiway.click_on_Continue()
        self.dashboard.navigate_to_timesheet_page()
        suggested_username=self.timesheet.get_name_from_suggested_entry()
        assert test_userID_name in suggested_username


if __name__=='__main__':
    pytest.main()
