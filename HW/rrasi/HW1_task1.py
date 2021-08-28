#Please, write integration tests by Selenium WebDriver to verify some features of Open Cart Application.
#Please develop next methods in the FirstSeleniumTest class

#checkCurrencyChange method - to check currency change on page;
#Check out three cases of choosing on webpage: Dollar, Euro and Pound Sterling;

import time
import re
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


    def test_checkCurrencyChange(self):
        All_currencies = ['$', '€', '£']
        currency_btn = self.driver.find_element_by_css_selector("#form-currency")
        currency_btn.click()
        eur_btn = self.driver.find_element_by_css_selector("#form-currency > div > ul > li:nth-child(1) > button")
        eur_btn.click()
        products = self.driver.find_elements_by_class_name("product-thumb")
        currencies = []
        for product in products:
            currencies.append(product.find_element_by_xpath('.//div/button/strong').text)
        self.assertListEqual(currencies, ['€'])
        currency_btn = self.driver.find_element_by_css_selector("#form-currency")
        currency_btn.click()
        usd_btn = self.driver.find_element_by_css_selector("#form-currency > div > ul > li:nth-child(3) > button")
        usd_btn.click()
        currency_btn = self.driver.find_element_by_css_selector("#form-currency")
        currency_btn.click()
        pound_btn = self.driver.find_element_by_css_selector("#form-currency > div > ul > li:nth-child(2) > button")
        pound_btn.click()
