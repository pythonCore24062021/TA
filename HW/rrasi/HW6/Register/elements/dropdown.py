
from HW.rrasi.HW6.Register.elements.base import BaseElement
from HW.rrasi.HW6.Register.pages.login import Login
from HW.rrasi.HW6.Register.locators.home_page_locators import HomePageLocators
from HW.rrasi.HW6.Register.locators.register_page_locators import RegisterPageLocators
#from HW.rrasi.HW6.Register.pages.register_page import RegisterUser
from selenium.webdriver.common.keys import Keys


class Dropdown(BaseElement):
    def click(self):
        self.element.click()


class DropdownMyAccount(Dropdown):

    def __init__(self, driver, locators):
        super().__init__(driver, locators)
        self.register = driver.find_element(*HomePageLocators.REGISTER_LINK)
        self.login = self.driver.find_element(*HomePageLocators.LOGIN_LINK)

    def click(self):
        self.element.click()
        return self

    def clickLogin(self):
        self.login.click()
        return Login(self.driver)

    def clickRegister(self):
        self.register.click()


class DropdownRegionState(Dropdown):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)
        self.region_state = driver.find_element(*RegisterPageLocators.DROPDOWN_REGION_STATE)

    def select_first_value(self):
        self.region_state.click()
        self.region_state.send_keys(Keys.DOWN)
        self.region_state.send_keys(Keys.ENTER)
        return self