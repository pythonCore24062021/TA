from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time

from selenium.webdriver.support.wait import WebDriverWait


class SearchXPathTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://taqc-opencart.epizy.com/")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_login_user_xpath(self):
        my_account = self.driver.find_element_by_xpath('//a[@title="My Account"]')
        my_account.click()
        login = self.driver.find_element_by_xpath('//a[contains (text(), "Login")]')
        login.click()
        email_field = self.driver.find_element_by_xpath('//input[@name="email"]')
        email_field.send_keys("test321@test.com")
        pass_field = self.driver.find_element_by_xpath('//input[@name="password"]')
        pass_field.send_keys("test")
        login_btn = self.driver.find_element_by_xpath('//input[@type="submit"]')
        login_btn.click()

        user_logged = self.driver.find_element_by_xpath('//h2[contains (text(), "My Account")]')
        user_account = user_logged.text

        self.assertEqual(user_account, "My Account")


    def test_search_xpath(self):
        search_input = self.driver.find_element_by_xpath('//input[@name="search"]')
        search_input.send_keys("Mac")
        click_search = self.driver.find_element_by_xpath('//div[@id="search"]//button[@type="button"]')
        click_search.click()

        time.sleep(2)
        products_xpath = self.driver.find_elements_by_xpath('//div[@class="product-thumb"]')

        self.assertEqual(len(products_xpath), 4)
        names = []
        for product_xpath in products_xpath:
            names.append(product_xpath.find_element_by_xpath('.//div[2]/div[1]/h4/a').text)

        time.sleep(5)


        expected_results = ["iMac", "MacBook", "MacBook Air", "MacBook Pro"]
        self.assertEqual(names, expected_results)



    def test_add_items_to_cart(self):
        search_input = self.driver.find_element_by_xpath('//input[@name="search"]')
        search_input.send_keys("Xiaomi Mi 8")
        click_search = self.driver.find_element_by_xpath('//div[@id="search"]//button[@type="button"]')
        click_search.click()

        add_to_cart = self.driver.find_element_by_xpath('(//*[contains(text(), "Add to Cart")])[1]')
        add_to_cart.click()

        select_option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//select[@id="input-option224"]/option[@value="14"]'))
        )
        select_option.click()
        add_option = self.driver.find_element_by_xpath('//button[@id="button-cart"]')
        add_option.click()

        search_input = self.driver.find_element_by_xpath('//input[@name="search"]')
        search_input.send_keys("MacBook")

        click_search = self.driver.find_element_by_xpath('//div[@id="search"]//button[@type="button"]')
        click_search.click()
        add_second_item = self.driver.find_element_by_xpath('(//span[contains (text(), "Add to Cart")])[1]')
        add_second_item.click()

        time.sleep(1)
        # Was added due bad internet connection.

        open_cart = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@id="cart"]'))
        )

        open_cart.click()

        check_add_to_cart = self.driver.find_elements_by_xpath('//td[@class="text-left"]')
        self.assertEqual(len(check_add_to_cart), 2)

        names = []
        for cart_item in check_add_to_cart:
            names.append(cart_item.find_element_by_xpath('./a').text)

        expected_results = ["Xiaomi Mi 8", "MacBook"]

        self.assertListEqual(names, expected_results)