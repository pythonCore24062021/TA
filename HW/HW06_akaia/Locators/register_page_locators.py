from selenium.webdriver.common.by import By


class RegisterPageLocators:

    INPUT_FIRST_NAME = (By.CSS_SELECTOR, '#input-firstname')
    INPUT_LAST_NAME = (By.CSS_SELECTOR, '#input-lastname')
    INPUT_EMAIL = (By.CSS_SELECTOR, '#input-email')
    INPUT_PHONE = (By.CSS_SELECTOR, '#input-telephone')
    INPUT_ADDRESS_ONE = (By.CSS_SELECTOR, '#input-address-1')
    INPUT_CITY = (By.CSS_SELECTOR, '#input-city')
    INPUT_POST_CODE = (By.CSS_SELECTOR, '#input-postcode')
    DROPDOWN_REGION_STATE = (By.CSS_SELECTOR, '#input-zone')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '#input-password')
    INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#input-confirm')
    CHECKBOX_PRIVACY = (By.CSS_SELECTOR, 'input[name="agree"]')
    BTN_CONTINUE = (By.CSS_SELECTOR, 'input[value="Continue"]')
