from selenium.webdriver.remote.webelement import WebElement

from framework.web.search import Search


class Element:
    _wrapper: WebElement

    def __init__(self, wrapper: WebElement):
        self._wrapper = wrapper

    def find_child_element(self, search: Search) -> WebElement:
        return self._wrapper.find_element(*search.wrapper())

    def find_child_elements(self, search) -> list[WebElement]:
        return self._wrapper.find_elements(*search.wrapper())

    def click(self):
        self._wrapper.click()

