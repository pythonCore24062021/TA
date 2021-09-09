from framework.web.elements.element import Element
from framework.web.search import Search


class BaseComponent:
    def __init__(self, wrapper: Element):
        self._wrapper = wrapper

    def find_child_element(self, search: Search):
        self._wrapper.find_child_element(search)

    def find_child_elements(self, search: Search):
        self._wrapper.find_child_elements(search)
