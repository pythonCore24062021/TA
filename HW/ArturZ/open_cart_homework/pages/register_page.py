import time

from HW.ArturZ.open_cart_homework.elements.alert import AlertDiv
from HW.ArturZ.open_cart_homework.elements.buttons import Button
from HW.ArturZ.open_cart_homework.elements.checkbox import Checkbox
from HW.ArturZ.open_cart_homework.elements.confirmation import ConfirmationDiv
from HW.ArturZ.open_cart_homework.elements.dropdowns import *
from HW.ArturZ.open_cart_homework.elements.input import Input
from HW.ArturZ.open_cart_homework.elements.list import List
from HW.ArturZ.open_cart_homework.locators.register_page_locators import RegisterPageLocators
from HW.ArturZ.open_cart_homework.pages.base_page import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.firstname_input = Input(driver, RegisterPageLocators.FIRSTNAME_INPUT)
        self.lastname_input = Input(driver, RegisterPageLocators.SECONDNAME_INPUT)
        self.email_input = Input(driver, RegisterPageLocators.EMAIL_INPUT)
        self.phone_input = Input(driver, RegisterPageLocators.PHONE_INPUT)
        self.password_input = Input(driver, RegisterPageLocators.PASSWORD_INPUT)
        self.confirmpass_input = Input(driver, RegisterPageLocators.CONFIRMPASSWORD_INPUT)
        self.continue_btn = Button(driver, RegisterPageLocators.CONTINUE_BTN)
        self.address_input = Input(driver, RegisterPageLocators.ADDRESS_INPUT)
        self.city_input = Input(driver, RegisterPageLocators.CITY_INPUT)
        self.postcode_input = Input(driver, RegisterPageLocators.POSTCODE_INPUT)
        self.country_select = List(driver, RegisterPageLocators.COUNTRY_DROPDOWN)
        self.region_select = List(driver, RegisterPageLocators.REGION_DROPDOWN)
        self.privacy_select = Checkbox(driver, RegisterPageLocators.PRIVACY_CHECKBOX)


    def get_warning(self):
        self.warning = AlertDiv(self.driver, RegisterPage.ALERT_DIV)
        return self.warning

    def get_hooray(self):
        self.success = ConfirmationDiv(self.driver, RegisterPage.HOORAY_DIV)
        return self.success


    def set_email(self, email):
        self.email_input.set_value(email)
        return self

    def set_password(self, password):
        self.password_input.set_value(password)
        return self

    def set_confirm_password(self, password):
        self.confirmpass_input.set_value(password)
        return self

    def set_phone(self, phone):
        self.phone_input.set_value(phone)
        return self

    def set_address(self, address):
        self.address_input.set_value(address)
        return self

    def set_city(self, city):
        self.city_input.set_value(city)
        return self

    def set_postcode(self, postcode):
        self.postcode_input.set_value(postcode)
        return self

    def set_first_name(self, firstname):
        self.firstname_input.set_value(firstname)
        return self

    def set_lastname(self, lastname):
        self.lastname_input.set_value(lastname)
        return self

    def select_privacy(self):
        self.privacy_select.click()

    def set_country(self):
        time.sleep(2)
        self.country_select.click()
        return self


    def set_region(self):
        self.region_select.click()
        return self



    def click_continue(self):
        self.continue_btn.click()
        time.sleep(2)
        try:
            self.get_warning()
            return self
        except:
            pass
