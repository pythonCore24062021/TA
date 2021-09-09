from elements.base import BaseElement
from locators.home_page_locators import HomePageLocators
from pages.register import Register
from locators.register_page_locators import RegisterPageLocators


class Region(Register):
    def click(self):
        self.element.click()


class RegionDropdown(Region):

    def __init__(self, driver, locators):
        super().__init__(driver, locators)
        self.register = driver.find_element(*RegisterPageLocators.REGION)

    def click(self):
        self.element.click()
        return self

    def __init__(self, driver, locators):
        super().__init__(driver, locators)
        self.registeroption = driver.find_element(*RegisterPageLocators.REGIONOPTIONпше)

    def click(self):
        self.element.click()
        return self


    def clickRegister(self):
        self.register.click()
