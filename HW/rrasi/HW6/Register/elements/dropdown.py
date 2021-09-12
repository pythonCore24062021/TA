
from HW.rrasi.HW6.Register.elements.base import BaseElement
from HW.rrasi.HW6.Register.pages.login import Login
from HW.rrasi.HW6.Register.locators.home_page_locators import HomePageLocators


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
