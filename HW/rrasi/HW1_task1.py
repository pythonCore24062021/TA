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


    def test_check_currency_is_eur(self):
        currency_btn = self.driver.find_element_by_css_selector("#form-currency > div > button > span")
        currency_btn.click()
        eur_btn = self.driver.find_element_by_css_selector("#form-currency > div > ul > li:nth-child(1) > button")
        eur_btn.click()
        check_currency_change = self.driver.find_element_by_css_selector("#cart-total")
        self.assertEqual(check_currency_change.text, "0 item(s) - 0.00€")

    def test_check_currency_is_dollar(self):
        currency_dropdown = self.driver.find_element_by_css_selector("#form-currency > div > button")
        currency_dropdown.click()
        select_dollar = self.driver.find_element_by_css_selector("#form-currency > div > ul > li:nth-child(3) > button")
        select_dollar.click()
        check_currency_change = self.driver.find_element_by_css_selector("#cart-total")
        self.assertEqual(check_currency_change.text, "0 item(s) - $0.00")

    def test_check_currency_is_pound(self):
        currency_dropdown = self.driver.find_element_by_css_selector("#form-currency > div > button")
        currency_dropdown.click()
        select_pound = self.driver.find_element_by_css_selector("#form-currency > div > ul > li:nth-child(2) > button")
        select_pound.click()
        check_currency_change = self.driver.find_element_by_css_selector("#cart-total")
        self.assertEqual(check_currency_change.text, "0 item(s) - £0.00")


