#- addQuantityInCartByXPath - to check the functionality of adding items to cart.

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
        search_input = self.driver.find_element_by_xpath(".//input[@name='search']")
        search_input.send_keys("Xiaomi Mi 8")
        search_button = self.driver.find_element_by_xpath('//span[@class="input-group-btn"]')
        search_button.click()
        add_to_cart = self.driver.find_element_by_xpath('(//span[contains (text(), "Add to Cart")])')
        add_to_cart.click()
        time.sleep(3)
        option_btn = self.driver.find_element_by_xpath('.//*[@id="input-option224"]')
        time.sleep(2)
#div[@class="form-group required"]
#//select[@id="input-option224"]/option[@value="14"]
        option_btn.click()
        time.sleep(3)
        select_size = self.driver.find_element_by_xpath('.//*[@id="input-option224"]/option[2]')
        select_size.click()
        time.sleep(3)
        add_quantity = self.driver.find_element_by_xpath('.//*[@id="input-quantity"]')
        add_quantity.clear()
        add_quantity.send_keys("2")
        time.sleep(2)
        add_product_btn = self.driver.find_element_by_xpath('//*[@id="button-cart"]')
        add_product_btn.click()
        time.sleep(2)


        open_cart = self.driver.find_element_by_xpath('//span[contains (text(), "Shopping Cart")]')
#
        open_cart.click()
        time.sleep(3)
        check_add_to_cart = self.driver.find_element_by_xpath('//*[@name="quantity[5017]" and @value="2"]')
#        ('//*[@id="content"]/form/div/table/tbody/tr/td[2]/a')
        expected_results = ["2"]

        self.assertEqual(check_add_to_cart.text, '2')