from pages.base_page import BasePage
from elements.input import Input
from elements.button import Button
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = Input(self.driver, LoginPageLocators.INPUT_EMAIL)
        self.password_input = Input(self.driver, LoginPageLocators.INPUT_PASSWORD)
        self.login_button = Button(self.driver, LoginPageLocators.BTN_LOGIN)

    # def open_my_account_dropdown(self):
    #     self

    def set_email(self, value):
        self.email_input.set_value(value)
        return self

    def set_password(self, value):
        self.password_input.set_value(value)
        return self

    def click_login_button(self):
        self.login_button.click()
        return self
