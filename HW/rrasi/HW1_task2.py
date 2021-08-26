#Please, write integration tests by Selenium WebDriver to verify some features of Open Cart Application.
#Please develop next methods in the FirstSeleniumTest class

#checkMacSearch method - to check the functionality of a simple search;
#Expected to receive 'iMac', 'MacBook', 'MacBook Air' and 'MacBook Pro' in the case of searching by keyword 'mac';
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
        PHRASE = 'mac'
        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("mac")
        search_input.send_keys(Keys.ENTER)
#        element.btm.click()
#        time.sleep(3)
        element2 = self.driver.find_element_by_xpath('//*[@id="content"]/div/section/form/ul/p')

        self.assertEqual("No results found.", element2.text)
        self.assertEqual(element2.value_of_css_property("color"), 'rgba(68, 68, 68, 1)')

# Verify that at least one search result contains the search phrase
#        xpath = f"//*[@id="search"]/input"]/input']//*[contains(text(), '{PHRASE}')]"
#        phrase_results = self.find_elements_by_xpath(xpath)
#        assert len(phrase_results) > 0


