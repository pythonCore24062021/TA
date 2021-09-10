import time

from HW.achornyi.ta_solution.tests.test_cases.base_test_case import BaseTestCase
from ui.common.enums import Currencies


class HW02Tests(BaseTestCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        pass

    def test_hw02_task01(self):
        self.start_page.select_currency(Currencies.EUR)
        time.sleep(3)
