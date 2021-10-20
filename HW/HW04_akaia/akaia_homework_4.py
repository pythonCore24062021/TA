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


class FirstSeleniumTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        """Go to test page and maximize window"""
        cls.driver = webdriver.Chrome("C:\dev\Python\TA with Python - SoftServe\chromedriver\chromedriver.exe")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        """Kill the driver"""
        cls.driver.quit()

    def setUp(self):
        """Go to test page"""
        self.driver.get('http://taqc-opencart.epizy.com/')

    def tearDown(self):
        """Remove all cookies to start each new test with virgin data"""
        self.driver.delete_all_cookies()

    def testLoginByCssSelectOriginByXPath(self):
        """This test verifies functionality of login. All elements found by XPath"""

        # 1. Create new user
        my_account_button = self.driver.find_element_by_xpath('.//a[@title="My Account"]')
        my_account_button.click()
        register_button = self.driver.find_element_by_xpath('.//li[@class="dropdown open"]/ul/li[1]/a')
        register_button.click()
        self.assertIn('account/register', self.driver.current_url)
        first_name = self.driver.find_element_by_xpath('.//input[@name="firstname"]')
        last_name = self.driver.find_element_by_xpath('.//input[@name="lastname"]')
        email_field = self.driver.find_element_by_xpath('.//input[@name="email"]')
        phone = self.driver.find_element_by_xpath('.//input[@name="telephone"]')
        address_one = self.driver.find_element_by_xpath('.//input[@name="address_1"]')
        city = self.driver.find_element_by_xpath('.//input[@name="city"]')
        post_code = self.driver.find_element_by_xpath('.//input[@name="postcode"]')
        region_state = self.driver.find_element_by_xpath('.//select[@name="zone_id"] ')
        password_field = self.driver.find_element_by_xpath('.//input[@name="password"] ')
        password_confirm = self.driver.find_element_by_xpath('.//input[@name="confirm"] ')
        privacy_checkbox = self.driver.find_element_by_xpath('.//input[@name="agree"] ')
        continue_button = self.driver.find_element_by_xpath('.//input[@type="submit"] ')
        email = 'JDoe' + str(round(time.time() * 1000)), '@gmail.com'
        password = '1234567'
        first_name.send_keys("John")
        last_name.send_keys("Doe")
        email_field.send_keys(email)
        phone.send_keys("1234567")
        address_one.send_keys("Pushkina str. 4/20")
        city.send_keys("Kyiv")
        post_code.send_keys("0241")
        region_state.send_keys(Keys.ENTER)
        region_state.send_keys(Keys.DOWN)
        region_state.send_keys(Keys.ENTER)
        password_field.send_keys(password)
        password_confirm.send_keys("1234567")
        privacy_checkbox.click()
        continue_button.click()
        time.sleep(1)

        # 2. Logging out after registration
        my_account_button = self.driver.find_element_by_xpath('.//a[@title="My Account"]')
        my_account_button.click()
        logout_button = self.driver.find_element_by_xpath('.//a[contains(text(), "Logout")]')
        logout_button.click()
        self.assertIn('account/logout', self.driver.current_url)

        # 3. Login with user credentials from step 1
        my_account_button = self.driver.find_element_by_xpath('.//a[@title="My Account"]')
        my_account_button.click()
        login_button = self.driver.find_element_by_xpath('.//a[contains(text(), "Login")]')
        login_button.click()
        email_textbox = self.driver.find_element_by_xpath('.//input[@name="email"]')
        password_textbox = self.driver.find_element_by_xpath('.//input[@name="password"]')
        submit_button = self.driver.find_element_by_xpath('.//input[@type="submit"]')
        email_textbox.send_keys(email)
        password_textbox.send_keys(password)
        submit_button.click()
        # Verify that user was created
        self.assertIn('account/account', self.driver.current_url)

    def testFindByXPath(self):
        """check the functionality of a simple search. Find all elements by xpath"""

        # Entering data in search field and executing search
        search_field = self.driver.find_element_by_xpath('.//input[@name="search"]')
        search_field.send_keys("mac")
        search_field.send_keys(Keys.ENTER)

        # Finding web elements with search result names listed
        search_results = self.driver.find_elements_by_xpath('.//div[@class="caption"]/h4')

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
        search_field = self.driver.find_element_by_xpath('.//input[@name="search"]')
        search_field.send_keys("MacBook")
        search_field.send_keys(Keys.ENTER)

        # Finding "Add To Cart" button for each search result
        search_results = self.driver.find_elements_by_xpath('.//div[@class="button-group"]')

        # Adding each item to cart
        for item in search_results:
            item.click()
            time.sleep(1)

        # Find "Cart button"
        cart_button = self.driver.find_element_by_xpath('.//span[@id="cart-total"]')

        # verify that all added items are present in the Cart by clicking on Cart and verifying it
        cart_button.click()
        cart_item_names = self.driver.find_elements_by_xpath('.//td[@class="text-left"]/a')
        actual_item_names = [item.text for item in cart_item_names]
        expected_item_names = ['MacBook', 'MacBook Air', 'MacBook Pro']
        self.assertListEqual(expected_item_names, actual_item_names)

    def testAddQuantityInCartByXPath(self):
        """Adding items from search to cart one by one and verifying
        that quantity increases each time"""

        # Entering data in search field and executing search
        search_field = self.driver.find_element_by_xpath('.//input[@name="search"]')
        search_field.send_keys("MacBook")
        search_field.send_keys(Keys.ENTER)

        # Finding "Add To Cart" button for each search result
        search_results = self.driver.find_elements_by_xpath('.//div[@class="button-group"]')

        # Adding each item to cart and verifying number of items in cart
        num = 1
        for item in search_results:
            item.click()
            time.sleep(5) # sleeping since button needs to load first
            # Find "Cart button"
            cart_button = self.driver.find_element_by_xpath('.//span[@id="cart-total"]')
            expected_text = str(num) + ' item(s)'
            self.assertIn(expected_text, cart_button.text)
            num = num+1
