import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class FirstSeleniumTest(unittest.TestCase):
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

    def test_euro_search(self):
        currency = self.driver.find_element_by_css_selector('#form-currency > div > button > span')
        currency.click()
        euro = self.driver.find_element_by_css_selector('#form-currency > div > ul > li:nth-child(1) > button')
        euro.click()
        currency_change = self.driver.find_element_by_css_selector('#cart-total')
        self.assertEqual(currency_change.text, "0 item(s) - 0.00€")

    def test_dollar_search(self):
        currency = self.driver.find_element_by_css_selector('#form-currency > div > button > span')
        currency.click()
        dollar = self.driver.find_element_by_css_selector('#form-currency > div > ul > li:nth-child(3) > button')
        dollar.click()
        currency_change = self.driver.find_element_by_css_selector('#cart-total')
        self.assertEqual(currency_change.text, "0 item(s) - $0.00")

    def test_pound_search(self):
        currency = self.driver.find_element_by_css_selector('#form-currency > div > button > span')
        currency.click()
        dollar = self.driver.find_element_by_css_selector('#form-currency > div > ul > li:nth-child(2) > button')
        dollar.click()
        currency_change = self.driver.find_element_by_css_selector('#cart-total')
        self.assertEqual(currency_change.text, "0 item(s) - £0.00")

