from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_URL = 'http://taqc-opencart.epizy.com/index.php?route=account/login'
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    PSW_INPUT = (By.CSS_SELECTOR, '#input-password')
    LOGIN_BTN = (By.CSS_SELECTOR, '#content > div > div:nth-child(2) > div > form > input')
    ALERT_DIV = (By.CSS_SELECTOR, 'body > div:nth-child(4) > div.alert.alert-danger')