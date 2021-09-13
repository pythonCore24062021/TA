import time
import unittest

from selenium import webdriver


from HW.rrasi.HW6.Register.pages.home import Home
#from HW.rrasi.HW6.Register.pages.register_page import RegisterUser
#from HW.rrasi.HW6.Register.locators.register_page_locators import RegisterPageLocators



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
            .set_firstname("Popandopalo2") \
            .set_lastname("Test2") \
            .set_email("rul@gmail.com") \
            .set_telephone("55555") \
            .set_address("street") \
            .set_city("Lviv") \
            .set_postcode("79000") \
            .set_country() \
            .click() \
            .set_region() \
            .click() \
            .set_password("789456") \
            .set_passwordconfirm("789456") \
            .set_privacycheckmark() \
 \
            .click_continue()

        self.assertEqual(register_page.get_successmessage().get_message(), 'Your Account Has Been Created!')
