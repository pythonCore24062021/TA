from HW.ArturZ.open_cart_homework.elements.base_elements import BaseElements


class Input(BaseElements):
    def click(self):
        self.element.click()

    def set_value(self, text):
        self.element.clear()
        self.element.send_keys(text)

