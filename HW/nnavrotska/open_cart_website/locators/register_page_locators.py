from selenium.webdriver.common.by import By


class RegisterPageLocators:
    REGISTER_URL = 'http://taqc-opencart.epizy.com/index.php?route=account/register'
    REGISTER_ACCOUNT_HEADER = (By.CSS_SELECTOR, '#content > h1')

