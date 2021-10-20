import time
from unittest import TestCase

from selenium.webdriver.chrome import webdriver

from pages.home_page import HomePage


class TestRegisterPage(TestCase):
    driver = None

    def setUp(self):
        self.home_page = HomePage(self.driver)
        self.home_page.get_url()

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_page(self):
        login_page = self.home_page \
            .click_my_account() \
            .click_register()

        self.assertEqual(REGISTER_ACCOUNT_HEADER, 'Register Account')

# RegisterPage class - to representation sign up page;
# RegisterTest class - to check the functionality of sign up;
