import time

from HW.ArturZ.open_cart_homework.elements.alert import AlertDiv
from HW.ArturZ.open_cart_homework.elements.buttons import Button
from HW.ArturZ.open_cart_homework.elements.input import Input
from HW.ArturZ.open_cart_homework.locators.login_page_locators import LoginPageLocators
from HW.ArturZ.open_cart_homework.pages.base_page import BasePage


class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = Input(driver, LoginPageLocators.INPUT_EMAIL)
        self.password_input = Input(driver, LoginPageLocators.INPUT_PASSWORD)
        self.login_btn = Button(driver, LoginPageLocators.LOGIN_BTN)

    def get_warning(self):
        self.warning = AlertDiv(self.driver, LoginPageLocators.ALERT_DIV)
        return self.warning


    def set_email(self, email):
        self.email_input.set_value(email)
        return self

    def set_password(self, password):
        self.password_input.set_value(password)
        return self


    def click_login(self):
        self.login_btn.click()
        time.sleep(2)
        try:
            self.get_warning()
            return self
        except:
            pass
