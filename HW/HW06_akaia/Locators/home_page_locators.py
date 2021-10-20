from selenium.webdriver.common.by import By


class HomePageLocators:
    MY_ACCOUNT_DROPDOWN = (By.XPATH, './/a[@title="My Account"]')
    REGISTER_LINK = (By.XPATH, './/li[@class="dropdown open"]/ul/li[1]/a')
    LOGIN_LINK = (By.XPATH, './/a[contains(text(), "Login")]')
    LOGOUT_LINK = (By.XPATH, './/a[contains(text(), "Logout")]')
