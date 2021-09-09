import unittest
from HW.achornyi.ta_solution.tests.repositories import base_repository
from framework.web.driver import Driver
from framework.web.drivers import Drivers
from ui.pages.home_page.home_page import HomePage


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Drivers().set_current(Driver(base_repository.BROWSER_TYPE))
        Drivers().get_current().maximize_window()

    @classmethod
    def tearDownClass(cls):
        Drivers().get_current().quit()

    def setUp(self):
        Drivers().get_current().get(base_repository.BASE_URL)
        self.home_page = HomePage()
