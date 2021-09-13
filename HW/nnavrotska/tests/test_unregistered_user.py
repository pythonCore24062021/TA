import time
from unittest import TestCase, defaultTestLoader

from selenium import webdriver


class SearchTest(TestCase):
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

    def test_loginByCssSelector_with_empty_fields(self):  # test to be changed and moved to UnregisteredUserTest class
        my_accout_dropdown = self.driver.find_element_by_css_selector('#top-links > ul > li.dropdown')
        my_accout_dropdown.click()
        time.sleep(1)
        dropdown_options = self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul')
        login = self.driver.find_element_by_css_selector(
            '#top-links > ul > li.dropdown.open > ul > li:nth-child(2)')
        time.sleep(2)
        login.click()
        login_btn = self.driver.find_element_by_css_selector(
            '#content > div > div:nth-child(2) > div > form > input')
        login_btn.click()
        warning_msg = self.driver.find_element_by_css_selector('body > div:nth-child(4) > div.alert.alert-danger')
        self.assertEqual(warning_msg.get_property('innerText'),
                         ' Warning: No match for E-Mail Address and/or Password.')
