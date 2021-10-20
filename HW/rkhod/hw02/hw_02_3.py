import time
import unittest
from selenium import webdriver


class OpenCartApp(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)
        self.driver.refresh()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="c:\\selenium browser drivers\\chromedriver.exe")
        cls.driver.maximize_window()

    def test_AddToCart1(self):
        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("Xiaomi Mi 8")
        search_btn = self.driver.find_element_by_css_selector("#search > span > button > i")
        search_btn.click()
        time.sleep(1)
        add_btn = self.driver.find_element_by_css_selector("#content > div:nth-child(8) > div > div > div:nth-child(2) > div.button-group > button:nth-child(1) > span")
        add_btn.click()
        time.sleep(1)
        add_size = self.driver.find_element_by_css_selector("#input-option224")
        add_size.click()
        time.sleep(1)
        add_size = self.driver.find_element_by_xpath('//*[@id="input-option224"]/option[2]')
        add_size.click()
        time.sleep(1)
        add_btn = self.driver.find_element_by_css_selector("#button-cart")
        add_btn.click()
        time.sleep(1)
        total = self.driver.find_element_by_css_selector("#cart > ul > li:nth-child(1) > table > tbody > tr > td.text-left > a")
        self.assertIn(total.text, "Xiaomi Mi 8")

    def test_AddToCart2(self):
        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("MacBook")
        search_btn = self.driver.find_element_by_css_selector("#search > span > button > i")
        search_btn.click()
        time.sleep(1)
        add_btn = self.driver.find_element_by_css_selector("#content > div:nth-child(8) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(1) > span")
        add_btn.click()
        time.sleep(1)
        add_btn = self.driver.find_element_by_id("cart-total")
        add_btn.click()
        time.sleep(1)
        total = self.driver.find_element_by_css_selector("#cart > ul > li:nth-child(1) > table > tbody > tr > td.text-left")
        self.assertIn(total.text, "MacBook")