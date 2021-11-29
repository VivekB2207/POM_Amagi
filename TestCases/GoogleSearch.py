import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import sys
sys.path.append("/Users/apple/PycharmProject/pythonProject/Amagi_SeleniumPython")

from PageObjects.SearchPage import SearchPage
from PageObjects.ResultPage import ResultPage
from PageObjects.WikipediaPage import WikipediaPage

class SearchTest(unittest.TestCase):
    baseURL = "https://www.google.com"
    searchQuery = "Wikipedia"
    WikiQuery = "Harry Potter"
    QueryLink = "https://www.wikipedia.org/"

    QueryDescription = "https://en.wikipedia.org/wiki/Harry_Potter"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()


    def test_search(self):
        searchPage = SearchPage(self.driver)
        resultPage = ResultPage(self.driver)
        wikipediaResult = WikipediaPage(self.driver)

        searchPage.searchGooglePage(self.searchQuery)
        time.sleep(5)
        resultPage.sendResult(self.QueryLink)

        wikipediaResult.QuerySearch(self.WikiQuery)
        wikipediaResult.SuggestionList(self.QueryDescription)
        wikipediaResult.VerifyHeading(self.WikiQuery)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()



    if __name__== '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/apple/PycharmProject/pythonProject/Amagi_SeleniumPython/Reports'))

