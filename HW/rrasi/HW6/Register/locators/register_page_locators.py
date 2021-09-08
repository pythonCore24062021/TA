from selenium.webdriver.common.by import By


class RegisterPageLocators:
    FirstName= (By.XPATH, '//*[@input-firstname"]')
    LastName = (By.XPATH, '//*[@id="input-lastname"]')
    EMail = (By.XPATH, '//*[@id="input-email"]')
    Telephone = (By.XPATH, '//*[@id="input-telephone"]')
    Address1 = (By.XPATH, '//*[@id="input-address-1"]')
    city = (By.XPATH, '//*[@id="input-city"]')
    PostCode = (By.XPATH, '//*[@id="input-postcode"]')
    Country = (By.XPATH, '//*[@id="input-country"]')

