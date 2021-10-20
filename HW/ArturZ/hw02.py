from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time

from selenium.webdriver.support.wait import WebDriverWait


class FirstSeleniumTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://taqc-opencart.epizy.com/")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.maximize_window()
    #
    # @classmethod
    # def tearDownClass(cls):
    #    cls.driver.quit()

    #def check_currency_change(self):
    #    check_currency = self.driver.find_element_by_css_selector("#cart-total")
    #    return check_currency.text


    def test_check_currency_is_dollar(self):
        currency_dropdown = self.driver.find_element_by_css_selector("#form-currency > div > button")
        currency_dropdown.click()
        select_dollar = self.driver.find_element_by_css_selector("#form-currency > div > ul > li:nth-child(3) > button")
        select_dollar.click()
        check_currency_change = self.driver.find_element_by_css_selector("#cart-total")
        self.assertEqual(check_currency_change.text, "0 item(s) - $0.00")

    def test_check_currency_is_euro(self):
        currency_dropdown = self.driver.find_element_by_css_selector("#form-currency > div > button")
        currency_dropdown.click()
        select_euro_currency = self.driver.find_element_by_css_selector("#form-currency > div > ul > li:nth-child(1) > button")
        select_euro_currency.click()
        check_currency_change = self.driver.find_element_by_css_selector("#cart-total")
        self.assertEqual(check_currency_change.text, "0 item(s) - 0.00€")

    def test_check_currency_is_pound(self):
        currency_dropdown = self.driver.find_element_by_css_selector("#form-currency > div > button")
        currency_dropdown.click()
        select_euro_currency = self.driver.find_element_by_css_selector("#form-currency > div > ul > li:nth-child(2) > button")
        select_euro_currency.click()
        check_currency_change = self.driver.find_element_by_css_selector("#cart-total")
        self.assertEqual(check_currency_change.text, "0 item(s) - £0.00")

    def test_mac_search(self):
        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("Mac")
    #    search_input.send_keys(Keys.RETURN)
        click_search = self.driver.find_element_by_xpath('//span[@class="input-group-btn"]')
        click_search.click()
        check_mac_search = self.driver.find_elements_by_css_selector("h4 > a")

        check_mac_results = list()
        for item in check_mac_search:
            check_mac_results.append(item.text)

        time.sleep(5)

        expected_results = ["iMac", "MacBook", "MacBook Air", "MacBook Pro"]
        self.assertTrue(set(check_mac_results) & set(expected_results))


    def test_add_items_to_cart(self):
        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("Xiaomi Mi 8")
        search_input.send_keys(Keys.RETURN)
        add_to_cart = self.driver.find_element_by_xpath('(//*[contains(text(), "Add to Cart")])[1]')
        add_to_cart.click()

        select_option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//select[@id="input-option224"]/option[@value="14"]'))
        )
        select_option.click()
        add_option = self.driver.find_element_by_id("button-cart")
        add_option.click()

        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("MacBook")
        search_input.send_keys(Keys.RETURN)
        add_second_item = self.driver.find_element_by_css_selector("#content > div:nth-child(8) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(1)")
        add_second_item.click()

        time.sleep(1)
        # Was added due bad internet connection.

        open_cart = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@id="cart"]'))
        )

        open_cart.click()

        check_add_to_cart = self.driver.find_elements_by_css_selector("td.text-left > a")

        check_cart_items = list()
        for cart_item in check_add_to_cart:
            check_cart_items.append(cart_item.text)


        expected_results = ["Xiaomi Mi 8", "MacBook"]


        self.assertTrue(set(check_cart_items) & set(expected_results))



