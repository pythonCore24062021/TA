from selenium.webdriver.common.by import By


class RegisterPageLocators:
    REGISTER_URL = 'http://taqc-opencart.epizy.com/index.php?route=account/register'
    REGISTER_ACCOUNT_HEADER = (By.CSS_SELECTOR, '#content > h1')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE_INPUT = (By.CSS_SELECTOR, '#input-telephone')
    FAX_INPUT = (By.CSS_SELECTOR, '#input-fax')
    COMPANY_INPUT = (By.CSS_SELECTOR, '#input-company')
    ADDRESS_1_INPUT = (By.CSS_SELECTOR, '#input-address-1')
    ADDRESS_2_INPUT = (By.CSS_SELECTOR, '#input-address-2')
    CITY_INPUT = (By.CSS_SELECTOR, '#input-city')
    POST_CODE_INPUT = (By.CSS_SELECTOR, '#input-postcode')
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, '#input-country')
    REGION_STATE_DROPDOWN = (By.CSS_SELECTOR, '#input-zone')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, '#input-confirm')
    SUBSCRIBE_YES_RADIO_BUTTON = (By.CSS_SELECTOR, '#content > form > fieldset:nth-child(4) > div > div > label:nth-child(1) > input[type=radio]')
    SUBSCRIBE_NO_RADIO_BUTTON = (By.CSS_SELECTOR, '#content > form > fieldset:nth-child(4) > div > div > label:nth-child(2) > input[type=radio]')
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, '#content > form > div > div > input[type=checkbox]:nth-child(2)')
    CONTINUE_BTN = (By.CSS_SELECTOR, '#content > form > div > div > input.btn.btn-primary')


