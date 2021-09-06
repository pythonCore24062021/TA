from HW.achornyi.TASolution.Framework.Web import drivers
from HW.achornyi.TASolution.Tests.Repositories import HW02Repository
from HW.achornyi.TASolution.Tests.TestCases.BaseTestCase import BaseTestCase


class HW02Tests(BaseTestCase):
    def setUp(self):
        drivers.current.get(HW02Repository.BASE_URL)

    def tearDown(self):
        pass

    def test_hw02_task01(self):
        pass
