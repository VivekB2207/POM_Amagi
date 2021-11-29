import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchPage():
    #Locators of search page
    search_box_xpath = "//input[@name='q']"

    def __init__(self, driver):
        self.driver = driver

    def searchGooglePage(self, searchQuery):
        element = self.driver.find_element(By.XPATH, self.search_box_xpath)
        element.send_keys(searchQuery)
        time.sleep(0.5)
        element.send_keys(Keys.ENTER)
        time.sleep(1)