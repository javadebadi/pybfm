from unittest import TestCase
from pybfm.irr import IRR

class TestIRR(TestCase):

    def setUp(self) -> None:
        self.p1_irr = IRR(
            [0,1],
            [-11,12],
            [None, None]
        )
        self.p2_irr = IRR(
            [0, 0, 1, 2, 3, 4, 5, 6],
            [-5, -6, -4, -10, 1, 2, 4, 40],
            [None, None, None, None ,None, None, None, None],
        )
        self.p3_irr = IRR(
            [0, 0, 1, 2, 3],
            [-5, -6, -10, 0, 5],
            [None, None, None, None ,'perpetuity'],
        )
        self.cam_irr = IRR(
            [0, 1, 2, 3, 4],
            [-120, 48, 48, 48, 48],
            [None, None, None, None, None],
        )
        self.atr_irr = IRR(
            [0, 1, 2, 3, 4],
            [-250, 90, 90, 90, 90],
            [None, None, None, None, None],
        )
        self.multiple_irr = IRR(
            [0, 1, 2],
            [-3000, 15000, -13000],
            [None, None, None],
        )
        return super().setUp()


    def test_find(self):
        self.assertAlmostEqual(self.p1_irr.find(), 0.0909, 4)
        self.assertAlmostEqual(self.p2_irr.find(), 0.1395, 4)
        self.assertAlmostEqual(self.p3_irr.find(), 0.1835, 4)
        self.assertAlmostEqual(self.cam_irr.find(), 0.2186, 4)
        self.assertAlmostEqual(self.atr_irr.find(), 0.1637, 4)

    def test_find_all(self):
        self.assertAlmostEqual(self.multiple_irr.find_all()[0], 0.1156, 4)
        self.assertAlmostEqual(self.multiple_irr.find_all()[1], 2.8844, 4)

    def test_get_yield_curve(self):
        xs, ys = self.multiple_irr.get_yield_curve(min_r=0, max_r=1, points=3)
        xs_correct = [0, 0.5, 1]
        ys_correct = [-1000.0, 1222.222, 1250.0]
        for index in range(len(xs)):
            self.assertAlmostEqual(xs[index], xs_correct[index], 3)
            self.assertAlmostEqual(ys[index], ys_correct[index], 3)
