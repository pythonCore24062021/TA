from selenium.webdriver.common.by import By


class RegisterPageLocators:
    FIRSTNAME = (By.CSS_SELECTOR, '#input-firstname')
    LASTNAME = (By.XPATH, '//*[@id="input-lastname"]')
    EMAIL = (By.XPATH, '//*[@id="input-email"]')
    TELEPHONE = (By.XPATH, '//*[@id="input-telephone"]')
    ADDRESS1 = (By.XPATH, '//*[@id="input-address-1"]')
    CITY = (By.XPATH, '//*[@id="input-city"]')
    POSTCODE = (By.XPATH, '//*[@id="input-postcode"]')
    DROPDOWN_REGION_STATE = (By.CSS_SELECTOR, '#input-zone')
    COUNTRY = (By.XPATH, '//*[@id="input-country"]')
    COUNTRYOPTION = (By.XPATH, '//*[@id="input-country"]/option[2]')
    REGION = (By.ID, 'input-zone')
    REGIONOPTION = (By.XPATH, '//*[@id="input-zone"]/option[2]')
    REGION_OPTION_Albania = (By.XPATH, '//*[@id="input-zone"]/option[2]')
    PASSWORD = (By.XPATH, '//*[@id="input-password"]')
    PASSWORDCONFIRM = (By.XPATH, '//*[@id="input-confirm"]')
    PRIVACYPOLICYCHECKMARK = (By.XPATH, '//*[@id="content"]/form/div/div/input[1]')
    CONTINUEBTN = (By.XPATH, './/input[@class="btn btn-primary"]')
    SUCCESSMESSAGE = (By.XPATH, '//*[@id="content"]/h1')

