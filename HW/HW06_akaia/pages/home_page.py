from pages.base_page import BasePage
from elements.dropdown import DropdownMyAccount
from locators.home_page_locators import HomePageLocators
from elements.button import Button
from pages.register import RegisterPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.my_account_dropdown = DropdownMyAccount(self.driver, HomePageLocators.MY_ACCOUNT_DROPDOWN)
        # self.register = Button(self.driver, HomePageLocators.REGISTER_LINK)

    # def click_my_account_dropdown(self):
    #     self.my_account_dropdown.click()
    #     return self
    #
    # def click_register(self):
    #     self.register.click()
    #     return RegisterPage(self.driver)

    def get_my_account(self):
        return self.my_account_dropdown
