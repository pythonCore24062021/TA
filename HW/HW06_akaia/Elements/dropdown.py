from Elements.base import BaseElement
from Locators.home_page_locators import HomePageLocators
from Locators.register_page_locators import RegisterPageLocators
from pages.login_page import LoginPage
from pages.register import RegisterPage
from selenium.webdriver.common.keys import Keys


class Dropdown(BaseElement):
    def click(self):
        self.element.click()
        return self


class DropdownMyAccount(Dropdown):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)
        self.my_account = driver.find_element(*HomePageLocators.MY_ACCOUNT_DROPDOWN)
        self.login = None
        self.register = None

    def open_dropdown(self):
        self.my_account.click()
        return self

    def click_login(self):
        self.login = self.driver.find_element(*HomePageLocators.LOGIN_LINK)
        self.login.click()
        return LoginPage(self.driver)

    def click_register(self):
        self.register = self.driver.find_element(*HomePageLocators.REGISTER_LINK)
        self.register.click()
        return RegisterPage(self.driver)


class DropdownRegionState(Dropdown):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)
        self.region_state = driver.find_element(*RegisterPageLocators.DROPDOWN_REGION_STATE)

    def select_first_value(self):
        self.region_state.click()
        self.region_state.send_keys(Keys.DOWN)
        self.region_state.send_keys(Keys.ENTER)
        return self
