from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Hiway_page:
    def click_on_Continue(self,driver):
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.h3.btn")))
        hiway_login = driver.find_element_by_css_selector('a.h3.btn').click()