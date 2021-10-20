import time

from framework.web import element_factory
from framework.web.elements.element import Element
from framework.web.search import ID
from framework.web.search import xpath
from ui.pages.base_component import BaseComponent
import ui.pages.base_pages.header_component._locators as locators


class Header(BaseComponent):
    def __init__(self, wrapper: Element):
        super().__init__(wrapper)
        self.currency_button = self.wrapper.find_child_element(xpath(locators.CURRENCY_BTN_XPATH))

    def set_currency(self, currency):
        self.currency_button.click()

