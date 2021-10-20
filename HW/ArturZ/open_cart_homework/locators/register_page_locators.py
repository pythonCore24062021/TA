from selenium.webdriver.common.by import By


class RegisterPageLocators:
    FIRSTNAME_INPUT = (By.XPATH, '//*[@id="input-firstname"]')
    SECONDNAME_INPUT = (By.XPATH, '//*[@id="input-lastname"]')
    EMAIL_INPUT = (By.XPATH, '//*[@id="input-email"]')
    PHONE_INPUT = (By.XPATH, '//*[@id="input-telephone"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="input-password"]')
    CONFIRMPASSWORD_INPUT = (By.XPATH, '//*[@id="input-confirm"]')
    ADDRESS_INPUT = (By.XPATH, '//*[@id="input-address-1"]')
    CITY_INPUT = (By.XPATH, '//*[@id="input-city"]')
    POSTCODE_INPUT = (By.XPATH, '//*[@id="input-postcode"]')
    CONTINUE_BTN = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')
    ALERT_DIV = (By.XPATH, '/html/body/div[2]/div[1]')
    HOORAY_DIV = (By.XPATH, '//*[@id="content"]/h1')
    PRIVACY_CHECKBOX = (By.XPATH, '//*[@id="content"]/form/div/div/input[1]')

    COUNTRY_DROPDOWN =(By.XPATH, '//select[@id="input-country"]/option[contains (text(), "Ukraine")]')
    REGION_DROPDOWN = (By.CSS_SELECTOR, '#input-zone > option:nth-child(2)')