import time
from unittest import TestCase
from selenium import webdriver


class FirstSeleniumTest(TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # to check the functionality of adding items 'Xiaomi Mi 8' and 'MacBook' to cart.
    def test_checkAddToCart(self):  # test to be changed and moved to CartTest class
        search_field = self.driver.find_element_by_css_selector('#search > input')
        search_field.send_keys("Xiaomi Mi 8")
        search_btn = self.driver.find_element_by_css_selector('#search > span > button > i')
        search_btn.click()
        add_to_cart_btn = self.driver.find_element_by_css_selector(
            '#content > div:nth-child(8) > div > div > div:nth-child(2) > div.button-group > button:nth-child(1)')
        add_to_cart_btn.click()
        time.sleep(1)
        dropdown = self.driver.find_element_by_css_selector('#input-option224')
        dropdown.click()
        dropdown_option = self.driver.find_element_by_css_selector('#input-option224 > option:nth-child(2)')
        dropdown_option.click()
        blue_add_to_cart_btn = self.driver.find_element_by_css_selector('#button-cart')
        blue_add_to_cart_btn.click()
        time.sleep(1)
        search_field = self.driver.find_element_by_css_selector('#search > input')
        search_field.click()
        search_field.send_keys("MacBook")
        search_btn = self.driver.find_element_by_css_selector('#search > span > button > i')
        search_btn.click()
        time.sleep(1)
        add_to_cart_btn = self.driver.find_element_by_css_selector(
            '#content > div:nth-child(8) > div > div > div:nth-child(2) > div.button-group > button:nth-child(1)')
        add_to_cart_btn.click()
        time.sleep(1)
        cart_btn = self.driver.find_element_by_css_selector('#cart > button')
        cart_btn.click()
        time.sleep(1)
        items_in_cart = []
        items_in_cart.append(
            self.driver.find_element_by_xpath('.//ul / li[1] / table / tbody / tr[1] / td[2] / a').text)
        items_in_cart.append(
            self.driver.find_element_by_xpath('.//ul / li[1] / table / tbody / tr[2] / td[2] / a').text)
        self.assertListEqual(items_in_cart, ['Xiaomi Mi 8', 'MacBook'])
        view_cart_btn = self.driver.find_element_by_css_selector(
            '#cart > ul > li:nth-child(2) > div > p > a:nth-child(1)')
        view_cart_btn.click()
        time.sleep(1)
        items = []
        items.append(
            self.driver.find_element_by_xpath(
                '//*[@id="content"]/form/div/table/tbody/tr[1]/td[4]/div/input').get_attribute('value'))
        items.append(
            self.driver.find_element_by_xpath(
                '//*[@id="content"]/form/div/table/tbody/tr[2]/td[4]/div/input').get_attribute('value'))
        self.assertListEqual(items, ['1', '1'])

    # to check the functionality of adding items to cart;
    def test_addToCartByXPath(self):
        pass

    # to check the functionality of adding items to cart.
    def test_addQuantityInCartByXPath(self):
        pass

    # update checkAddToCart method - remove presentationSleep(2); and write explicit wait code to expect breadcrumb element or url updated;
    # checkAddAppleCinema30ToCart method - to check the functionality of a add Apple Cinema 30" item to cart;
