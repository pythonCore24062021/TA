import time
from unittest import TestCase
from selenium import webdriver


class FirstSeleniumTest(TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_checkCurrencyChange_euro(self): # test to be changed and moved to CurrencyChangeTest class
        currency_btn = self.driver.find_element_by_css_selector('#form-currency > div > button')
        currency_btn.click()
        euro = self.driver.find_element_by_css_selector('#form-currency > div > ul > li:nth-child(1) > button')
        euro.click()
        euro_symbol = self.driver.find_element_by_css_selector('#form-currency > div > button > strong')
        cart_btn = self.driver.find_element_by_css_selector('#cart-total')
        product_price = self.driver.find_element_by_css_selector(
            '#content > div.row > div:nth-child(1) > div > div.caption > p.price')
        tax_price = self.driver.find_element_by_css_selector(
            '#content > div.row > div:nth-child(1) > div > div.caption > p.price > span')

        self.assertEqual(euro_symbol.text, '€')
        self.assertIn('€', cart_btn.text)
        self.assertIn('€', product_price.text)

        for element in self.driver.find_elements_by_class_name('price'):
            self.assertIn('€', element.text)
        for element in self.driver.find_elements_by_class_name('price-new'):
            self.assertIn('€', element.text)
        for element in self.driver.find_elements_by_class_name('price-old'):
            self.assertIn('€', element.text)
        for element in self.driver.find_elements_by_class_name('price-tax'):
            self.assertIn('€', element.text)

    def test_checkCurrencyChange_pound(self): # test to be changed and moved to CurrencyChangeTest class
        currency_element = self.driver.find_element_by_css_selector('#form-currency > div > button')
        currency_element.click()
        pound = self.driver.find_element_by_css_selector('#form-currency > div > ul > li:nth-child(2) > button')
        pound.click()
        pound_symbol = self.driver.find_element_by_css_selector('#form-currency > div > button > strong')
        cart_btn = self.driver.find_element_by_css_selector('#cart-total')
        product_price = self.driver.find_element_by_css_selector(
            '#content > div.row > div:nth-child(1) > div > div.caption > p.price')

        self.assertEqual(pound_symbol.text, '£')
        self.assertIn('£', cart_btn.text)
        self.assertIn('£', product_price.text)

        for element in self.driver.find_elements_by_class_name('price'):
            self.assertIn('£', element.text)
        for element in self.driver.find_elements_by_class_name('price-new'):
            self.assertIn('£', element.text)
        for element in self.driver.find_elements_by_class_name('price-old'):
            self.assertIn('£', element.text)
        for element in self.driver.find_elements_by_class_name('price-tax'):
            self.assertIn('£', element.text)

    def test_checkCurrencyChange_dollar(self): # test to be changed and moved to CurrencyChangeTest class
        currency_element = self.driver.find_element_by_css_selector('#form-currency > div > button')
        currency_element.click()
        dollar = self.driver.find_element_by_css_selector('#form-currency > div > ul > li:nth-child(3) > button')
        dollar.click()
        dollar_symbol = self.driver.find_element_by_css_selector('#form-currency > div > button > strong')
        cart_btn = self.driver.find_element_by_css_selector('#cart-total')
        product_price = self.driver.find_element_by_css_selector(
            '#content > div.row > div:nth-child(1) > div > div.caption > p.price')

        self.assertEqual(dollar_symbol.text, '$')
        self.assertIn('$', cart_btn.text)
        self.assertIn('$', product_price.text)

        for element in self.driver.find_elements_by_class_name('price'):
            self.assertIn('$', element.text)
        for element in self.driver.find_elements_by_class_name('price-new'):
            self.assertIn('$', element.text)
        for element in self.driver.find_elements_by_class_name('price-old'):
            self.assertIn('$', element.text)
        for element in self.driver.find_elements_by_class_name('price-tax'):
            self.assertIn('$', element.text)
