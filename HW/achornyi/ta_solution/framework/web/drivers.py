import threading

import chromedriver_autoinstaller

from framework.web.driver import Driver


class Drivers:
    _drivers = dict()

    def __init__(self):
        self._drivers = {}
        self.update_and_configure_drivers()

    @property
    def _current_driver_key(self) -> int:
        return threading.get_ident()


    # @property
    # def current(self) -> Driver:
    #     return _drivers[_current_driver_key]


    def get_current(self) -> Driver:
        return self._drivers.get(self._current_driver_key)


    def set_current(self, value: Driver):
        self._drivers[self._current_driver_key] = value

    def update_and_configure_drivers(self):
        chromedriver_autoinstaller.install()
