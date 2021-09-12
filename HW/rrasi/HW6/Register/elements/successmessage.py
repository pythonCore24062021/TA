from elements.base import BaseElement
from locators.home_page_locators import HomePageLocators
from pages.register import Register
from locators.register_page_locators import RegisterPageLocators



class Message(Register):
    def get_message(self):
        return self.element.text