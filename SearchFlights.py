import time
import unittest
from HomePage import *
from BrowserPage import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Search_Flights(unittest.TestCase):
    def test_search_flights(self):
        Browser = browser.SetUp(self,"https://www.kayak.com/")
        flight = Browser.find_element(By.PARTIAL_LINK_TEXT,"Flights")
        flight.click()
        assert Browser.current_url.__contains__("flights")
        print("Book your Flight now")