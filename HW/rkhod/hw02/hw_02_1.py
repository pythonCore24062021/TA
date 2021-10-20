import time
import unittest
from selenium import webdriver


class OpenCartApp(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="c:\\selenium browser drivers\\chromedriver.exe")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_checkCurrencyUSD_items(self):
        btn_currency = self.driver.find_element_by_css_selector("#form-currency > div > button > span")
        btn_currency.click()
        usd_currency = self.driver.find_element_by_name("USD")
        usd_currency.click()
        currency = self.driver.find_element_by_css_selector("#cart-total")
        self.assertIn(currency.text, "0 item(s) - $0.00")

    def test_CheckCurrencyEUR_items(self):
        btn_currency = self.driver.find_element_by_css_selector("#form-currency > div > button > span")
        btn_currency.click()
        eu_currency = self.driver.find_element_by_name("EUR")
        eu_currency.click()
        currency = self.driver.find_element_by_css_selector("#cart-total")
        self.assertIn(currency.text, "0 item(s) - 0.00€")

    def test_CheckCurrencyGBP_items(self):
        btn_currency = self.driver.find_element_by_css_selector("#form-currency > div > button > span")
        btn_currency.click()
        eu_currency = self.driver.find_element_by_name("GBP")
        eu_currency.click()
        currency = self.driver.find_element_by_css_selector("#cart-total")
        self.assertIn(currency.text, "0 item(s) - £0.00")
