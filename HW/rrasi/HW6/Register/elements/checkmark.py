
from HW.rrasi.HW6.Register.locators.register_page_locators import RegisterPageLocators

from HW.rrasi.HW6.Register.pages.register_page import RegisterUser



class PrivacyCheckmark(RegisterUser):

    def __init__(self, driver, locators):
        super().__init__(driver, locators)
        self.checkbox = driver.find_element(*RegisterPageLocators.PRIVACYPOLICYCHECKMARK)

    def click(self):
        self.element.click()
        return self


