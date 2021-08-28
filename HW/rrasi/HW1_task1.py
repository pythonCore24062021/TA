#Please, write integration tests by Selenium WebDriver to verify some features of Open Cart Application.
#Please develop next methods in the FirstSeleniumTest class

#checkCurrencyChange method - to check currency change on page;
#Check out three cases of choosing on webpage: Dollar, Euro and Pound Sterling;

import time
import unittest

from selenium import webdriver



class PythonOrgSearch(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")

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

    def checkCurrencyChange(self):
        currency_btm = self.driver.find_element_by_css_selector(
            "#form-currency > div > button > span"
        )
        currency_btm.click()
        eur_btn = self.driver.find_element_by_css_selector(
            "#form-currency > div > ul > li:nth-child(1) > button")
        eur_btn.click()

        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("mac")
        search_btn = self.driver.find_element_by_css_selector("#search > span > button > i")
        search_btn.click()
        products = self.driver.find_elements_by_class_name("product-thumb")


