import time
from unittest import TestCase

from selenium import webdriver
from HW.nnavrotska.open_cart_website.locators.home_page_locators import HomePageLocators
from HW.nnavrotska.open_cart_website.pages.home_page import HomePage


class TestLoginPage(TestCase):
    driver = None

    def setUp(self):
        self.driver.get(HomePageLocators.HOME_URL)
        time.sleep(1)
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

    def test_check_successful_login_ByCssSelector(self):
        login_page = self.home_page \
            .get_header() \
            .account_dropdown \
            .click() \
            .click_login() \
            .set_email('testing@gmail.com') \
            .set_psw('test') \
            .click_login()

        self.assertEqual(login_page.get_current_path(),
                         'http://taqc-opencart.epizy.com/index.php?route=account/account')
