from HW.nnavrotska.open_cart_website.elements.base import BaseElement


class Button(BaseElement):
    def click(self):
        self.element.click()

    def get_text(self):
        return self.element.text