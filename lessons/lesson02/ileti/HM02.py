import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FirstSeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://taqc-opencart.epizy.com/?i=1')

    def TearDown(self):
        time.sleep(1)
        self.driver.quit()
    def test_checkCurrencyChange_dollar(self):
        element = self.driver.find_element_by_css_selector("#content > div.row > div:nth-child(1) > div > div.button-group > button:nth-child(1)")
        element.click()
        self.assertIn("$", self.driver.page_source)
        time.sleep(1)

    def test_checkCurrencyChange_euro(self):
        element = self.driver.find_element_by_css_selector(
            "#content > div.row > div:nth-child(1) > div > div.button-group > button:nth-child(1)")
        element.click()
        currency_check = self.driver.find_element_by_css_selector("#form-currency > div > button > i")
        currency_check.click()
        busket_euro = self.driver.find_element_by_css_selector("#form-currency > div > ul > li:nth-child(1) > button")
        busket_euro.click()
        time.sleep(1)
        self.assertIn("€", self.driver.page_source)

    def test_checkCurrencyChange_pound(self):
        element = self.driver.find_element_by_css_selector(
            "#content > div.row > div:nth-child(1) > div > div.button-group > button:nth-child(1)")
        element.click()
        currency_check = self.driver.find_element_by_css_selector(
            "#form-currency > div > button > i")
        currency_check.click()
        busket_pound = self.driver.find_element_by_css_selector("#form-currency > div > ul > li:nth-child(2) > button")
        busket_pound.click()
        time.sleep(1)
        self.assertIn("£", self.driver.page_source)

    def test_checkMacSearch(self):
        element = self.driver.find_element_by_name("search")
        element.send_keys("mac")
        element.send_keys(Keys.ENTER)
        self.assertIn("Search - mac", self.driver.page_source)
        self.assertIn("iMac", self.driver.page_source)
        self.assertIn("MacBook", self.driver.page_source)
        self.assertIn("MacBook Air", self.driver.page_source)
        self.assertIn("MacBook Pro", self.driver.page_source)
        time.sleep(5)

     def test_checkAddToCart(self):
