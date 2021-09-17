from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_EMAIL = (By.CSS_SELECTOR, '#input-email')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '#input-password')
    BTN_LOGIN = (By.CSS_SELECTOR, 'input[type=Submit]')
    DIV_ALERT_NO_MATCH_EMAIL = (By.CSS_SELECTOR, 'div.alert.alert-danger')
