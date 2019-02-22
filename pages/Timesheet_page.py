import datetime
import re
import time
from colormap import rgb2hex
from selenium.webdriver.common.keys import Keys
now = datetime.datetime.now()
from pages.Login_page import Page_Login
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Utility.constants import *
from pages.Driver import Driver
from pages.Login_page import Page_Login
from pages.Hiway_page import Hiway_page



class Timesheet_page:
    # test_driver=Driver().get_driver()
    def __init__(self,driver):#!!!!DONT FORGET TO REMOVE AFTER TESTTTTTTTTT
        self.driver=driver
        self.locator_timesheet_button='/html/body/div/md-toolbar/div/div[2]/span[4]/a'
        self.locator_name_in_header='/html/body/md-content/div/div/div[1]/h2'
        self.locator_name_in_email='span.username-position.hide-sm.hide-xs.ng-binding.ng-scope'
        self.locator_next_button='/html/body/md-content/div/div/div[2]/button[2]'
        self.locator_previous_button='/html/body/md-content/div/div/div[2]/button[1]'
        self.locator_project_code='input[type="search"]'
        self.locator_project_code_dropdown='//ul/li[1]/md-autocomplete-parent-scope/span[1]/span'
        self.locator_datepicker='body > md-content > div > div > div.md-title.layout-align-space-between-center.layout-row > span'
        self.locator_type_dropdown='//md-select[@ng-model="newEntry.type"]'
        self.locator_type_dropdown_edit='//md-select[@ng-model="entry.type"]'
        self.locator_type_choice='//div[@class="md-select-menu-container md-active md-clickable"]/md-select-menu/md-content/md-option[1]/div'
        self.locator_hours='newEntry.hrs'
        self.locator_hours_edit = 'entry.hrs'
        self.locator_mins='newEntry.min'
        self.locator_mins_edit = 'entry.min'
        self.locator_description='newEntry.description'
        self.locator_description_edit = '//input[@ng-model="entry.description"]'
        self.locator_hit_add= '/html/body/md-content/div/div/md-card/md-card-text/form/div[1]/button'
        self.locator_color_header='.md-bar.md-bar2'
        self.locator_delete_button='//form/div[1]/div[1]/div[1]/md-icon-button/md-icon/i'
        self.locator_description_from_display='//form//div//md-input-container/input[@ng-model="entry.description"]'
        self.locator_sl_no='//div/div/form/div[1]/div[1]/div[1]/div[1]'
        self.locator_after_delete_msg='/html/body/md-content/div/div/div[5]/i'
        self.locator_sharedwith_select_users_hidden_popups= '//md-autocomplete-wrap/input[@placeholder="Select Users"]'
        self.locator_shared_with_button='//div/div/form/div[1]/div[2]/span[2]/a/b'
        self.locator_sharedwith_user_name=shared_with_username
        self.locator_sharedwith_save_button='#user-select-modal-save-button'
        self.locator_username_autocomplete='//li/md-autocomplete-parent-scope/div[@class="ng-binding"]'
        self.locator_logout_button='span.username-position.hide-sm.hide-xs.ng-binding.ng-scope'
        self.locator_logout_username='//*[@id="menu_container_1"]/md-menu-content/md-menu-item/a'
        self.locator_google_my_avtaar='//*[@id="gbw"]/div/div/div[2]/div[4]/div[1]/a/span'
        self.locator_google_signout='//*[@id="gb_71"]'
        self.locator_freeze_message='//div/div/div[@ng-if="editable && !unfreeze"]/i[@class="ng-binding"]'
        self.locator_toast_div='div.md-toast-content'
        self.locator_toast_message='//md-content/md-toast/div[@class="md-toast-content"]/span[@class="md-toast-text ng-binding"]'
        self.locator_chrome_cleardata='chrome://settings/clearBrowserData'
        self.locator_hit_enter_in_cleardata_screen='settings-ui'
        self.locator_suggested_username='hiwaytest'



    def timesheet_page(self):
        time.sleep(5)
        timesheet = self.driver.find_element_by_xpath(self.locator_timesheet_button).click()
        time.sleep(3)

    def get_name_in_header(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.locator_name_in_header)))
        return self.driver.find_element_by_xpath(self.locator_name_in_header)

    def get_name_from_email(self):
        return  str(self.driver.find_element_by_css_selector \
                (self.locator_name_in_email).text).split('@')[0].replace('.', ' ')

    def get_current_date(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.locator_datepicker)))
        text=str(self.driver.find_element_by_css_selector(self.locator_datepicker).text)
        date=text[12:]
        return date

    def get_next_button_status(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.locator_next_button)))
        next_button = self.driver.find_element_by_xpath(self.locator_next_button).is_enabled()
        return next_button

    def click_previous_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.locator_previous_button)))
        prev_button = self.driver.find_element_by_xpath(self.locator_previous_button).click()

    def create_entry_projectcode(self,text='bat'):
        project_code=self.driver.find_element_by_css_selector(self.locator_project_code)
        project_code.clear()
        project_code.send_keys(text)


    def create_entry_type(self,type="Debug"):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.locator_type_dropdown)))
        select=self.driver.find_element_by_xpath(self.locator_type_dropdown)
        select.send_keys(type)

    def edit_entry_type(self, type="Debug"):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.locator_type_dropdown_edit)))
        select = self.driver.find_element_by_xpath(self.locator_type_dropdown_edit)
        select.send_keys(type)
        select.send_keys(Keys.TAB)
        self.wait_till_toast_dissapear()

    def create_entry_hours(self,hours='05'):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.locator_hours)))
        self.hour=self.driver.find_element_by_name(self.locator_hours).send_keys(hours)

    def edit_entry_hours(self,hours='05'):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.locator_hours_edit)))
        self.hour=self.driver.find_element_by_name(self.locator_hours_edit)
        self.hour.clear()
        self.hour.send_keys(hours)
        self.wait_till_toast_dissapear()


    def create_entry_mins(self,mins='30'):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.locator_mins)))
        self.mins=self.driver.find_element_by_name(self.locator_mins).send_keys(mins)

    def edit_entry_mins(self,mins='30'):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.locator_mins_edit)))
        self.mins=self.driver.find_element_by_name(self.locator_mins_edit)
        self.mins.clear()
        self.mins.send_keys(mins)
        self.wait_till_toast_dissapear()




    def create_entry_description(self,description='default description'):
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, self.locator_description)))
        self.description=self.driver.find_element_by_name(self.locator_description).send_keys(description)

    def edit_entry_description(self,description='default description'):
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, self.locator_description)))
        self.description=self.driver.find_element_by_xpath(self.locator_description_edit)
        self.description.clear()
        self.description.send_keys(description)
        self.description.send_keys(Keys.TAB)

    def create_entry_hit_add(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_hit_add)))
        # time.sleep(3)
        add=self.driver.find_element_by_xpath(self.locator_hit_add).click()

    def create_entry_complete(self,text='ARU-CCUI-DEL',type="Debug",hours='6',mins='25',desc='default desc'):
        self.driver.implicitly_wait(3)
        self.create_entry_projectcode(text)
        self.create_entry_type(type)
        self.create_entry_hours(hours)
        self.create_entry_mins(mins)
        self.create_entry_description(desc)
        self.create_entry_hit_add()


    def get_color_rgb_value(self):
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of((By.CSS_SELECTOR, self.locator_color_header)))
        time.sleep(3)
        self.color=self.driver.find_element_by_css_selector(self.locator_color_header).value_of_css_property('background-color')
        return str(self.color)

    def delete_task(self):
        while(True):
            try:
                delete=self.driver.find_element_by_xpath(self.locator_delete_button).click()
                self.wait_till_toast_dissapear()


            except:
                return

    def get_slno_from_display(self):
        time.sleep(5)
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of((By.XPATH, self.locator_description_from_display)))
        self.description_display=str(self.driver.find_element_by_xpath(self.locator_sl_no).text)
        return self.description_display

    def get_hexcode_from_rgb(self,rgb):
        m = re.search('rgba\((.+?)\)', rgb)
        if m:
            found = m.group(1)
        r,g,b=found.split(',')[:3]
        return rgb2hex(int(r),int(g),int(b))

    def get_delete_status(self):
        try:
            message=self.driver.find_element_by_xpath(self.locator_after_delete_msg)
            return str(message.text)
        except NoSuchElementException:
            return None

    def get_working_hours_from_header(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.locator_delete_button)))
        text = str(self.driver.find_element_by_css_selector(self.locator_datepicker).text)
        time = text[:5]
        return time

    def click_shared_with(self):
        self.driver.find_element_by_xpath(self.locator_shared_with_button).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.locator_sharedwith_select_users_hidden_popups)))

    def enter_name_sharedwith(self,name=shared_with_username):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.locator_sharedwith_select_users_hidden_popups)))
        select_users=self.driver.find_element_by_xpath(self.locator_sharedwith_select_users_hidden_popups)
        select_users.click()
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH, self.locator_username_autocomplete)))
        except:
            pass
        for i in name:
            select_users.send_keys(i)
        user=self.driver.find_element_by_xpath(self.locator_username_autocomplete).click()

    def wait_till_toast_dissapear(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.locator_toast_div)))
        element = WebDriverWait(self.driver, 10).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.locator_toast_div)))

    def save_sharedwith_entry(self):
        # time.sleep(5)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_sharedwith_select_users_hidden_popups)))
        save=self.driver.find_element_by_css_selector(self.locator_sharedwith_save_button).click()
        self.wait_till_toast_dissapear()


    def save_sharedwith_complete(self,name=shared_with_username):
        self.create_entry_complete()
        self.click_shared_with()
        self.enter_name_sharedwith(name)
        self.save_sharedwith_entry()

    def get_name_from_sharedwith_entry(self):
        # time.sleep(5)
        name=self.driver.find_element_by_partial_link_text(self.locator_sharedwith_user_name).text
        return str(name)

    def get_add_button_createtask_clickable_status(self):
        return self.driver.find_element_by_xpath(self.locator_hit_add).is_enabled()

    def clear_browser_cache_and_cookies(self):
        self.driver.get(self.locator_chrome_cleardata)
        self.driver.switch_to_active_element()
        self.driver.find_element_by_tag_name(self.locator_hit_enter_in_cleardata_screen).send_keys(Keys.ENTER)
        self.driver.get(Driver().home_url)

    def signout_from_google(self):
        self.driver.get(google_url)
        self.driver.find_element_by_xpath(self.locator_google_my_avtaar).click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, self.locator_google_signout)))
        self.driver.find_element_by_xpath(self.locator_google_signout).click()

    def logout(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR,self.locator_logout_button)))
        username = self.driver.find_element_by_css_selector(self.locator_logout_button).click()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.locator_logout_username)))
        logout_button = self.driver.find_element_by_xpath(self.locator_logout_username).click()
        self.signout_from_google()
        self.clear_browser_cache_and_cookies()

    def login_as_testuser(self):
        Page_Login(self.driver).login_complete(test_username,test_password)

    def get_name_from_suggested_entry(self):
        name=self.driver.find_element_by_partial_link_text(test_userID_name).text
        return str(name)

    def datepicker_navigate_to_specified_date(self,specified_date):
        while True:
            self.click_previous_button()
            date = self.get_current_date()
            if (date==specified_date):
                break

    def get_freeze_message(self):
        return str(self.driver.find_element_by_xpath(self.locator_freeze_message).text)

    def get_message_from_toast(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.locator_toast_div)))
        msg=self.driver.find_element_by_xpath(self.locator_toast_message).text
        element = WebDriverWait(self.driver, 10).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.locator_toast_div)))
        return str(msg)

    def get_message_from_hidden_input_invalid_hours(self):
        time.sleep(10)
        message=self.driver.execute_script('return $("//md-card-text/form/div/md-input-container[@flex-xs="50"]").text();')
        return str(message)

    def get_suggested_user_name(self):
        name=self.driver.find_element_by_partial_link_text(self.locator_suggested_username).text
        return str(name)

