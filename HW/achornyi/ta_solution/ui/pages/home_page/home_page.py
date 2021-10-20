from ui.pages.base_pages.base_page import BasePage
import ui.pages.home_page._locators as locators


class HomePage(BasePage):
    def __init__(self):
        super().__init__(locators.PAGE_TITLE, locators.RELATIVE_PATH)

