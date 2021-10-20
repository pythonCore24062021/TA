
from HW.ArturZ.open_cart_homework.elements.base_elements import BaseElements
from HW.ArturZ.open_cart_homework.locators.home_page_locators import HomePageLocators
from HW.ArturZ.open_cart_homework.pages.login_page import Login
from HW.ArturZ.open_cart_homework.pages.register_page import RegisterPage


class Dropdown(BaseElements):
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
        return RegisterPage(self.driver)

