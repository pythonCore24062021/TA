from HW.nnavrotska.open_cart_website.elements.base import BaseElement


class Input(BaseElement):
    def click(self):
        self.element.click()

    def set_value(self, text):
        self.element.click()
        self.element.send_keys(text)


