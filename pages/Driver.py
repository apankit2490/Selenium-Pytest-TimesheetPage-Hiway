import json

import pytest
import csv
import unittest
from selenium import webdriver


class Driver():
    def __init__(self):
        with open('/home/ankit_kumar/PycharmProjects/Selenium_automation/data.json', 'r') as data:
            data = json.load(data)
        self.chrome_path = data['chromedriver_path']
        self.home_url = data['home_url']
        self.username = data['uname']
        self.password = data['password']
        self.invalid_email = data['invalid_email']
        self.invalid_password = data['invalid_password']

    def get_driver(self):
        self.driver = webdriver.Chrome(self.chrome_path)
        self.driver.maximize_window()
        self.driver.get(self.home_url)
        return self.driver

