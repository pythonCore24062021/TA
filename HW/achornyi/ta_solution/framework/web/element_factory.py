from framework.web.drivers import Drivers


def create_element(search):
    driver = Drivers().get_current()
    return driver.find_element(search)
