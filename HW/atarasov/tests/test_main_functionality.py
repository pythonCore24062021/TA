import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from HW.atarasov.pages.base_page import BasePage
from HW.atarasov.pages.landing_page import LandingPage
from HW.atarasov.data.constants import LANDING_PAGE_URL


class TestRunner(unittest.TestCase):
    driver = None
    landing_page = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.landing_page = LandingPage(cls.driver)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# Home Work №2
class FirstSeleniumTest(TestRunner):

    def setUp(self):
        self.driver.delete_all_cookies()
        self.landing_page.go_to_landing_page()

    def tearDown(self):
        self.driver.close()

    def test_currency_usd(self):
        self.landing_page.change_currency_using_css('USD')
        self.assertTrue(self.landing_page.verify_currency_change('USD'), "Something is wrong - currency wasn't changed")

    def test_currency_eur(self):
        self.landing_page.change_currency_using_css('EUR')
        self.assertTrue(self.landing_page.verify_currency_change('EUR'), "Something is wrong - currency wasn't changed")

    def test_currency_gbp(self):
        self.landing_page.change_currency_using_css('GBP')
        self.assertTrue(self.landing_page.verify_currency_change('GBP'), "Something is wrong - currency wasn't changed")

    def test_mac_search(self):
        self.landing_page.make_search_request('Mac')
        self.assertTrue(self.landing_page.verify_search_results({'iMac', 'MacBook', 'MacBook Air', 'MacBook Pro'}))

    def test_add_to_cart(self):
        self.landing_page.make_search_request('xiaomi mi 8')
        self.landing_page.add_item_to_cart('Xiaomi Mi 8')
        self.landing_page.make_search_request('macbook')
        self.landing_page.add_item_to_cart('MacBook')
        self.assertTrue(self.landing_page.verify_items_present_in_cart({'Xiaomi Mi 8', 'MacBook'}))


# Home Work №3
class LoginWithCssSearch(TestRunner):

    def setUp(self):
        self.driver.delete_all_cookies()
        self.landing_page.go_to_landing_page()

    def tearDown(self):
        self.driver.close()

    def test_login_using_css(self):
        pass

    def test_simple_search_using_css(self):
        pass


# Home Work №4
class TestsUsingXpath(TestRunner):

    def setUp(self):
        self.driver.delete_all_cookies()
        self.landing_page.go_to_landing_page()

    def tearDown(self):
        self.driver.close()

    def test_login_using_xpath(self):
        pass

    def test_simple_search_using_xpath(self):
        pass

    def test_add_to_cart_using_xpath(self):
        pass

    def test_adding_quantity_to_cart_by_xpath(self):
        pass


# Home Work №5
class SearchWithExplicitWaiters(TestRunner):

    def setUp(self):
        self.driver.delete_all_cookies()
        self.landing_page.go_to_landing_page()

    def tearDown(self):
        self.driver.close()

    def test_something(self):
        pass


if __name__ == '__main__':
    unittest.main()
