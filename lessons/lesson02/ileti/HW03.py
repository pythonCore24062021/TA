import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")
        time.sleep(2)
    def TearDown(self):
        time.sleep(1)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_loginByCssSelector(self):
        my_acount_btm = self.driver.find_element_by_css_selector(
            "#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md"
        )
        my_acount_btm.click()
        reg_btn = self.driver.find_element_by_css_selector(
            "#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a")
        reg_btn.click()
        element = self.driver.find_element_by_css_selector('#input-firstname')
        element.send_keys("Barbara")
        element2 = self.driver.find_element_by_css_selector("#input-lastname")
        element2.send_keys("Koachello")
        element3 = self.driver.find_element_by_css_selector("#input-email")
        element3.send_keys("barbara@Koachello.com")
        element4 = self.driver.find_element_by_css_selector("#input-address-1")
        element4.send_keys("New York city")
        time.sleep(2)
        element5 = self.driver.find_element_by_css_selector("#input-city")
        element5.send_keys("Nee York city")
        element6 = self.driver.find_element_by_css_selector("#input-postcode")
        element6.send_keys("79017")
        element7 = self.driver.find_element_by_css_selector("#input-telephone")
        element7.send_keys("23424253")
        element8 = self.driver.find_element_by_css_selector("#input-zone")
        element8.send_keys("Aberdeen")
        time.sleep(2)
        element9 = self.driver.find_element_by_css_selector("#input-password")
        element9.send_keys("NewYork")
        element10 = self.driver.find_element_by_css_selector("#input-confirm")
        element10.send_keys("NewYork")
        element11 = self.driver.find_element_by_css_selector("#content > form > div > div > input[type=checkbox]:nth-child(2)")
        element11.click()
        element12 = self.driver.find_element_by_css_selector("#content > form > div > div > input.btn.btn-primary")
        element12.click()
        time.sleep(2)
        self.assertIn("Congratulations", self.driver.page_source)
        time.sleep(5)

    def test_findByCss(self):
        searchElement = self.driver.find_element_by_css_selector("#search > input")
        searchElement.send_keys("test for search")
        searchElement.send_keys(Keys.ENTER)
        time.sleep(2)
