"""
Tests related to Login functionality
"""

import unittest
from selenium import webdriver
from HW.HW06_akaia.pages.home_page import HomePage
from utils.data_manager import Credentials

"""Getting test data from google sheet"""
credentials = Credentials("1rr1dzPSwa6qx6jarzbtXdWBSg5DsNsknmn2dWckmnvk")
email = credentials.get_existing_email()
password = credentials.get_existing_password()


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Go to test page and maximize window"""
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(15)

    @classmethod
    def tearDownClass(cls):
        """Kill the driver"""
        cls.driver.quit()

    def setUp(self):
        """Go to test page"""
        self.driver.get("http://taqc-opencart.epizy.com/")
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        """Remove all cookies to start each new test with virgin data"""
        self.driver.delete_all_cookies()

    def testLoginHappyPath(self):
        """Verify that user can successfully log in using existing account"""
        login_page = self.home_page.\
            get_my_account().\
            click().\
            click_login().\
            set_email(email).\
            set_password(password).\
            click_login_button()

        self.assertEqual(login_page.get_current_url(), "http://taqc-opencart.epizy.com/index.php?route=account/account")
