import time
from unittest import TestCase

from selenium.webdriver.chrome import webdriver
from locators.home_page_locators import HOME_URL
from pages.login_page import login_page
from pages.home_page import HomePage


class TestLoginPage(TestCase):
    driver = None

    def setUp(self):
        self.driver.get(HOME_URL)
        time.sleep(1)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_page(self):
        login_page = self.home_page \
            .get_my_account() \
            .click() \
            .clickLogin() \
            .set_email('testing@gmail.com') \
            .set_psw('test') \
            .click_login()

        self.assertEqual(login_page.get_warning().get_message(), ' Warning: No match for E-Mail Address and/or Password.')

    # to check the functionality of login;
    def test_loginByCssSelectoroginByXPath(self):
        pass

    #checkUnsuccessful method of LoginTest class - to check the functionality of unsuccessfuly login.