import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://taqc-opencart.epizy.com/index.php?route=account/login')

    def TearDown(self):
        time.sleep(1)
        self.driver.quit()

    def test_loginByCssSelector(self):

    # def test_findByCss(self):
