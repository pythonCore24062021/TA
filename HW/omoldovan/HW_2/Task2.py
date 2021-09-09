import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class FirstSeleniumTest(unittest.TestCase):
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

    def test_check_mac_search_(self):
        search = self.driver.find_element_by_css_selector('#search > input')
        search.send_keys("mac")
        search_btn = self.driver.find_element_by_css_selector("#search > span > button > i")
        search_btn.click()
        items = self.driver.find_element_by_class_name("product-thumb")


