import time


from HW.rrasi.HW6.Register.elements.button import Button
from HW.rrasi.HW6.Register.elements.input import Input
from HW.rrasi.HW6.Register.pages.base_page import BasePage
#from HW.rrasi.HW6.Register.locators.login_page_locators import LoginPageLocators
from HW.rrasi.HW6.Register.locators.register_page_locators import RegisterPageLocators
from HW.rrasi.HW6.Register.elements.successmessage import Message
#from HW.rrasi.HW6.Register.elements.checkmark import PrivacyCheckmark
#import HW.rrasi.HW6.Register.elements.dropdown


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
        self.region_input = Input(driver, RegisterPageLocators.REGION)
        self.password_input = Input(driver, RegisterPageLocators.PASSWORD)
        self.passwordconfirm_input = Input(driver, RegisterPageLocators.PASSWORDCONFIRM)
        self.privacycheckmark_input = Input(driver, RegisterPageLocators.PRIVACYPOLICYCHECKMARK)


        self.continue_btn = Button(driver, RegisterPageLocators.CONTINUEBTN)

    def get_successmessage(self):
        self.successmessage = Message(self.driver, RegisterPageLocators.SUCCESSMESSAGE)
        return self.message

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
