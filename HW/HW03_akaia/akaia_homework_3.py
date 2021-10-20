"""
HW03
Please, write integration tests by Selenium WebDriver to verify some features of Open Cart Application.
Use only CSS selectors to search of all web elements on site.
Please develop next methods in the `SearchTest` class

- loginByCssSelector method - to check the functionality of login;
- findByCss method - to check the functionality of a simple search;
"""

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SearchTest(unittest.TestCase):
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

    def testRegisterByCssSelector(self):
        """This test was created to verify Register functionality"""

        # 1. Reach 'Register' page
        my_account_button = self.driver.find_element_by_css_selector('a[title="My Account"]')
        my_account_button.click()
        register_button = self.driver.find_element_by_css_selector('a[href="http://taqc-opencart.epizy.com/index.php'
                                                                   '?route=account/register"]')
        register_button.click()
        self.assertIn('account/register', self.driver.current_url)

        # 2. Define mandatory fields
        first_name = self.driver.find_element_by_css_selector("#input-firstname")
        last_name = self.driver.find_element_by_css_selector("#input-lastname")
        email_field = self.driver.find_element_by_css_selector("#input-email")
        phone = self.driver.find_element_by_css_selector("#input-telephone")
        address_one = self.driver.find_element_by_css_selector("#input-address-1")
        city = self.driver.find_element_by_css_selector("#input-city")
        post_code = self.driver.find_element_by_css_selector("#input-postcode")
        region_state = self.driver.find_element_by_css_selector("#input-zone")
        password_field = self.driver.find_element_by_css_selector("#input-password")
        password_confirm = self.driver.find_element_by_css_selector("#input-confirm")
        privacy_checkbox = self.driver.find_element_by_css_selector('input[name="agree"]')
        continue_button = self.driver.find_element_by_css_selector('input[value="Continue"]')

        # 3. Enter data
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

        # 4. Assert that user was redirected to account/success page
        self.assertIn('account/success', self.driver.current_url)

    def testLoginByCssSelector(self):
        """
        This test verifies functionality of login
        """

        # 1. Create new user
        my_account_button = self.driver.find_element_by_css_selector('a[title="My Account"]')
        my_account_button.click()
        register_button = self.driver.find_element_by_css_selector('a[href="http://taqc-opencart.epizy.com/index.php'
                                                                   '?route=account/register"]')
        register_button.click()
        self.assertIn('account/register', self.driver.current_url)
        first_name = self.driver.find_element_by_css_selector("#input-firstname")
        last_name = self.driver.find_element_by_css_selector("#input-lastname")
        email_field = self.driver.find_element_by_css_selector("#input-email")
        phone = self.driver.find_element_by_css_selector("#input-telephone")
        address_one = self.driver.find_element_by_css_selector("#input-address-1")
        city = self.driver.find_element_by_css_selector("#input-city")
        post_code = self.driver.find_element_by_css_selector("#input-postcode")
        region_state = self.driver.find_element_by_css_selector("#input-zone")
        password_field = self.driver.find_element_by_css_selector("#input-password")
        password_confirm = self.driver.find_element_by_css_selector("#input-confirm")
        privacy_checkbox = self.driver.find_element_by_css_selector('input[name="agree"]')
        continue_button = self.driver.find_element_by_css_selector('input[value="Continue"]')
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
        my_account_button = self.driver.find_element_by_css_selector('a[title="My Account"]')
        my_account_button.click()
        logout_button = self.driver.find_element_by_css_selector("#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a")
        logout_button.click()
        self.assertIn('account/logout', self.driver.current_url)

        # 3. Login with user credentials from step 1
        my_account_button = self.driver.find_element_by_css_selector('a[title="My Account"]')
        my_account_button.click()
        login_button = self.driver.find_element_by_css_selector("#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a")
        login_button.click()
        email_textbox = self.driver.find_element_by_css_selector("#input-email")
        password_textbox = self.driver.find_element_by_css_selector("#input-password")
        submit_button = self.driver.find_element_by_css_selector("input[type=Submit]")
        email_textbox.send_keys(email)
        password_textbox.send_keys(password)
        submit_button.click()
        # Verify that user was created
        self.assertIn('account/account', self.driver.current_url)

    def testFindByCss(self):
        """
        check the functionality of a simple search. Find all elements by css
        """

        # 1. Enter data in search field and executing search
        search_field = self.driver.find_element_by_css_selector("input[name='search']")
        search_field.send_keys("mac")
        search_field.send_keys(Keys.ENTER)

        # 2. Find web elements with search result names listed
        search_results = self.driver.find_elements_by_css_selector('div[class="caption"] > h4')

        # 3. Define Expected Result
        expected_results = ['iMac', 'MacBook', 'MacBook Air', 'MacBook Pro']

        # 4. Define Actual Result
        actual_results = []
        for result in search_results:
            actual_results.append(result.text)

        # 5. Comparing expected and actual
        self.assertListEqual(expected_results, actual_results)
