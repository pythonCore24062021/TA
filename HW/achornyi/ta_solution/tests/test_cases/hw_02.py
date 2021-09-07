from HW.achornyi.ta_solution.framework.web import drivers
from HW.achornyi.ta_solution.tests.repositories import hw_02_repository
from HW.achornyi.ta_solution.tests.test_cases.base_test_case import BaseTestCase


class HW02Tests(BaseTestCase):
    def setUp(self):
        drivers.current.get(hw_02_repository.BASE_URL)

    def tearDown(self):
        pass

    def test_hw02_task01(self):
        pass
