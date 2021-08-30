"""
HW02
Please, write integration tests by Selenium WebDriver to verify some features of Open Cart Application.
Please develop next methods in the `FirstSeleniumTest` class

- checkCurrencyChange method - to check currency change on page; Check out three cases of choosing on webpage: Dollar,
  Euro and Pound Sterling;
- checkMacSearch method - to check the functionality of a simple search; Expected to receive 'iMac', 'MacBook',
  'MacBook Air' and 'MacBook Pro' in the case of  searching by keyword 'mac';
- checkAddToCart method - to check the functionality of adding items 'Xiaomi Mi 8' and 'MacBook' to cart.
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\dev\Python\TA with Python - SoftServe\chromedriver\chromedriver.exe")


class FirstSeleniumTest(unittest.TestCase):

    def setUp(self):
        driver.get("http://taqc-opencart.epizy.com/")

    def tearDown(self):
        driver.quit()

    def test_check_currency_change(self):

        # Verifications for Euro
        currency_dropdown = driver.find_element_by_xpath('.//div[@class="btn-group"]')
        currency_dropdown.click()
        euro_button = driver.find_element_by_xpath('.//button[@name="EUR"]')
        euro_button.click()
        currency_sign = driver.find_element_by_xpath('.//button[@class="btn btn-link dropdown-toggle"]/strong')
        self.assertEqual(currency_sign.text, "€")

        # Verifications for Pound
        currency_dropdown = driver.find_element_by_xpath('.//div[@class="btn-group"]')
        currency_dropdown.click()
        pound_button = driver.find_element_by_xpath('.//button[@name="GBP"]')
        pound_button.click()
        currency_sign = driver.find_element_by_xpath('.//button[@class="btn btn-link dropdown-toggle"]/strong')
        self.assertEqual(currency_sign.text, "£")

        # Verification for USD
        currency_dropdown = driver.find_element_by_xpath('.//div[@class="btn-group"]')
        currency_dropdown.click()
        dollar_button = driver.find_element_by_xpath('.//button[@name="USD"]')
        dollar_button.click()
        currency_sign = driver.find_element_by_xpath('.//button[@class="btn btn-link dropdown-toggle"]/strong')
        self.assertEqual(currency_sign.text, "$")

    def test_check_mac_search(self):
        # Entering data in search field and executing search
        search_field = driver.find_element_by_xpath('.//input[@name="search"]')
        search_field.send_keys("mac")
        search_field.send_keys(Keys.ENTER)

        # Finding web elements with search result names
        search_results = driver.find_elements_by_xpath('.//div[@class="caption"]/h4')

        # Defining Expected Result
        expected_results = ['iMac', 'MacBook', 'MacBook Air', 'MacBook Pro']

        # Defining Actual Result
        actual_results = []
        for result in search_results:
            actual_results.append(result.text)

        # Comparing expected and actual
        self.assertListEqual(expected_results, actual_results)

    def test_check_add_to_cart(self):
        # check the functionality of adding items 'Xiaomi Mi 8' and 'MacBook' to cart.

        # search for 'Xiaomi Mi 8' and press add_to_cart
        search_field = driver.find_element_by_xpath('.//input[@name="search"]')
        search_field.send_keys("Xiaomi Mi 8")
        search_field.send_keys(Keys.ENTER)
        result = driver.find_element_by_xpath('.//div[@class="caption"]/h4')
        self.assertEqual(result.text, "Xiaomi Mi 8")
        add_to_cart_button = driver.find_element_by_xpath('.//div[@class="button-group"]/button')
        add_to_cart_button.click()
        time.sleep(1)

        # Select size and confirm
        size_dropdown = driver.find_element_by_xpath('.//select[@id="input-option224"]')
        size_dropdown.click()
        size_dropdown.send_keys(Keys.DOWN)
        size_dropdown.send_keys(Keys.ENTER)

        # add Xiaomi to Cart
        add_to_cart_final = driver.find_element_by_xpath('.//button[@id="button-cart"]')
        add_to_cart_final.click()

        # search for 'MacBook' and  add_to_cart
        search_field = driver.find_element_by_xpath('.//input[@name="search"]')
        search_field.send_keys("MacBook")
        search_field.send_keys(Keys.ENTER)
        result = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[1]/div/div[2]/div[1]/h4/a') # redo
        self.assertEqual(result.text, "MacBook")
        add_to_cart_button = driver.find_element_by_xpath('.//div[@class="button-group"]/button')
        add_to_cart_button.click()
        time.sleep(1)

        # Verify that there are 2 items in CART
        cart_button = driver.find_element_by_xpath('.//span[@id="cart-total"]')
        self.assertIn('2 item(s)', cart_button.text)
