from framework.web.elements.element import Element
from framework.web.search import Search


class BaseComponent:
    def __init__(self, wrapper: Element):
        self.wrapper = wrapper
