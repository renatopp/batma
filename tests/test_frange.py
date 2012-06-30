import unittest
import math
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class Test_Math(unittest.TestCase):
    def get_target(self, function):
        from batma import util
        return getattr(util, function)

    def test_frange(self):
        frange = self.get_target('frange')
        assert frange(5) == [0., 1., 2., 3., 4.]
        assert frange(2, 5) == [2., 3., 4.]
        assert frange(0, 0.3, 0.1) == [0., 0.1, 0.2]

    def test_xfrange(self):
        xfrange = self.get_target('xfrange')
        assert hasattr(xfrange(10), 'next')
        assert [i for i in xfrange(5)] == [0., 1., 2., 3., 4.]
        assert [i for i in xfrange(2, 5)] == [2., 3., 4.]
        assert [i for i in xfrange(0, 0.3, 0.1)] == [0., 0.1, 0.2]

if __name__ == '__main__':
    unittest.main()