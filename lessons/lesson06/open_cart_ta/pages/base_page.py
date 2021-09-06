from selenium import webdriver


class BasePage:

    def __init__(self, driver=None):
        self.driver = driver if driver else webdriver.Chrome()

    def get_url(self, url):
        self.driver.get(url)

    def get_current_path(self):
        return self.driver.current_url
