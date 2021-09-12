import time

from elements.button import Button
from elements.input import Input
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators
from elements.successmessage import Message


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
        self.region_input = Input(driver, RegisterPageLocators.REGION)
        self.password_input = Input(driver, RegisterPageLocators.PASSWORD)
        self.passwordconfirm_input = Input(driver, RegisterPageLocators.PASSWORDCONFIRM)
        self.privacycheckmark_input = Input(driver, RegisterPageLocators.PRIVACYPOLICYCHECKMARK)


        self.continue_btn = Button(driver, RegisterPageLocators.CONTINUEBTN)

    def get_message(self):
        self.message = Message(self.driver, RegisterPageLocators.SUCCESSMESSAGE)
        return self.message

    def set_firstname(self, firstname):
        self.firstname_input.set_value(firstname)
        return self

    def set_lastname(self, lastname):
        self.lastname_input.set_value(lastname)
        return self

    def set_email(self, email):
        self.email_input.set_value(email)
        return self

    def set_telephone(self, telephone):
        self.telephone_input.set_value(telephone)
        return self

    def set_address(self, address):
        self.address_input.set_value(address)
        return self

    def set_city(self, city):
        self.city_input.set_value(city)
        return self

    def set_country(self, country):
        self.country_input.set_value(country)
        return self

    def set_region(self, region):
        self.region_input.set_value(region)
        return self

    def set_password(self, email):
        self.password_input.set_value(email)
        return self

    def set_passwordconfirm(self, passwordconfirm):
        self.passwordconfirm_input.set_value(passwordconfirm)
        return self

    def set_privacycheckmark(self, privacycheckmark):
        self.privacycheckmark_input.set_value(privacycheckmark)
        return self

    def click_continue(self):
        self.continue_btn.click()
        time.sleep(2)
        try:
            self.get_message()
            return self
        except:
            pass
