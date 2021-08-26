#Please, write integration tests by Selenium WebDriver to verify some features of Open Cart Application.
#Please develop next methods in the FirstSeleniumTest class

#checkCurrencyChange method - to check currency change on page;
#Check out three cases of choosing on webpage: Dollar, Euro and Pound Sterling;

import time
import unittest

from selenium import webdriver



class PythonOrgSearch(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")

        time.sleep(2)

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def checkCurrencyChange(self):
        currency_btm = self.driver.find_element_by_css_selector(
            "#form-currency > div > button > span"
        )
        currency_btm.click()
        reg_btn = self.driver.find_element_by_css_selector(
            "#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a")
        reg_btn.click()
        first_name_input = self.driver.find_element_by_css_selector("#input-firstname")
        first_name_input.send_keys("lhalam")
        email_input = self.driver.find_element_by_css_selector("#input-email")
        email_input.send_keys("lhalam@l")

        continue_btn = self.driver.find_element_by_css_selector("#content > form > div > div > input.btn.btn-primary")
        continue_btn.click()

        last_name_error_lb = self.driver.find_element_by_css_selector("#account > div:nth-child(4) > div > div")
        self.assertEqual(last_name_error_lb.text,
        "Last Name must be between 1 and 32 characters!")
        try:

            first_name_error_lb = self.driver.find_element_by_css_selector("#account > div:nth-child(3) > div > div")
        except:
            first_name_error_lb = None
        self.assertIsNone(first_name_error_lb)
