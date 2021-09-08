from ui.components.base_component import BaseComponent
import ui.locators.base_page.header as locators


class Header(BaseComponent):
    def __call__(self, *args, **kwargs):
        super().__init__(locators.WRAPPER)  # TODO - implement Element Factory on Framework to pass element

