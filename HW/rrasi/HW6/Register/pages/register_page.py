import time


from Register.elements.button import Button
from Register.elements.checkmark import PrivacyCheckmark
from Register.elements.input import Input
from Register.pages.base_page import BasePage
#from HW.rrasi.HW6.Register.locators.login_page_locators import LoginPageLocators
from Register.locators.register_page_locators import RegisterPageLocators
from Register.elements.successmessage import Message
#from HW.rrasi.HW6.Register.elements.checkmark import PrivacyCheckmark
#import HW.rrasi.HW6.Register.elements.dropdown
from Register.elements.dropdown import Dropdown


class RegisterUser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.firstname_input = Input(driver, RegisterPageLocators.FIRSTNAME)
        self.lastname_input = Input(driver, RegisterPageLocators.LASTNAME)
        self.email_input = Input(driver, RegisterPageLocators.EMAIL)
        self.telephone_input = Input(driver, RegisterPageLocators.TELEPHONE)
        self.address_input = Input(driver, RegisterPageLocators.ADDRESS1)
        self.city_input = Input(driver, RegisterPageLocators.CITY)
        self.postcode_input = Input(driver, RegisterPageLocators.POSTCODE)
        self.country_input = Input(driver, RegisterPageLocators.COUNTRY)
        self.region_input = Dropdown(driver, RegisterPageLocators.REGION)
        self.password_input = Input(driver, RegisterPageLocators.PASSWORD)
        self.passwordconfirm_input = Input(driver, RegisterPageLocators.PASSWORDCONFIRM)
        self.privacycheckmark_input = PrivacyCheckmark(driver, RegisterPageLocators.PRIVACYPOLICYCHECKMARK)
        self.country_dropdown = Dropdown(driver, RegisterPageLocators.COUNTRY)
        self.firstname_label = Label(driver, RegisterPageLocators.FIRST_NAME_LABEL)
        self.lastname_label = Label(driver, RegisterPageLocators.LASTNAME_LABEL)
        self.email_label = Label(driver, RegisterPageLocators.EMAIL_LABEL)
        self.telephone_label = Label(driver, RegisterPageLocators.TELEPHONE_LABEL)
        self.address1_label = Label(driver, RegisterPageLocators.ADDRESS1_LABEL)
        self.city_label = Label(driver, RegisterPageLocators.CITY_LABEL)
        self.postcode_label = Label(driver, RegisterPageLocators.POSTCODE_LABEL)
        self.country_label = Label(driver, RegisterPageLocators.COUNTRY_LABEL)
        self.region_label = Label(driver, RegisterPageLocators.DROPDOWN_REGION_STATE_LABEL)
        self.passwordconfirm_label = Label(driver, RegisterPageLocators.PASSWORDCONFIRM_LABEL)
        self.privacycheckmark_label = self.driver.find_element(*RegisterPageLocators.PRIVACYPOLICYCHECKMARK_LINK)
        self.privacycheckmark_error = Error(driver, RegisterPageLocators.PRIVACYPOLICYCHECKMARK_ERRORMESSAGE)




        self.continue_btn = Button(driver, RegisterPageLocators.CONTINUEBTN)
    def get_region_dropdown(self):
        self.region_input = Dropdown(self.driver, RegisterPageLocators.REGION)
        return self.region_input
    def get_successmessage(self):
        # time.sleep(2)
        self.successmessage = Message(self.driver, RegisterPageLocators.SUCCESSMESSAGE)
        return self.successmessage

    def set_firstname(self, value):
        self.firstname_input.set_value(value)
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

    def set_postcode(self, postcode):
        self.postcode_input.set_value(postcode)
        return self

    def set_country(self, country):

        self.country_dropdown.select_by_value(country)
        time.sleep(1)
        return self
        # self.country_input.set_value(country)
        # return self

    def set_region(self, region):
        self.get_region_dropdown().select_by_value(region)
        return self

    def set_password(self, email):
        self.password_input.set_value(email)
        return self

    def set_passwordconfirm(self, passwordconfirm):
        self.passwordconfirm_input.set_value(passwordconfirm)
        return self

    def set_privacycheckmark(self):
        self.privacycheckmark_input.click()
        return self

    def click_continue(self):
        self.continue_btn.click()
        time.sleep(2)
        return self
        # try:
        #     self.get_message()
        #     return self
        # except:
        #     pass
    def get_err_firstname(self):
        self.error_firstname = Error(self.driver, RegisterPageLocators.FIRST_NAME_ERRORMESSAGE)
        return self.error
    def get_err_lastname(self):
        self.error_lastname = Error(self.driver, RegisterPageLocators.LASTNAME_ERRORMESSAGE)
        return self.error
    def get_err_email(self):
        self.error_email = Error(self.driver, RegisterPageLocators.EMAIL_ERRORMESSAGE)
        return self.error
    def get_err_telephone(self):
        self.error_telephone = Error(self.driver, RegisterPageLocators.TELEPHONE_ERRORMESSAGE)
        return self.error
    def get_err_address1(self):
        self.error_address = Error(self.driver, RegisterPageLocators.ADDRESS1_ERRORMESSAGE)
        return self.error
    def get_err_city(self):
        self.error_city = Error(self.driver, RegisterPageLocators.CITY_ERRORMESSAGE)
        return self.error
    def get_err_postcode(self):
        self.error_postcode = Error(self.driver, RegisterPageLocators.POSTCODE_ERRORMESSAGE)
        return self.error
    def get_err_region(self):
        self.error_region = Error(self.driver, RegisterPageLocators.DROPDOWN_REGION_STATE_ERRORMESSAGE)
        return self.error
    def get_err_password(self):
        self.error_password = Error(self.driver, RegisterPageLocators.PASSWORD_ERRORMESSAGE)
        return self.error


    def get_error_privacy(self):
        return self.element.text
