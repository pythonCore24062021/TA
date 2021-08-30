"""
HW04
Please, write integration tests by Selenium WebDriver to verify some features of Open Cart Application.
Search for web elements only by XPAth. Please develop next methods in the SearchXPathTest class

- loginByCssSelectOriginByXPath method - to check the functionality of login;
- findByXPath method - to check the functionality of a simple search;
- addToCartByXPath - to check the functionality of adding items to cart;
- addQuantityInCartByXPath - to check the functionality of adding items to cart.
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Calling web driver from a specific folder not to mess things up
driver = webdriver.Chrome("C:\dev\Python\TA with Python - SoftServe\chromedriver\chromedriver.exe")
driver.maximize_window()


class FirstSeleniumTest(unittest.TestCase):

    def setUp(self):
        driver.get("http://taqc-opencart.epizy.com/")

    def tearDown(self):
        driver.get('chrome://settings/clearBrowserData')
        driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)

    @classmethod
    def tearDownClass(cls):
        driver.quit()

    def testLoginByCssSelectOriginByXPath(self):
        # Find and then click "My Account" button and "Log in button"
        my_account_button = driver.find_element_by_xpath('.//li[@class="dropdown"]/a[@title="My Account"]')
        my_account_button.click()
        login_button = driver.find_element_by_xpath('.//ul[@class="dropdown-menu dropdown-menu-right"]/li[2]')
        login_button.click()

        # Enter data in E-Mail and Password field and login
        email_textbox = driver.find_element_by_xpath('.//input[@name="email"]')
        password_textbox = driver.find_element_by_xpath('.//input[@name="password"]')
        email = 'test_for_food@gmail.com'
        password = '12345'
        email_textbox.send_keys(email)
        password_textbox.send_keys(password)
        password_textbox.send_keys(Keys.ENTER)

        # Verify that user was redirected to url of logged in user
        self.assertEqual(driver.current_url, 'http://taqc-opencart.epizy.com/index.php?route=account/account')

    def findByXPath(self):
        """check the functionality of a simple search. Find all elements by xpath"""

        # Entering data in search field and executing search
        search_field = driver.find_element_by_xpath('.//input[@name="search"]')
        search_field.send_keys("mac")
        search_field.send_keys(Keys.ENTER)

        # Finding web elements with search result names listed
        search_results = driver.find_elements_by_xpath('.//div[@class="caption"]/h4')

        # Defining Expected Result
        expected_results = ['iMac', 'MacBook', 'MacBook Air', 'MacBook Pro']

        # Defining Actual Result
        actual_results = []
        for result in search_results:
            actual_results.append(result.text)

        # Comparing expected and actual
        self.assertListEqual(expected_results, actual_results)

    def testAddToCartByXPath(self):
        """Adding all items from search to cart"""

        # Entering data in search field and executing search
        search_field = driver.find_element_by_xpath('.//input[@name="search"]')
        search_field.send_keys("MacBook")
        search_field.send_keys(Keys.ENTER)

        # Finding "Add To Cart" button for each search result
        search_results = driver.find_elements_by_xpath('.//div[@class="button-group"]')

        # Adding each item to cart
        for item in search_results:
            item.click()
            time.sleep(1)

        # Find "Cart button"
        cart_button = driver.find_element_by_xpath('.//span[@id="cart-total"]')

        # verify that all added items are present in the Cart by clicking on Cart and verifying it
        cart_button.click()
        cart_item_names = driver.find_elements_by_xpath('.//td[@class="text-left"]/a')
        actual_item_names = [item.text for item in cart_item_names]
        expected_item_names = ['MacBook', 'MacBook Air', 'MacBook Pro']
        self.assertListEqual(expected_item_names, actual_item_names)

    def testAddQuantityInCartByXPath(self):
        """Adding items from search to cart one by one and verifying
        that quantity increases each time"""

        # Entering data in search field and executing search
        search_field = driver.find_element_by_xpath('.//input[@name="search"]')
        search_field.send_keys("MacBook")
        search_field.send_keys(Keys.ENTER)

        # Finding "Add To Cart" button for each search result
        search_results = driver.find_elements_by_xpath('.//div[@class="button-group"]')

        # Adding each item to cart and verifying number of items in cart
        num = 1
        for item in search_results:
            item.click()
            time.sleep(5) # sleeping since button needs to load first
            # Find "Cart button"
            cart_button = driver.find_element_by_xpath('.//span[@id="cart-total"]')
            expected_text = str(num) + ' item(s)'
            self.assertIn(expected_text, cart_button.text)
            num = num+1
