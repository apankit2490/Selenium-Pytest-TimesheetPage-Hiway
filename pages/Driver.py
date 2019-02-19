import json
from selenium import webdriver

class Driver:
        with open('/home/ankit_kumar/PycharmProjects/Selenium_automation/data.json', 'r') as data:
            data = json.load(data)
        chrome_path = data['chromedriver_path']
        home_url = data['home_url']
        username = data['uname']
        password = data['password']
        invalid_email=data['invalid_email']
        invalid_password=data['invalid_password']
        def drivermanager(self):
                driver = webdriver.Chrome(self.chrome_path)
                driver.maximize_window()
                driver.get(self.home_url)
                return driver
