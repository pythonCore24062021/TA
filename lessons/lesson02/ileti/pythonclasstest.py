import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.python.org/")
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
    def test_search1(self):
        element = self.driver.find_element_by_id("id-search-field")
        element.send_keys("python")
        element.send_keys(Keys.ENTER)
        # s = self.driver.page_source
        # s.find("No result found")
        self.assertNotIn("No result found", self.driver.page_source)

    def test_search2(self):
        element = self.driver.find_element_by_id("id-search-field")
        element.send_keys("python22222fff")
        element.send_keys(Keys.ENTER)
        self.assertIn("No results found", self.driver.page_source)

    def test_search21(self):
        element = self.driver.find_element_by_id("id-search-field")
        element.send_keys("python22222fff")
        element.send_keys(Keys.ENTER)
        element2 = self.driver.find_element_by_xpath('//*[@id="content"]/div/section/form/ul/p')
        self.assertEqual("No results found.", element2.text)
        self.assertEqual(element2.value_of_css_property("color"), 'rgba(68, 68, 68, 1)')
