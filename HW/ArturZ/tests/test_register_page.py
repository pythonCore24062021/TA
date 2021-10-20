
import unittest

from selenium import webdriver

from HW.ArturZ.open_cart_homework.pages.home_page import HomePage
import time


class RegisterTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")
        time.sleep(1)
        self.home = HomePage(self.driver)

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_register_user(self):
        register_page = self.home \
            .get_my_account() \
            .click() \
            .clickRegister() \
            .set_first_name("Test") \
            .set_lastname("User") \
            .set_email("test@example.com") \
            .set_phone("9379992") \
            .set_address("Somewhere") \
            .set_city("Kharkiv") \
            .set_password("test123") \
            .set_confirm_password("test123") \
            .set_country() \
            .set_region() \



    #    self.assertEqual(tbd)

