from selenium import webdriver

from framework.web.elements.element import Element


class Driver:
    def __init__(self, bt: str = "Chrome"):
        browsers = {"Chrome": webdriver.Chrome()}
        self._driver = browsers[bt]

    def find_element(self, element) -> Element:
        return Element(self._driver.find_element(*element.wrapper()))

    def maximize_window(self):
        self._driver.maximize_window()

    def quit(self):
        self._driver.quit()

    def get(self, url):
        self._driver.get(url)
