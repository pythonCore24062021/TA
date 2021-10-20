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



    def test_first_reg_user(self):
        my_acount_btm = self.driver.find_element_by_css_selector(
            "#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md"
        )
        my_acount_btm.click()
        reg_btn = self.driver.find_element_by_css_selector(
            "#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a")
        reg_btn.click()
        first_name_input = self.driver.find_element_by_css_selector("#input-firstname")
        first_name_input.send_keys("lhalam")
        email_input = self.driver.find_element_by_css_selector("#input-email")
        email_input.send_keys("lhalam@l")

        continue_btn = self.driver.find_element_by_css_selector("#content > form > div > div > input.btn.btn-primary")
        continue_btn.click()

        last_name_error_lb = self.driver.find_element_by_css_selector("#account > div:nth-child(4) > div > div")
        self.assertEqual(last_name_error_lb.text,
        "Last Name must be between 1 and 32 characters!")
        try:

            first_name_error_lb = self.driver.find_element_by_css_selector("#account > div:nth-child(3) > div > div")
        except:
            first_name_error_lb = None
        self.assertIsNone(first_name_error_lb)
