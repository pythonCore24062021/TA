from selenium.webdriver.common.by import By

class HomePageLocators:
    HOME_URL = 'http://taqc-opencart.epizy.com/'
    MY_ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown > a')
    REGISTER_LINK = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a')
    LOGIN_LINK = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a')