<<<<<<< HEAD
#from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#browser = webdriver.Chrome()
#browser.get("https://google.com/")
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

    def test_add_items_to_cart(self):
        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("Xiaomi Mi 8")
        search_input.send_keys(Keys.RETURN)
        add_to_cart = self.driver.find_element_by_xpath('(//*[contains(text(), "Add to Cart")])[1]')
        add_to_cart.click()
        select_option = EC.element_to_be_clickable((By.XPATH, '//select[@id="input-option224"]/option[@value="14"]'))
        select_option.click()
        add_option = self.driver.find_element_by_id("button-cart")
        add_option.click()
        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("MacBook")
        search_input.send_keys(Keys.RETURN)
        add_second_item = self.driver.find_element_by_css_selector(
            "#content > div:nth-child(8) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(1)")
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
=======
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:\Users\rrasi\PycharmProjects\TA\Driver\chromedriver.exe')
browser.get("https://google.com/")
>>>>>>> e4d8579 (veb)
