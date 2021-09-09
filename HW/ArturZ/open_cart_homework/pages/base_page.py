from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver=None):
        self.driver = driver if driver else webdriver.Chrome()

    def get_url(self, url):
        self.driver.get(url)

    def get_current_path(self):
        return self.driver.current_url

    def _wait_and_click(self, locator, timeout):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(expected_conditions.invisibility_of_element_located((locator))).click()
        except TimeoutException:
            return False
        return True
