##- findByCss method - to check the functionality of a simple search;
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

    def test_first_reg_user(self):
        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("mac")
        search_btn = self.driver.find_element_by_css_selector("#search > span > button > i")
        search_btn.click()





