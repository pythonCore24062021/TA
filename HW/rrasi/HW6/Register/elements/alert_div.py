from HW.rrasi.HW6.Register.elements.base import BaseElement


class AlertDiv(BaseElement):
    def get_message(self):
        return self.element.text