from HW.ArturZ.open_cart_homework.elements.base_elements import BaseElements


class AlertDiv(BaseElements):
    def get_message(self):
        return self.element.text