import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class Home_page(unittest.TestCase):
    def test_home_page(self):
        browser = webdriver.Chrome()
        browser.get("https://www.kayak.com/")
        browser.maximize_window()
        time.sleep(5)
        print(browser.title)
        #act_title = 'Search Flights, Hotels & Rental Cars | KAYAK'

        assert browser.title.__contains__("KAYAK")
        print("Home page has been loaded successfully")

        browser.quit()