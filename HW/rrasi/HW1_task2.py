#Please, write integration tests by Selenium WebDriver to verify some features of Open Cart Application.
#Please develop next methods in the FirstSeleniumTest class

#checkMacSearch method - to check the functionality of a simple search;
#Expected to receive 'iMac', 'MacBook', 'MacBook Air' and 'MacBook Pro' in the case of searching by keyword 'mac';
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://taqc-opencart.epizy.com/")

class FirstSeleniumTest(unittest.TestCase):
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

