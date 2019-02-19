import time


class Timesheet:
    def timesheet_page(self,driver):
        time.sleep(5)
        timesheet = driver.find_element_by_xpath('/html/body/div/md-toolbar/div/div[2]/span[4]/a').click()