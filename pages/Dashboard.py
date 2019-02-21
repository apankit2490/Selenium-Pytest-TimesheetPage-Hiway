import time


class Dashboard_Page:
    def __init__(self,driver):
        self.driver=driver
        self.locator_timesheet_button = '/html/body/div/md-toolbar/div/div[2]/span[4]/a'

    def navigate_to_dashboard_page(self):
        time.sleep(5)
        timesheet = self.driver.find_element_by_xpath(self.locator_timesheet_button).click()
        time.sleep(3)
