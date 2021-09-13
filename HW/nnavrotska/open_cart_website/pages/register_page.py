from elements.dropdown import DropdownMyAccount
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

