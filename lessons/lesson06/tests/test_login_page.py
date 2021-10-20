import time
import unittest

from selenium import webdriver

from pages.home import Home


class TestLoginPage(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")
        time.sleep(1)
        self.home = Home(self.driver)

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_first_reg_user(self):
        login_page = self.home \
            .get_my_account() \
            .click() \
            .clickLogin() \
            .set_email("testEmail") \
            .set_password("testPasword") \
            .click_login()

        self.assertEqual(login_page.get_warning().get_message(), 'Warning: No match for E-Mail Address and/or Password.')
