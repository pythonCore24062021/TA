import time

from HW.nnavrotska.open_cart_website.elements.alert import AlertDiv
from HW.nnavrotska.open_cart_website.elements.button import Button
from HW.nnavrotska.open_cart_website.elements.input import Input

from HW.nnavrotska.open_cart_website.locators.login_page_locators import LoginPageLocators
from HW.nnavrotska.open_cart_website.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.get_url(LoginPageLocators.LOGIN_URL)
        self.email_input = Input(driver, LoginPageLocators.EMAIL_INPUT)
        self.psw_input = Input(driver, LoginPageLocators.PSW_INPUT)
        self.login_btn = Button(driver, LoginPageLocators.LOGIN_BTN)

    def get_warning(self):
        self.warning = AlertDiv(self.driver, LoginPageLocators.ALERT_DIV)
        return self.warning

    def set_email(self, email):
        self.email_input.set_value(email)
        return self

    def set_psw(self, psw):
        self.psw_input.set_value(psw)
        return self

    def click_login(self):
        self.login_btn.click()
        time.sleep(2)
        return self