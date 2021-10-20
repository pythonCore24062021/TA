from Elements.base import BaseElement


class CheckBox(BaseElement):

    def check(self):
        self.element.click()