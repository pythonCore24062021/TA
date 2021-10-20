import time

from framework.web import element_factory
from framework.web.drivers import Drivers
from framework.web.search import ID
from ui.common.enums import Currencies
import ui.pages.base_pages._locators as locators
from ui.pages.base_pages.header_component.header_component import Header


class BasePage:
    def __init__(self, page_title: str, relative_path: str):
        self.page_title = page_title
        self.relative_path = relative_path
        self.wait_for_page_is_loaded()
        self.header_wrapper = element_factory.create_element(ID(locators.HEADER_ID))
        self.header = Header(self.header_wrapper)

    def wait_for_page_is_loaded(self):
        Drivers().get_current().wait_for_url_contains(self.relative_path)
        Drivers().get_current().wait_for_title_matches(self.page_title)

    def select_currency(self, currency: Currencies):
        self.header.set_currency(currency)
