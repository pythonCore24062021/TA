import time
import unittest

from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):
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

    def test_first_reg_user(self):
        search_input = self.driver.find_element_by_css_selector("#search > input")
        search_input.send_keys("mac")
        search_btn = self.driver.find_element_by_css_selector("#search > span > button > i")
        search_btn.click()
        products = self.driver.find_elements_by_class_name("product-thumb")

        self.assertEqual(len(products), 4)
        names = []
        for product in products:
            names.append(product.find_element_by_xpath('.//div[2]/div[1]/h4/a').text)
        self.assertListEqual(names, ['iMac', 'MacBook', 'MacBook Air', 'MacBook Pro'])
        self.assertListEqual(names, ['iMac', 'MacBook', 'MacBook Air', 'MacBook Pro'])





