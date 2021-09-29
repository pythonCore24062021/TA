from HW.nnavrotska.open_cart_website.elements.button import Button
from HW.nnavrotska.open_cart_website.elements.label import Label
from HW.nnavrotska.open_cart_website.locators.home_page_locators import HomePageLocators
from HW.nnavrotska.open_cart_website.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_currency_symbol(self):
        currency_symbol = Label(self.driver, HomePageLocators.CURRENCY_SYMBOL)
        return currency_symbol.get_text()

    def get_cart_btn(self):
        cart_btn = Button(self.driver, HomePageLocators.CART_BTN)
        return cart_btn.get_text()

    def get_product_price(self):
        product_price = Label(self.driver, HomePageLocators.PRODUCT_PRICE)
        return product_price.get_text()

    def get_tax_price(self):
        tax_price = Label(self.driver, HomePageLocators.TAX_PRICE)
        return tax_price.get_text()

    # def check_all_price_class_name(self):
    #     price_class_name = Label(self.driver, *HomePageLocators.PRICE_CLASS_NAME)
    #     return price_class_name.get_text()
    #
    # def check_all_price_new_class_name(self):
    #     price_new_class_name = Label(self.driver, *HomePageLocators.PRICE_NEW_CLASS_NAME)
    #     return price_new_class_name.get_text()
    #
    # def check_all_price_old_class_name(self):
    #     price_old_class_name = Label(self.driver, *HomePageLocators.PRICE_OLD_CLASS_NAME)
    #     return price_old_class_name.get_text()
    #
    # def check_all_price_tax_class_name(self):
    #     price_tax_class_name = Label(self.driver, *HomePageLocators.PRICE_TAX_CLASS_NAME)
    #     return price_tax_class_name.get_text()
