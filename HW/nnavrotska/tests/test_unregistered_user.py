import time
from unittest import TestCase

from selenium import webdriver

from HW.nnavrotska.open_cart_website.locators.home_page_locators import HomePageLocators
from HW.nnavrotska.open_cart_website.pages.home_page import HomePage


class UnregisteredUserTest(TestCase):
    driver = None

    def setUp(self):
        self.driver.get(HomePageLocators.HOME_URL)
        time.sleep(2)
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

    def test_check_unsuccessful_login_with_empty_fields(self):
        login_page = self.home_page \
            .get_header() \
            .account_dropdown \
            .click() \
            .click_login() \
            .click_login()

        self.assertEqual(login_page.get_warning().get_text(), 'Warning: No match for E-Mail Address and/or Password.')
