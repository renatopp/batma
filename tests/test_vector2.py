import unittest
import sys
import os
sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__), '..')))

class Test_Vector2(unittest.TestCase):
    def get_target(self, *args, **kwargs):
        from batma.algebra import Vector2
        return Vector2(*args, **kwargs)

    def test_init_no_param(self):
        v = self.get_target()
        assert v.x == 0
        assert v.y == 0

    def test_init(self):
        v = self.get_target(5, 10)
        assert v.x == 5
        assert v.y == 10

    def test_init_propertys(self):
        from batma.algebra import Vector2
        
        v = Vector2.Zero
        assert v.x == 0
        assert v.y == 0

        v = Vector2.One
        assert v.x == 1
        assert v.y == 1

    def test_list(self):
        v = self.get_target(5, 6)
        assert v[0] == 5
        assert v[1] == 6

    def test_copy(self):
        v1 = self.get_target(2, 3)
        assert v1.copy == v1.__copy__
        assert v1.__pos__ == v1.__copy__

        v2 = v1.copy()
        assert v1 is not v2
        assert v2.x == 2
        assert v2.y == 3

    def test_eq(self):
        v = self.get_target(3, 4)
        assert v == self.get_target(3, 4)
        assert v == [3, 4]
    
    def test_ne(self):
        assert self.get_target(3, 4) != self.get_target(2, 3)
        assert not self.get_target(3, 4) != self.get_target(3, 4)
    
    def test_nonzero(self):
        assert self.get_target(1, 2)
        assert not self.get_target()
    
    def test_len(self):
        assert len(self.get_target()) == 2

    def test_add(self):
        result = self.get_target(1, 2) + self.get_target(5, 3)
        assert result.x == 6
        assert result.y == 5

        result = self.get_target(1, 2) + [5, 3]
        assert result.x == 6
        assert result.y == 5
    
    def test_add_integer(self):
        result = self.get_target(2, 3) + 6
        assert result.x == 8
        assert result.y == 9

    def test_radd_integer(self):
        result = 6 + self.get_target(2, 3)
        assert result.x == 8
        assert result.y == 9

    def test_iadd(self):
        v = self.get_target(5, 2)
        v += [2, 3]
        assert v.x == 7
        assert v.y == 5
    
    def test_iadd_integer(self):
        v = self.get_target(5, 2)
        v += 3
        assert v.x == 8
        assert v.y == 5
    
    def test_sub(self):
        result = self.get_target(4, 4) - self.get_target(1, 2)
        assert result.x == 3
        assert result.y == 2

        result = self.get_target(4, 4) - (1, 2)
        assert result.x == 3
        assert result.y == 2

    def test_sub_integer(self):
        result = self.get_target(4, 4) - 3
        assert result.x == 1
        assert result.y == 1

    def test_rsub(self):
        result = [10, 5] - self.get_target(4, 3)
        assert result.x == 6
        assert result.y == 2

    def test_rsub_integer(self):
        result = 10 - self.get_target(4, 3)
        assert result.x == 6
        assert result.y == 7

    def test_isub(self):
        v = self.get_target(5, 6)
        v -= self.get_target(2, 1)
        assert v.x == 3
        assert v.y == 5

        v = (2, 3)
        v -= self.get_target(1, 1)
        assert v.x == 1
        assert v.y == 2

    def test_isub_integer(self):
        v = self.get_target(3, 4)
        v -= 2
        assert v.x == 1
        assert v.y == 2

        v = 10
        v -= self.get_target(3, 4)
        assert v.x == 7
        assert v.y == 6

    def test_mul(self):
        result = self.get_target(2, 3) * self.get_target(2, 2)
        assert result.x == 4
        assert result.y == 6

        result = self.get_target(5, 3) * [2, 2]
        assert result.x == 10
        assert result.y == 6

    def test_mul_integer(self):
        result = self.get_target(3, 5) * 3
        assert result.x == 9
        assert result.y == 15

    def test_rmul_integer(self):
        result = 5*self.get_target(2, 3)
        assert result.x == 10
        assert result.y == 15

    def test_imul(self):
        v = self.get_target(5, 2)
        v *= [2, 3]
        assert v.x == 10
        assert v.y == 6
    
    def test_imul_integer(self):
        v = self.get_target(5, 2)
        v *= 3
        assert v.x == 15
        assert v.y == 6
    
    def test_neg(self):
        v = -self.get_target(4, -2)
        assert v.x == -4
        assert v.y == 2

    def test_abs(self):
        v = self.get_target(2, 3)
        result = abs(v)
        self.assertAlmostEquals(result, 3.6055513)

        assert v.__abs__ == v.magnitude

    def test_magnitude_squared(self):
        result = self.get_target(3, 5).magnitude_squared()
        assert result == 34

    def test_normalize(self):
        v = self.get_target(2, 3)
        v.normalize()
        self.assertAlmostEquals(v.x, 0.5547002)
        self.assertAlmostEquals(v.y, 0.8320503)

    def test_normalized(self):
        v1 = self.get_target(2, 3)
        v2 = v1.normalized()
        assert v1.x == 2
        assert v1.y == 3
        self.assertAlmostEquals(v2.x, 0.5547002)
        self.assertAlmostEquals(v2.y, 0.8320503)

    def test_dot(self):
        v = self.get_target(2, 3)
        result = v.dot([5, 2])
        assert result == 16
    
    def test_cross(self):
        v = self.get_target(2, 3)
        assert v.cross() == [3, -2]
    
    def test_reflect(self):
        v = self.get_target(2, 3)
        result = v.reflect(self.get_target(3, 2).normalized())
        self.assertAlmostEquals(result[0], -3.5384615)
        self.assertAlmostEquals(result[1], -0.6923077)
    
    def test_angle(self):
        v1 = self.get_target(1, 1)
        v2 = self.get_target(2, 1)
        self.assertAlmostEquals(v1.angle(v2), 0.3217506)
        
    def test_project(self):
        v1 = self.get_target(1, 1)
        v2 = self.get_target(2, 1)
        assert v1.project(v2) == [1.2, 0.6]



if __name__ == '__main__':
    unittest.main()