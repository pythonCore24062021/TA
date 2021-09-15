from HW.nnavrotska.open_cart_website.elements.base import BaseElement


class Dropdown(BaseElement):
    def click(self):
        self.element.click()

    def select_by_value(self, value):
        self.driver.find_element_by_xpath(f""".//option[text()='{value}']""").click()
