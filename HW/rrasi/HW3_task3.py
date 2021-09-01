#- addToCartByXPath - to check the functionality of adding items to cart;

import time
import unittest

from selenium import webdriver


def temp():
    tem = 1


class PythonOrgSearch(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")
        temp()
        temp()
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

    def test_checkAddToCart (self):
        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("Xiaomi Mi 8")
        search_button = self.driver.find_element_by_css_selector('#search > span > button > i')
        search_button.click()
        add_to_cart = self.driver.find_element_by_css_selector('#content > div:nth-child(8) > div > div > div:nth-child(2) > div.button-group > button:nth-child(1) > span')
        add_to_cart.click()
        time.sleep(5)
        option_btn = self.driver.find_element_by_css_selector('#input-option224')
        option_btn.click()
        time.sleep(3)
        select_size = self.driver.find_element_by_xpath('.//*[@id="input-option224"]/option[2]')
        select_size.click()
        time.sleep(3)
        add_product_btn = self.driver.find_element_by_xpath('//*[@id="button-cart"]')
        add_product_btn.click()

        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("MacBook")
        search_button = self.driver.find_element_by_css_selector('#search > span > button > i')
        search_button.click()
        add_second_item_button = self.driver.find_element_by_css_selector(
            ' #content > div:nth-child(8) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(1)')
        add_second_item_button.click()
        open_cart = self.driver.find_element_by_css_selector('#top-links > ul > li:nth-child(4) > a > span')
        open_cart.click()
        check_add_to_cart = self.driver.find_elements_by_css_selector(
            "#content > form > div > table > tbody > tr > td:nth-child(2) > a")  # td.text-left > a
        check_cart_items = list()
        for cart_item in check_add_to_cart:
            check_cart_items.append(cart_item.text)

        expected_results = ["Xiaomi Mi 8", "MacBook"]

        self.assertTrue(set(check_cart_items) & set(expected_results))