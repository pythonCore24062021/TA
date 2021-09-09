from ui.pages.base_component import BaseComponent
import ui.pages.base_pages.header_component._locators as locators


class Header(BaseComponent):
    def __call__(self, *args, **kwargs):
        super().__init__(locators.WRAPPER)  # TODO - implement Element Factory on Framework to pass element

