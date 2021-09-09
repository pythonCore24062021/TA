from selenium.webdriver.common.by import By


class Search:
    def __init__(self, wrapper):
        self._wrapper = wrapper

    def wrapper(self):
        return self._wrapper


def xpath(selector: str):
    search = By.XPATH(selector)
    return Search(search)


def css_selector(selector: str):
    search = By.CSS_SELECTOR(selector)
    return Search(search)


def ID(selector):
    search = (By.ID, selector)
    return Search(search)
