from framework.web.element_factory import create_element
from framework.web.search import ID
from ui.common.enums import Currencies
import ui.pages.base_pages._locators as locators


class BasePage:
    def __init__(self, page_title: str, relative_path: str):
        self.page_title = page_title
        self.relative_path = relative_path
        self.create_element = create_element
        search = ID(locators.HEADER_ID)
        self._header = self.create_element(search)

    def __call__(self, *args, **kwargs):
        self.wait_for_page_is_loaded()

    def wait_for_page_is_loaded(self):
        pass  # TODO - Implement

    def select_currency(self, currency: Currencies):
 #       self._header.
        return self
