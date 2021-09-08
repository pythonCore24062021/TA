import time

from elements.button import Button
from elements.input import Input
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators


class Register(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.firstname_input = Input(driver, RegisterPageLocators.FIRSTNAME)
        self.lastname_input = Input(driver, RegisterPageLocators.LASTNAME)
        self.email_input = Input(driver, RegisterPageLocators.EMAIL)
        self.telephone_input = Input(driver, RegisterPageLocators.TELEPHONE)
        self.address_input = Input(driver, RegisterPageLocators.ADDRESS1)
        self.city_input = Input(driver, RegisterPageLocators.CITY)
        self.country_input = Input(driver, RegisterPageLocators.COUNTRY)

        self.login_btn = Button(driver, LoginPageLocators.LOGIN_BTN)

    def get_warning(self):
        self.warning = AlertDiv(self.driver, LoginPageLocators.ALERT_DIV)
        return self.warning

    def set_email(self, email):
        self.email_input.set_value(email)
        return self

    def set_password(self, email):
        self.password_input.set_value(email)
        return self
    def click_login(self):
        self.login_btn.click()
        time.sleep(2)
        try:
            self.get_warning()
            return self
        except:
            pass
