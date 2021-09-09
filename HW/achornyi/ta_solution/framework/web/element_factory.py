import framework.web.drivers as drivers
from framework.web.driver import Driver


def create_element(search):
    driver: Driver = drivers.get_current()
    return driver.find_element(search)
