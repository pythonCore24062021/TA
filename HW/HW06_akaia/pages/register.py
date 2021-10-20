from pages.base_page import BasePage
from Locators.register_page_locators import RegisterPageLocators
from Elements.input import Input
from Elements.button import Button
from Elements.checkbox import CheckBox
import Elements.dropdown


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_input = Input(self.driver, RegisterPageLocators.INPUT_FIRST_NAME)
        self.last_name_input = Input(self.driver, RegisterPageLocators.INPUT_LAST_NAME)
        self.email_input = Input(self.driver, RegisterPageLocators.INPUT_EMAIL)
        self.phone_input = Input(self.driver, RegisterPageLocators.INPUT_PHONE)
        self.address_input = Input(self.driver, RegisterPageLocators.INPUT_ADDRESS_ONE)
        self.city_input = Input(self.driver, RegisterPageLocators.INPUT_CITY)
        self.post_code_input = Input(self.driver, RegisterPageLocators.INPUT_POST_CODE)
        self.region_state_dropdown = Elements.dropdown.DropdownRegionState(self.driver, RegisterPageLocators.DROPDOWN_REGION_STATE)
        self.password_input = Input(self.driver, RegisterPageLocators.INPUT_PASSWORD)
        self.password_confirm_input = Input(self.driver, RegisterPageLocators.INPUT_PASSWORD_CONFIRM)
        self.checkbox_privacy = CheckBox(self.driver, RegisterPageLocators.CHECKBOX_PRIVACY)
        self.btn_continue = Button(self.driver, RegisterPageLocators.BTN_CONTINUE)

    def set_first_name(self, value):
        self.first_name_input.set_value(value)
        return self

    def set_last_name(self, value):
        self.last_name_input.set_value(value)
        return self

    def set_email(self, value):
        self.email_input.set_value(value)
        return self

    def set_phone(self, value):
        self.phone_input.set_value(value)
        return self

    def set_address(self, value):
        self.address_input.set_value(value)
        return self

    def set_city(self, value):
        self.city_input.set_value(value)
        return self

    def set_post_code(self, value):
        self.post_code_input.set_value(value)
        return self

    def set_region_state(self):
        self.region_state_dropdown.select_first_value()
        return self

    def set_password(self, value):
        self.password_input.set_value(value)
        return self

    def set_password_confirm(self, value):
        self.password_confirm_input.set_value(value)
        return self

    def check_checkbox_privacy(self):
        self.checkbox_privacy.check()
        return self

    def click_continue_btn(self):
        self.btn_continue.click()
        return self
