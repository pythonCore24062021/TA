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


    def test_checkMacSearch(self): # test to be changed, but remains in SearchTest class
        search_field = self.driver.find_element_by_css_selector('#search > input')
        search_field.send_keys("mac")
        search_btn = self.driver.find_element_by_css_selector('#search > span > button > i')
        search_btn.click()
        products = self.driver.find_elements_by_class_name('product-thumb')
        names = []
        for product in products:
            names.append(product.find_element_by_xpath('.//div[2]/div[1]/h4/a').text)

        self.assertEqual(len(products), 4)
        self.assertListEqual(names, ['iMac', 'MacBook', 'MacBook Air', 'MacBook Pro'])
        for name in names:
            self.assertIn('mac', name.lower())

    def test_findByCss_iphone(self):  # test to be changed, but remains in SearchTest class
        search_field = self.driver.find_element_by_css_selector('#search > input')
        search_field.send_keys("iphone")
        search_btn = self.driver.find_element_by_css_selector('#search > span > button > i')
        search_btn.click()
        time.sleep(1)
        products = self.driver.find_elements_by_css_selector('#content > div:nth-child(8) > div')
        for product in products:
            self.assertIn('iphone', product.text.lower())

    # to check the functionality of a simple search;
    def test_findByXPath(self):
        pass

    # checkAjaxIframePage method - to check the functionality to search "Order Date" of selected "Store State" in the table.