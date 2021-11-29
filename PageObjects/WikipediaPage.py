import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

class WikipediaPage():
    #WikipediaPage locators
    WikipediaSearchbox_xpath = "//input[@name='search']"
    SuggestionDropdown_xpath = "//a[@class='suggestion-link']"
    ResultFirstHeading_xpath = '//*[@id="firstHeading"]/i'

    def __init__(self, driver):
        self.driver = driver

    def QuerySearch(self, WikiQuery):
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.WikipediaSearchbox_xpath)
        element.click()
        element.send_keys(WikiQuery)
        time.sleep(10)
        #self.driver.find_element(By.XPATH, self.SuggestionDropdown_xpath).send_keys(Keys.PAGE_DOWN)

    def SuggestionList(self, QueryDescription):
        SuggestionOptions = self.driver.find_elements(By.XPATH, self.SuggestionDropdown_xpath)

        for elements in SuggestionOptions:
            if elements.get_attribute("href") is None:
                pass
            else:
                if elements.get_attribute("href") == QueryDescription:
                    elements.click()
                    time.sleep(10)
                    break

    def VerifyHeading(self, WikiQuery):
        QueryHeading = self.driver.find_element(By.XPATH,self.ResultFirstHeading_xpath)
        if QueryHeading.text == WikiQuery:
            print(QueryHeading.text)
            print("result as expected")
        else:
            print("Opps Not found")