

class BaseElement:
    def __init__(self, driver, locators=None, element=None):
        self.driver = driver
        self.locator = locators
        self.element = self.driver.find_element(*self.locator) if element is None else element


