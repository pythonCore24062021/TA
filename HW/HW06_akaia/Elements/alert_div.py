from Elements.base import BaseElement


class AlertDiv(BaseElement):
    def get_message(self):
        return self.element.text
