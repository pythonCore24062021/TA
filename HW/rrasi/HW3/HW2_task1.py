## HW03
#Please, write integration tests by Selenium WebDriver to verify some features of Open Cart Application.
# Use only CSS selectors to search of all web elements on site.
#Please develop next methods in the `SearchTest` class

#- loginByCssSelector method - to check the functionality of login;

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

        my_acount_btm = self.driver.find_element_by_css_selector(
            "#top-links > ul > li.dropdown > a"
        )
        my_acount_btm.click()
        login_btn = self.driver.find_element_by_css_selector(
            "#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a")
        login_btn.click()
        email_input = self.driver.find_element_by_css_selector("#input-email")
        email_input.send_keys("rusichka85d@gmail.com")
        password_input = self.driver.find_element_by_css_selector("#input-password")
        password_input.send_keys("Pankivskogo151")

        login_btn = self.driver.find_element_by_css_selector("#content > div > div:nth-child(2) > div > form > input")
        login_btn.click()







