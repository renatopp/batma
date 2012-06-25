import unittest
import math
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class Test_Math(unittest.TestCase):
    def get_target(self, function):
        from batma.maths import mathematic
        return getattr(mathematic, function)

    def test_clamps(self):
        clamp = self.get_target('clamp')
        assert clamp(5, 0, 10) == 5
        assert clamp(5, 0, 3) == 3
        assert clamp(5, 7, 10) == 7

    def test_wrap_angle(self):
        wrap_angle = self.get_target('wrap_angle')
        self.assertAlmostEquals(wrap_angle(-4.9), 1.383185, 6)
        self.assertAlmostEquals(wrap_angle(-1.5), -1.5, 6)
        self.assertAlmostEquals(wrap_angle(0.6), 0.6, 6)
        self.assertAlmostEquals(wrap_angle(3.17), -3.113185, 6)

    def test_distance(self):
        distance = self.get_target('distance')
        assert distance(0, 5) == 5
        assert distance(0.4, 1.5) == 1.1
        assert distance(0.1, 8.0) == 7.9

        self.assertAlmostEquals(distance([2, 1], [5, 6]), 5.83095189)

    def test_mod(self):
        mod = self.get_target('mod')
        assert mod(5, 2) == 5%2
        assert mod(4, 3) == 4%3
        assert mod(2, 6) == 2%6
        assert mod(9, 8) == 9%8
        assert mod(4, 1) == 4%1

    def test_sign(self):
        sign = self.get_target('sign')
        assert sign(-1) == -1
        assert sign(1) == 1
        assert sign(-2) == -1
        assert sign(3) == 1
        assert sign(-8.0) == -1
        assert sign(2.6) == 1
        assert sign(0) == 0

    def test_step(self):
        step = self.get_target('step')
        assert step(5.9, 6) == 0
        assert step(6.1, 6) == 1
        assert step(6, 6) == 1

    def test_inversesqrt(self):
        inversesqrt = self.get_target('inversesqrt')
        assert inversesqrt(5) == 1.0/math.sqrt(5)
        assert inversesqrt(0.1) == 1.0/math.sqrt(0.1)

if __name__ == '__main__':
    unittest.main()