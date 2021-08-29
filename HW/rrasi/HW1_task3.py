#Please, write integration tests by Selenium WebDriver to verify some features of Open Cart Application.
#Please develop next methods in the FirstSeleniumTest class

#checkAddToCart method - to check the functionality of adding items 'Xiaomi Mi 8' and 'MacBook' to cart.

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
        option_btn = self.driver.find_element_by_css_selector('#input-option224')
        option_btn.click()
        select_size = find_element_by_css_selector('#input-option224 > option:nth-child(2)')
        select_size.click()
        add_product_btn = find_element_by_css_selector('# button-cart')
        add_product_btn.click()

        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("MacBook")
        search_button = self.driver.find_element_by_css_selector('#search > span > button > i')
        search_button.click()
        add_second_item_button = self.driver.find_element_by_css_selector(' # content > div:nth-child(8) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(1) > span')
        add_second_item_button.click()
        open_cart = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@id="cart"]'))
        )
        open_cart.click()
        check_add_to_cart = self.driver.find_elements_by_css_selector("td.text-left > a")#top-links > ul > li:nth-child(4) > a
        check_cart_items = list()
        for cart_item in check_add_to_cart:
            check_cart_items.append(cart_item.text)

        expected_results = ["Xiaomi Mi 8", "MacBook"]

        self.assertTrue(set(check_cart_items) & set(expected_results))






