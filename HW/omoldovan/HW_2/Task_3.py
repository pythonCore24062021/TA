import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class FirstSeleniumTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")
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

    def test_check_add_to_cart_xiaomi(self):
        search_xiaomi = self.driver.find_element_by_css_selector("#search > input")
        search_xiaomi.send_keys('Xiaomi Mi 8')
        search_btn = self.driver.find_element_by_css_selector('#search > span > button')
        search_btn.click()
        xiaomi_mi_8 = self.driver.find_element_by_css_selector('#content > div:nth-child(8)')
        self.assertIn('Xiaomi Mi 8', xiaomi_mi_8.text)
        add_to_cart_button = self.driver.find_element_by_css_selector('#content > div:nth-child(8) >'
                                                                      ' div:nth-child(1) > div > div:nth-child(2) >'
                                                                      ' div.button-group > button:nth-child(1)')
        add_to_cart_button.click()
        time.sleep(5)
        size_select = self.driver.find_element_by_css_selector('#input-option224')
        size_select.click()
        time.sleep(3)
        size_select2 = self.driver.find_element_by_css_selector('#input-option224 > option:nth-child(2)')
        size_select2.click()
        add_to_cart_button_2 = self.driver.find_element_by_css_selector('#button-cart')
        add_to_cart_button_2.click()
        cart = self.driver.find_element_by_css_selector('#cart > button')
        cart.click()
        time.sleep(5)
        added_amount = self.driver.find_elements_by_class_name('dropdown-menu pull-right')
        time.sleep(5)
        expected_result_xiaomi = ['1', 'Xiaomi Mi 8']
        self.assertIn(added_amount, expected_result_xiaomi)

    def test_check_add_to_cart_Mac(self):
        search_mac = self.driver.find_element_by_css_selector("#search > input")
        search_mac.send_keys('MacBook')
        search_btn = self.driver.find_element_by_css_selector('#search > span > button')
        search_btn.click()
        mac = self.driver.find_element_by_css_selector('#content > div:nth-child(8) > div > div')
        self.assertEqual(mac.text, 'MacBook')
        add_to_cart_button = self.driver.find_element_by_css_selector('#content > div:nth-child(8) >'
                                                                      ' div:nth-child(1) > div > div:nth-child(2) >'
                                                                      ' div.button-group > button:nth-child(1)')
        add_to_cart_button.click()
        time.sleep(5)
        add_to_cart_button_2 = self.driver.find_element_by_css_selector('#button-cart')
        add_to_cart_button_2.click()
        cart = self.driver.find_element_by_css_selector('#cart > button')
        cart.click()
        time.sleep(5)
        added_amount = self.driver.find_elements_by_class_name('dropdown-menu pull-right')
        time.sleep(5)
        expected_result_mac = ['1', 'Xiaomi Mi 8', '1', 'MacBook']
        self.assertIn(added_amount, expected_result_mac)