from HW.rrasi.HW6.Register.elements.base import BaseElement



class Input(BaseElement):
    def click(self):
        self.element.click()

    def set_value(self, text):
        self.element.clear()
        self.element.send_keys(text)

