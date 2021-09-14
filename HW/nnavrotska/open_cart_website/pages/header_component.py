from elements.dropdown import Dropdown
from locators.home_page_locators import HomePageLocators, HomePageLocatorsRegisteredUser
from pages.login_page import LoginPage


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
        return LoginPage(self.driver)

    def clickRegister(self):
        self.register.click()


class DropdownMyAccountRegisteredUser(Dropdown):
    def __init__(self, driver, locators):
        super().__init__(driver, locators)
        self.my_account = driver.find_element(*HomePageLocatorsRegisteredUser.MY_ACCOUNT)
        self.order_history = self.driver.find_element(*HomePageLocatorsRegisteredUser.ORDER_HISTORY)
        self.transactions = self.driver.find_element(*HomePageLocatorsRegisteredUser.TRANSACTIONS)
        self.downloads = self.driver.find_element(*HomePageLocatorsRegisteredUser.DOWNLOADS)
        self.logout = self.driver.find_element(*HomePageLocatorsRegisteredUser.LOGOUT)


class HeaderComponent:

    def __init__(self, driver):
        self.driver = driver
        self.account_dropdown = DropdownMyAccount(self.driver, HomePageLocators.MY_ACCOUNT_DROPDOWN)
