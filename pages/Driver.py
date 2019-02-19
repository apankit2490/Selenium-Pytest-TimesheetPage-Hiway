import json
from selenium import webdriver

class Driver:
    with open('data.json', 'r') as data:
        data = json.load(data)
    chrome_path=data['chromedriver_path']
    home_url=data['home_url']
    username = data['uname']
    password = data['password']
    def __init__(self):
        with open('data.json', 'r') as data:
            data = json.load(data)
        chrome_path=data['chromedriver_path']
        home_url=data['home_url']
        username = data['uname']
        password = data['password']
        self.driver = webdriver.Chrome(self.chrome_path)
        self.driver.maximize_window()
        self.driver.get(self.home_url)
