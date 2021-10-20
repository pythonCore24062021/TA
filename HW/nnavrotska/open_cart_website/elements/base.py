class BaseElement:
    def __init__(self, driver, locators=None, element=None):
        self.driver = driver
        self.locators = locators
        self.element = self.driver.find_element(*self.locators) if element is None else element
