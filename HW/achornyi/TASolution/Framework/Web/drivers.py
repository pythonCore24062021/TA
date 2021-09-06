import threading

import chromedriver_autoinstaller


def __init__(self):
    _drivers = {}
    update_and_configure_drivers()


@property
def _current_driver_key():
    return threading.get_ident()


@property
def current(self):
    return self._drivers[_current_driver_key]


@current.setter
def current(self, value):
    self._drivers[_current_driver_key] = value


def update_and_configure_drivers():
    chromedriver_autoinstaller.install()
