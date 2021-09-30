import time
from unittest import TestCase
from selenium import webdriver

from HW.nnavrotska.open_cart_website.elements.label import Label
from HW.nnavrotska.open_cart_website.pages.home_page import HomePage


class CheckCurrencyChange(TestCase):
    driver = None

    def setUp(self):
        self.driver.get('http://taqc-opencart.epizy.com/')
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_checkCurrencyChange_euro(self):
        self.home_page \
            .get_header() \
            .currency_dropdown \
            .click() \
            .select_euro()

        self.assertEqual('€', self.home_page.get_currency_symbol())
        self.assertIn('€', self.home_page.get_cart_btn())
        self.assertIn('€', self.home_page.get_product_price())
        self.assertIn('€', self.home_page.get_tax_price())
        self.assertIn('€', self.home_page.check_all_price_class_name())
        self.assertIn('€', self.home_page.check_all_price_new_class_name())
        self.assertIn('€', self.home_page.check_all_price_old_class_name())
        self.assertIn('€', self.home_page.check_all_price_tax_class_name())

    def test_checkCurrencyChange_pound(self):
        self.home_page \
            .get_header() \
            .currency_dropdown \
            .click() \
            .select_pound()

        self.assertEqual('£', self.home_page.get_currency_symbol())
        self.assertIn('£', self.home_page.get_cart_btn())
        self.assertIn('£', self.home_page.get_product_price())
        self.assertIn('£', self.home_page.get_tax_price())
        self.assertIn('£', self.home_page.check_all_price_class_name())
        self.assertIn('£', self.home_page.check_all_price_new_class_name())
        self.assertIn('£', self.home_page.check_all_price_old_class_name())
        self.assertIn('£', self.home_page.check_all_price_tax_class_name())

    def test_checkCurrencyChange_dollar(self):
        self.home_page \
            .get_header() \
            .currency_dropdown \
            .click() \
            .select_dollar()

        self.assertEqual('$', self.home_page.get_currency_symbol())
        self.assertIn('$', self.home_page.get_cart_btn())
        self.assertIn('$', self.home_page.get_product_price())
        self.assertIn('$', self.home_page.get_tax_price())
        self.assertIn('$', self.home_page.check_all_price_class_name())
        self.assertIn('$', self.home_page.check_all_price_new_class_name())
        self.assertIn('$', self.home_page.check_all_price_old_class_name())
        self.assertIn('$', self.home_page.check_all_price_tax_class_name())