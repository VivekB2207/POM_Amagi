import time

from selenium.webdriver.common.by import By

class ResultPage():
    #Seach result lcoators
    first_link_result = "a"

    def __init__(self, driver):
        self.driver = driver

    def sendResult(self, QueryLink):
        LinksList = self.driver.find_elements(By.TAG_NAME, self.first_link_result)

        for elements in LinksList:
            if elements.get_attribute("href") is None:
                pass
            else:
                #print(elements.get_attribute("href"))
                if elements.get_attribute("href") == QueryLink:
                    elements.click()
                    time.sleep(10)
                    break
