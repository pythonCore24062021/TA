from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import selenium.webdriver.support.expected_conditions as conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework.web._driver_settings import DEFAULT_DELAY
from framework.web.elements.element import Element


class Driver:
    def __init__(self, bt: str = "Chrome"):
        browsers = {"Chrome": webdriver.Chrome()}
        self._driver = browsers[bt]
        self._wait = WebDriverWait(self._driver, DEFAULT_DELAY)

    def find_element(self, element) -> Element:
        return Element(self._driver.find_element(*element.wrapper()))

    def maximize_window(self):
        self._driver.maximize_window()

    def quit(self):
        self._driver.quit()

    def get(self, url):
        self._driver.get(url)

    def wait_for_url_contains(self, relative_path):
        self._wait.until(conditions.url_contains(relative_path))

    def wait_for_title_matches(self, title):
        self._wait.until(conditions.title_is(title))


