
from selenium import webdriver
import unittest
import time


class SearchTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://taqc-opencart.epizy.com/")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


    def test_registration_user(self):
        my_account = self.driver.find_element_by_css_selector("#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md")
        my_account.click()
        registration = self.driver.find_element_by_css_selector("#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a")
        registration.click()
        first_name = self.driver.find_element_by_css_selector("#input-firstname")
        first_name.send_keys("name")
        second_name = self.driver.find_element_by_css_selector("#input-lastname")
        second_name.send_keys("last name")
        email = self.driver.find_element_by_css_selector("#input-email")
        email.send_keys("test4321@test.com")
        phone = self.driver.find_element_by_css_selector("#input-telephone")
        phone.send_keys("9379992")
        address = self.driver.find_element_by_css_selector("#input-address-1")
        address.send_keys("some street 42")
        city = self.driver.find_element_by_css_selector("#input-city")
        city.send_keys("Kharkiv")
        post_code = self.driver.find_element_by_css_selector("#input-postcode")
        post_code.send_keys("54321")
        select_address = self.driver.find_element_by_css_selector("#input-country > option:nth-child(237)")
        select_address.click()

        time.sleep(2)
        select_area = self.driver.find_element_by_css_selector("#input-zone > option:nth-child(2)")
        select_area.click()

        pass_field = self.driver.find_element_by_css_selector("#input-password")
        pass_field.send_keys("test")
        repeat_pass = self.driver.find_element_by_css_selector("#input-confirm")
        repeat_pass.send_keys("test")

        privacy_check = self.driver.find_element_by_css_selector("#content > form > div > div > input[type=checkbox]:nth-child(2)")
        privacy_check.click()

        confirm_reg = self.driver.find_element_by_css_selector("#content > form > div > div > input.btn.btn-primary")
        confirm_reg.click()


        success_continue = self.driver.find_element_by_css_selector("#content > div > div > a")
        success_continue.click()

        user_logged = self.driver.find_element_by_css_selector("body > div:nth-child(4) > ul > li:nth-child(2) > a")
        user_account = user_logged.text

        self.assertEqual(user_account, "Account")

        my_account = self.driver.find_element_by_css_selector("#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md")
        my_account.click()
        logout = self.driver.find_element_by_css_selector("#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a")
        logout.click()

    def test_login_user(self):
        my_account = self.driver.find_element_by_css_selector("#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md")
        my_account.click()
        login = self.driver.find_element_by_css_selector("#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a")
        login.click()
        email_field = self.driver.find_element_by_css_selector("#input-email")
        email_field.send_keys("test321@test.com")
        pass_field = self.driver.find_element_by_css_selector("#input-password")
        pass_field.send_keys("test")
        login_btn = self.driver.find_element_by_css_selector("#content > div > div:nth-child(2) > div > form > input")
        login_btn.click()

        user_logged = self.driver.find_element_by_css_selector("body > div:nth-child(4) > ul > li:nth-child(2) > a")
        user_account = user_logged.text

        self.assertEqual(user_account, "Account")


    def test_search_css(self):
        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("Mac")
        click_search = self.driver.find_element_by_css_selector("#search > span > button")
        click_search.click()
        check_css_search = self.driver.find_elements_by_css_selector("h4 > a")

        check_css_results = []
        for item in check_css_search:
            check_css_results.append(item.text)

        time.sleep(5)

        expected_results = ["iMac", "MacBook", "MacBook Air", "MacBook Pro"]
        self.assertListEqual(check_css_results, expected_results)

