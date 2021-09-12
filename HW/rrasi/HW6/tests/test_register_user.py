import time
import unittest

from selenium import webdriver

from pages.home import Home
from pages.register import Register


class RegisterPage(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")
        time.sleep(1)
        self.home = Home(self.driver)

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
        register_page = self.home \
            .get_my_account() \
            .click() \
            .clickRegister() \
            .set_firstname("Popandopalo") \
            .set_lastname("Test") \
            .set_email("testEmail@gmail.com") \
            .set_telephone("5555") \
            .set_address("street") \
            .set_city("Lviv") \
            .set_postcode("79000") \
            .set_country("testEmail") \
            .click() \
            .set_region("testPasword") \
            .click() \
            .set_password("789456") \
            .set_passwordconfirm("789456") \
            .set_privacycheckmark() \
 \
            .click_continue()

        self.assertEqual(register_page.get_successmessage().get_message(), 'Your Account Has Been Created!')
