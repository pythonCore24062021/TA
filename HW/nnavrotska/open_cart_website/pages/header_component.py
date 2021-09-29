from HW.nnavrotska.open_cart_website.elements.dropdown import Dropdown
from HW.nnavrotska.open_cart_website.locators.home_page_locators import HomePageLocators, HomePageLocatorsRegisteredUser


class DropdownMyAccount(Dropdown):

    def __init__(self, driver, locators):
        super().__init__(driver, locators)
        self.register = driver.find_element(*HomePageLocators.REGISTER_LINK)
        self.login = driver.find_element(*HomePageLocators.LOGIN_LINK)

    def click(self):
        self.element.click()
        return self

    def click_login(self):
        self.login.click()
        from HW.nnavrotska.open_cart_website.pages.login_page import LoginPage
        return LoginPage(self.driver)

    def click_register(self):
        self.register.click()


class DropdownMyAccountRegisteredUser(Dropdown):
    def __init__(self, driver, locators):
        super().__init__(driver, locators)
        self.my_account = self.driver.find_element(*HomePageLocatorsRegisteredUser.MY_ACCOUNT)
        self.order_history = self.driver.find_element(*HomePageLocatorsRegisteredUser.ORDER_HISTORY)
        self.transactions = self.driver.find_element(*HomePageLocatorsRegisteredUser.TRANSACTIONS)
        self.downloads = self.driver.find_element(*HomePageLocatorsRegisteredUser.DOWNLOADS)
        self.logout = self.driver.find_element(*HomePageLocatorsRegisteredUser.LOGOUT)


class HeaderComponent:
    def __init__(self, driver):
        self.driver = driver
        self.account_dropdown = DropdownMyAccount(self.driver, HomePageLocators.MY_ACCOUNT_DROPDOWN)
        self.currency_dropdown = DropdownCurrency(self.driver, HomePageLocators.CURRENCY_DROPDOWN)

class DropdownCurrency(Dropdown):
    def __init__(self, driver, locators):
        super().__init__(driver, locators)
        self.currency_dropdown = driver.find_element(*HomePageLocators.CURRENCY_DROPDOWN)

    def click(self):
        self.element.click()
        return self

    def select_euro(self):
        euro = self.driver.find_element(*HomePageLocators.EURO)
        return euro.click()

    def select_pound(self):
        pound = self.driver.find_element(*HomePageLocators.POUND)
        return pound.click()

    def select_dollar(self):
        dollar = self.driver.find_element(*HomePageLocators.DOLLAR)
        return dollar.click()