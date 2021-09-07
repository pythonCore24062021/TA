from selenium.webdriver.common.by import By


class RegisterPageLocators:
    FirstName= (By.XPATH, '//*[@input-firstname"]')
    LastName = (By.XPATH, '//*[@id="input-lastname"]')
    EMail = (By.XPATH, '//*[@id="input-email"]')
    Telephone = (By.XPATH, '//*[@id="input-telephone"]')
