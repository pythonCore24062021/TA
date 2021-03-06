from HW.ArturZ.open_cart_homework.elements.dropdowns import DropdownMyAccount
from HW.ArturZ.open_cart_homework.locators.home_page_locators import HomePageLocators
from HW.ArturZ.open_cart_homework.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.account_dropdown = DropdownMyAccount(self.driver, HomePageLocators.MY_ACCOUNT_DROPDOWN)

    def click_my_account(self):
        self.account_dropdown.click()

    def get_my_account(self):
        return self.account_dropdown
