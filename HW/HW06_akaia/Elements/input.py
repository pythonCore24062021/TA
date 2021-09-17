from Elements.base import BaseElement
from selenium.webdriver.common.keys import Keys


class Input(BaseElement):
    def set_value(self, value):
        self.element.send_keys(value)

    def get_value(self):
        return self.element.text()

    def press_enter(self):
        self.element.send_keys(Keys.ENTER)
