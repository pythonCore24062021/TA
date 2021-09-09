import unittest
import framework.web.drivers as drivers
from HW.achornyi.ta_solution.tests.repositories import base_repository
from framework.web.driver import Driver
from ui.pages.home_page.home_page import HomePage


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        drivers.set_current(Driver(base_repository.BROWSER_TYPE))
        drivers.get_current().maximize_window()

    @classmethod
    def tearDownClass(cls):
        drivers.get_current().quit()

    def setUp(self):
        drivers.get_current().get(base_repository.BASE_URL)
        self.home_page = HomePage()
