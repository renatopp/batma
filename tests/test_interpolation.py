import unittest
import math
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class Test_Interpolation(unittest.TestCase):
    def get_target(self, function):
        from batma.maths import interpolation
        return getattr(interpolation, function)

    def test_lerp(self):
        lerp = self.get_target('lerp')
        assert lerp(10, 50, 0.1) == 14
        assert lerp(10, 50, 0.3) == 22
        assert lerp(10, 50, 0.5) == 30
        assert lerp(10, 50, 0.7) == 38
        assert lerp(10, 50, 0.9) == 46

        assert lerp == self.get_target('linear')

    def test_smoothstep(self):
        smoothstep = self.get_target('smoothstep')
        self.assertAlmostEquals(smoothstep(10, 50, 0.1), 11.12, 2)
        self.assertAlmostEquals(smoothstep(10, 50, 0.3), 18.64, 2)
        self.assertAlmostEquals(smoothstep(10, 50, 0.5), 30.00, 2)
        self.assertAlmostEquals(smoothstep(10, 50, 0.7), 41.36, 2)
        self.assertAlmostEquals(smoothstep(10, 50, 0.9), 48.88, 2)

    def test_smoothstep_power(self):
        smoothstep = self.get_target('smoothstep')
        self.assertAlmostEquals(smoothstep(10, 50, 0.1, power=2), 10.09232384)
        self.assertAlmostEquals(smoothstep(10, 50, 0.3, power=3), 11.5850139402)
        self.assertAlmostEquals(smoothstep(10, 50, 0.5, power=4), 30.0)
        self.assertAlmostEquals(smoothstep(10, 50, 0.7, power=5), 49.9974838742)
        self.assertAlmostEquals(smoothstep(10, 50, 0.9, power=6), 50.0)

    def test_highpower(self):
        highpower = self.get_target('highpower')
        self.assertAlmostEquals(highpower(10, 50, 0.1, power=2), 10.4)
        self.assertAlmostEquals(highpower(10, 50, 0.3, power=3), 11.08)
        self.assertAlmostEquals(highpower(10, 50, 0.5, power=4), 12.5)
        self.assertAlmostEquals(highpower(10, 50, 0.7, power=5), 16.7228)
        self.assertAlmostEquals(highpower(10, 50, 0.9, power=6), 31.25764)

    def test_inverse_highpower(self):
        ihighpower = self.get_target('ihighpower')
        self.assertAlmostEquals(ihighpower(10, 50, 0.1, power=2), 17.6)
        self.assertAlmostEquals(ihighpower(10, 50, 0.3, power=3), 36.28)
        self.assertAlmostEquals(ihighpower(10, 50, 0.5, power=4), 47.5)
        self.assertAlmostEquals(ihighpower(10, 50, 0.7, power=5), 49.9028)
        self.assertAlmostEquals(ihighpower(10, 50, 0.9, power=6), 49.99996)

    def test_sin(self):
        sin = self.get_target('sin')
        self.assertAlmostEquals(sin(10, 50, 0.1), 16.2573786016)
        self.assertAlmostEquals(sin(10, 50, 0.3), 28.1596199896)
        self.assertAlmostEquals(sin(10, 50, 0.5), 38.2842712475)
        self.assertAlmostEquals(sin(10, 50, 0.7), 45.6402609675)
        self.assertAlmostEquals(sin(10, 50, 0.9), 49.5075336238)

    def test_inverse_sin(self):
        isin = self.get_target('isin')
        self.assertAlmostEquals(isin(10, 50, 0.1), 10.4924663762)
        self.assertAlmostEquals(isin(10, 50, 0.3), 14.3597390325)
        self.assertAlmostEquals(isin(10, 50, 0.5), 21.7157287525)
        self.assertAlmostEquals(isin(10, 50, 0.7), 31.8403800104)
        self.assertAlmostEquals(isin(10, 50, 0.9), 43.7426213984)

    def test_hermite(self):
        hermite = self.get_target('hermite')
        self.assertAlmostEquals(hermite(10, 0.3, 50, 0.8, 0.1), 11.1371, 4)
        self.assertAlmostEquals(hermite(10, 0.3, 50, 0.8, 0.3), 18.6337, 4)
        self.assertAlmostEquals(hermite(10, 0.3, 50, 0.8, 0.5), 29.9375, 4)
        self.assertAlmostEquals(hermite(10, 0.3, 50, 0.8, 0.7), 41.2613, 4)
        self.assertAlmostEquals(hermite(10, 0.3, 50, 0.8, 0.9), 48.8179, 4)

    def test_catmullrom(self):
        catmullrom = self.get_target('catmullrom')
        self.assertAlmostEquals(catmullrom(2, 4, 12, 13, 0.1),  4.5885, 4)
        self.assertAlmostEquals(catmullrom(2, 4, 12, 13, 0.3),  6.1795, 4)
        self.assertAlmostEquals(catmullrom(2, 4, 12, 13, 0.5),  8.0625, 4)
        self.assertAlmostEquals(catmullrom(2, 4, 12, 13, 0.7),  9.9255, 4)
        self.assertAlmostEquals(catmullrom(2, 4, 12, 13, 0.9), 11.4565, 4)


if __name__ == '__main__':
    unittest.main()