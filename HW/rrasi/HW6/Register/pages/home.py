from elements.dropdown import Dropdown, DropdownMyAccount
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class Home(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.account_dropdown = DropdownMyAccount(self.driver, HomePageLocators.MY_ACCOUNT_DROPDOWN)

    def click_my_account(self):
        self.account_dropdown.click()

    def get_my_account(self):
        return self.account_dropdown

    def click_register(self):
        self.
