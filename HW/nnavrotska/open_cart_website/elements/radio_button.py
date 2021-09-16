from HW.nnavrotska.open_cart_website.elements.base import BaseElement


class RadioButton(BaseElement):
    def get_text(self):
        return self.element.text