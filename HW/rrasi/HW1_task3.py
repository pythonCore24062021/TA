#Please, write integration tests by Selenium WebDriver to verify some features of Open Cart Application.
#Please develop next methods in the FirstSeleniumTest class

#checkAddToCart method - to check the functionality of adding items 'Xiaomi Mi 8' and 'MacBook' to cart.

import time
import unittest

from selenium import webdriver


def temp():
    tem = 1


class PythonOrgSearch(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")
        temp()
        temp()
        time.sleep(2)

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_checkAddToCart (self):
        my_acount_btm = self.driver.find_element_by_css_selector("#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md")
        my_acount_btm.click()
        reg_btn = self.driver.find_element_by_css_selector("#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a")
        reg_btn.click()



