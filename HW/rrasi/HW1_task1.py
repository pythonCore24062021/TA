#Please, write integration tests by Selenium WebDriver to verify some features of Open Cart Application.
#Please develop next methods in the FirstSeleniumTest class

#checkCurrencyChange method - to check currency change on page;
#Check out three cases of choosing on webpage: Dollar, Euro and Pound Sterling;

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://taqc-opencart.epizy.com/")

class PythonOrgSearch(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://taqc-opencart.epizy.com/")

    def tearDown(self):
        time.sleep(2)
        # self.driver.quit()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_search1(self):
        element = self.driver.find_element_by_css_selector("#search > input")
        element.send_keys("mac")
        element.send_keys(Keys.ENTER)
#        element.btm.click()
        self.assertNotIn("No results found.", self.driver.page_source)

        def tearDown(self):
            time.sleep(4)

    def test_search2(self):
        element = self.driver.find_element_by_css_selector("#search > input")
        element.send_keys("mac")
        element.send_keys(Keys.ENTER)
        self.assertIn("No results found.", self.driver.page_source)

    def test_search21(self):
        element = self.driver.find_element_by_css_selector("#search > input")
        element.send_keys("mac")
        element.send_keys(Keys.ENTER)

        element2 = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/div/div[2]/h4/a')

        self.assertEqual("No results found.", element2.text)
#        self.assertEqual(element2.value_of_css_property("color"), 'rgba(68, 68, 68, 1)')