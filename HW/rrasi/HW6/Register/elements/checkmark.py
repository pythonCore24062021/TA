from elements.base import BaseElement
from locators.home_page_locators import HomePageLocators
from pages.register import Register
from locators.register_page_locators import RegisterPageLocators



class PrivacyCheckmark(Register):

    def __init__(self, driver, locators):
        super().__init__(driver, locators)
        self.checkbox = driver.find_element(*RegisterPageLocators.PRIVACYPOLICYCHECKMARK)

    def click(self):
        self.element.click()
        return self


