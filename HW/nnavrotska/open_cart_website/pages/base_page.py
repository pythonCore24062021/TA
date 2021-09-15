from selenium import webdriver

from HW.nnavrotska.open_cart_website.pages.header_component import HeaderComponent


class BasePage:
    def __init__(self, driver=None):
        self.driver = driver if driver else driver.Chrome()

    def get_url(self, url):
        self.url = url

    def get_current_path(self):
        return self.driver.current_url

    def get_header(self):
        return HeaderComponent(self.driver)
