from selenium.webdriver.common.by import By

class HomePageLocators:
    HOME_URL = 'http://taqc-opencart.epizy.com/'
    MY_ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md')
    REGISTER_LINK = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown > ul > li:nth-child(1) > a')
    LOGIN_LINK = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown > ul > li:nth-child(2) > a')
    # MY_ACCOUNT_DROPDOWN = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[1]')
    # REGISTER_LINK = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a')
    # LOGIN_LINK = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')

class HomePageLocatorsRegisteredUser:
    MY_ACCOUNT = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a')
    ORDER_HISTORY = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a')
    TRANSACTIONS = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(3) > a')
    DOWNLOADS = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(4) > a')
    LOGOUT = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a')