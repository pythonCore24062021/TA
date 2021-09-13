from elements.base import BaseElement
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePageLocators
from pages.login_page import LoginPage




class Dropdown(BaseElement):
    def click(self):
        self.element.click()


class DropdownMyAccount(Dropdown):
    def __init__(self):
        super().__init__(driver, locators)
        self.register = driver.find_element(*HomePageLocators.REGISTER_LINK)
        self.login = self.driver.find_element(*HomePageLocators.LOGIN_LINK)

    def click(self):
        self.element.click()
        return self

    def clickLogin(self):
        self.login.click()
        return LoginPage(self.driver)

    def clickRegister(self):
        self.register.click()