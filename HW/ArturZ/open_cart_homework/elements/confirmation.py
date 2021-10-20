from HW.ArturZ.open_cart_homework.elements.base_elements import BaseElements


class ConfirmationDiv(BaseElements):
    def get_success(self):
        return self.element.text