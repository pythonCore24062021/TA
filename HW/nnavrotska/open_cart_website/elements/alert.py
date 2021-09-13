from elements.base import BaseElement


class AlertDiv(BaseElement):
    def get_text(self):
        return self.element.text