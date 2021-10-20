from selenium import webdriver


class BasePage:

    def __init__(self, driver=None):
        self.driver = driver if driver else webdriver.Chrome("C:\dev\Python\TA with Python - SoftServe\chromedriver\chromedriver.exe")

    def get_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url
