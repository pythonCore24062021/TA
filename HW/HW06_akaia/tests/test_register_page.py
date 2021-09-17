"""
Tests related to Register functionality
"""

import unittest
from selenium import webdriver
from pages.home_page import HomePage
from utils.data_manager import Credentials

import time

"""Getting test data from Google sheet"""
credentials = Credentials("1rr1dzPSwa6qx6jarzbtXdWBSg5DsNsknmn2dWckmnvk")
email = credentials.get_register_email() + str(round(time.time() * 1000)), '@gmail.com'
password = credentials.get_register_password()


class TestRegister(unittest.TestCase):
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

    def test_register_mandatory_fields_only(self):
        register_page = self.home_page.\
            get_my_account().\
            click().\
            click_register().\
            set_first_name('John').\
            set_last_name('Doe').\
            set_email(email).\
            set_phone('1234567').\
            set_address('Pushkina str.').\
            set_city('Kyiv').\
            set_post_code('0420').\
            set_region_state().\
            set_password(password).\
            set_password_confirm(password).\
            check_checkbox_privacy().\
            click_continue_btn()

        self.assertEqual(register_page.get_current_url(),
                         "http://taqc-opencart.epizy.com/index.php?route=account/success")
