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

    def test_loginByCssSelector_success(self):  # test to be changed and moved to RegisteredUserTest class
        my_account = self.driver.find_element_by_css_selector(
            '#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md')
        my_account.click()
        time.sleep(1)
        login = self.driver.find_element_by_css_selector(
            '#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a')
        login.click()
        time.sleep(1)
        email = self.driver.find_element_by_css_selector('#input-email')
        email.send_keys('testing@gmail.com')
        password = self.driver.find_element_by_css_selector('#input-password')
        password.send_keys('test')
        login_btn = self.driver.find_element_by_css_selector('#content > div > div:nth-child(2) > div > form > input')
        login_btn.click()
        time.sleep(1)
        my_account_content = self.driver.find_element_by_css_selector('#content > h2:nth-child(1)')
        self.assertEqual(self.driver.current_url, 'http://taqc-opencart.epizy.com/index.php?route=account/account')
        self.assertEqual(my_account_content.text, 'My Account')

#User class - to send parameters of checkRegister method of RegisterTest class;