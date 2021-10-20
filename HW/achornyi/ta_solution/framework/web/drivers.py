import threading

import chromedriver_autoinstaller

from framework.system.singleton_pattern import Singleton
from framework.web.driver import Driver


class Drivers(metaclass=Singleton):
    _drivers = dict()

    def __init__(self):
        self._drivers = {}
        self.update_and_configure_drivers()

    @property
    def _current_driver_key(self) -> int:
        return threading.get_ident()

    @property
    def current(self) -> Driver:
        return self._drivers[self._current_driver_key]

    def get_current(self) -> Driver:
        return self._drivers.get(self._current_driver_key)

    def set_current(self, value: Driver):
        self._drivers[self._current_driver_key] = value

    def delete_current(self):
        del self._drivers[self._current_driver_key]

    @staticmethod
    def update_and_configure_drivers():
        chromedriver_autoinstaller.install()
