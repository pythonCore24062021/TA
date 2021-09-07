from framework.web.elements.element import Element


class BaseComponent:
    def __init__(self, wrapper: Element):
        self.wrapper = wrapper

        