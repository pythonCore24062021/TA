# HW04
#Please, write integration tests by Selenium WebDriver to verify some features of Open Cart Application.
# Search for web elements only by XPAth. Please develop next methods in the SearchXPathTest class

# - loginByCssSelectoroginByXPath method - to check the functionality of login;

import time
import unittest

from selenium import webdriver


def temp():
    tem = 1


class PythonOrgSearch(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")
        temp()
        temp()
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

    def test_loginByCssSelector (self):

        my_acount_btm = self.driver.find_element_by_xpath(
            ".//ul/li[2]/a/span[1]"
        )
        my_acount_btm.click()
        login_btn = self.driver.find_element_by_xpath(".//ul/li[2]/ul/li[2]/a")
        login_btn.click()
        email_input = self.driver.find_element_by_xpath(".//input[@name='email']")
        email_input.send_keys("rusichka85d@gmail.com")
        password_input = self.driver.find_element_by_xpath(".//input[@name='password']")
        password_input.send_keys("Pankivskogo151")

        login_btn = self.driver.find_element_by_xpath(".//div/div[2]/div/form/input")
        login_btn.click()
        my_acount = self.driver.find_element_by_xpath(".//h2[1]")
        self.assertEqual(my_acount.text, 'My Account')
#check_currency_change = self.driver.find_element_by_css_selector("#cart-total")
#        self.assertEqual(check_currency_change.text, "0 item(s) - £0.00")
