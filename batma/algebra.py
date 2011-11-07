# -*- coding:utf-8 -*-
# Copyright (c) 2011 Renato de Pontes Pereira, renato.ppontes at gmail dot com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.

import math
import operator
from batma.util import classproperty

class Vector2(list):
    def __init__(self, x=0, y=0):
        super(Vector2, self).__init__((x, y))

    def get_x(self):
        return self[0]
    def set_x(self, value):
        self[0] = value
    x = property(get_x, set_x)

    def get_y(self):
        return self[1]
    def set_y(self, value):
        self[1] = value
    y = property(get_y, set_y)

    @classproperty
    @classmethod
    def Zero(cls):
        return Vector2(0.0, 0.0)

    @classproperty
    @classmethod
    def One(cls):
        return Vector2(1.0, 1.0)

    def __copy__(self):
        return Vector2(self.x, self.y)
    copy = __copy__

    def __repr__(self):
        return 'Vector2(%.2f, %.2f)' % (self.x, self.y)

    def __eq__(self, other):
        return self[0] == other[0] and self[1] == other[1]

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        try:
            return self[0] > other[0] and self[1] > other[1]
        except TypeError:
            return self[0] > other and self[1] > other

    def __le__(self, other):
        try:
            return self[0] < other[0] and self[1] < other[1]
        except TypeError:
            return self[0] < other and self[1] < other

    def __nonzero__(self):
        return self[0] != 0 or self[1] != 0

    def __add__(self, other):
        try:
            return Vector2(self[0]+other[0], self[1]+other[1])
        except TypeError:
            return Vector2(self[0]+other, self[1]+other)
    __radd__ = __add__

    def __iadd__(self, other):
        try:
            self[0] += other[0]
            self[1] += other[1]
        except TypeError:
            self[0] += other
            self[1] += other
        return self
    
    def __sub__(self, other):
        try:
            return Vector2(self[0]-other[0], self[1]-other[1])
        except TypeError:
            return Vector2(self[0]-other, self[1]-other)
    
    def __rsub__(self, other):
        try:
            return Vector2(other[0]-self[0], other[1]-self[1])
        except TypeError:
            return Vector2(other-self[0], other-self[1])
    
    def __isub__(self, other):
        try:
            self[0] -= other[0]
            self[1] -= other[1]
        except TypeError:
            self[0] -= other
            self[1] -= other
        return self

    def __mul__(self, other):
        try:
            return Vector2(self[0]*other[0], self[1]*other[1])
        except TypeError:
            return Vector2(self[0]*other, self[1]*other)
    __rmul__ = __mul__
    
    def __imul__(self, other):
        try:
            self[0] *= other[0]
            self[1] *= other[1]
        except TypeError:
            self[0] *= other
            self[1] *= other
        return self

    def __div__(self, other):
        try:
            return Vector2(operator.div(self[0], other[0]), 
                           operator.div(self[1], other[1]))
        except TypeError:
            return Vector2(operator.div(self[0], other), 
                           operator.div(self[1], other))

    def __rdiv__(self, other):
        try:
            return Vector2(operator.div(other[0], self[0]), 
                           operator.div(other[1], self[1]))
        except TypeError:
            return Vector2(operator.div(other, self[0]), 
                           operator.div(other, self[1]))

    def __floordiv__(self, other):
        try:
            return Vector2(operator.floordiv(self[0], other[0]), 
                           operator.floordiv(self[1], other[1]))
        except TypeError:
            return Vector2(operator.floordiv(self[0], other), 
                           operator.floordiv(self[1], other))

    def __rfloordiv__(self, other):
        try:
            return Vector2(operator.floordiv(other[0], self[0]), 
                           operator.floordiv(other[1], self[1]))
        except TypeError:
            return Vector2(operator.floordiv(other, self[0]), 
                           operator.floordiv(other, self[1]))

    def __truediv__(self, other):
        try:
            return Vector2(operator.truediv(self[0], other[0]), 
                           operator.truediv(self[1], other[1]))
        except TypeError:
            return Vector2(operator.truediv(self[0], other), 
                           operator.truediv(self[1], other))

    def __rtruediv__(self, other):
        try:
            return Vector2(operator.truediv(other[0], self[0]), 
                           operator.truediv(other[1], self[1]))
        except TypeError:
            return Vector2(operator.truediv(other, self[0]), 
                           operator.truediv(other, self[1]))

    __pos__ = __copy__

    def __neg__(self):
        return Vector2(-self[0], -self[1])

    def __abs__(self):
        return math.sqrt(self[0]**2 + self[1]**2)
    magnitude = __abs__

    def magnitude_squared(self):
        return self[0]**2 + self[1]**2

    def normalize(self):
        m = self.magnitude()
        if m:
            self[0] /= m
            self[1] /= m
        return self
    
    def normalized(self):
        v = self.copy()
        v.normalize()
        return v

    def dot(self, other):
        return self[0]*other[0] + self[1]*other[1]

    def cross(self):
        return Vector2(self[1], -self[0])

    def reflect(self, normal):
        d = 2*(self[0]*normal[0] + self[1]*normal[1])
        return Vector2(self[0]- d*normal[0], self[1] - d*normal[1])

    def angle(self, other):
        return math.acos(self.dot(other)/(self.magnitude()*other.magnitude()))

    def project(self, other):
        n = other.normalized()
        return self.dot(n)*n


class Vector3(list):
    def __init__(self, x=0, y=0, z=0):
        super(Vector3, self).__init__((x, y, z))

    def get_x(self):
        return self[0]
    def set_x(self, value):
        self[0] = value
    x = property(get_x, set_x)

    def get_y(self):
        return self[1]
    def set_y(self, value):
        self[1] = value
    y = property(get_y, set_y)

    def get_z(self):
        return self[2]
    def set_z(self, value):
        self[2] = value
    z = property(get_z, set_z)

    @classproperty
    @classmethod
    def Zero(cls):
        return Vector3(0.0, 0.0, 0.0)

    @classproperty
    @classmethod
    def One(cls):
        return Vector3(1.0, 1.0, 1.0)

    def __copy__(self):
        return Vector3(self.x, self.y, self.z)
    copy = __copy__

    def __repr__(self):
        return 'Vector3(%.2f, %.2f, %.2f)' % (self.x, self.y, self.z)

    def __eq__(self, other):
        return self[0] == other[0] and \
               self[1] == other[1] and \
               self[2] == other[2]

    def __ne__(self, other):
        return not self.__eq__(other)

    def __nonzero__(self):
        return self[0] != 0 or self[1] != 0 or self[2] != 0

    def __add__(self, other):
        try:
            return Vector3(self[0]+other[0], self[1]+other[1], self[2]+other[2])
        except TypeError:
            return Vector3(self[0]+other, self[1]+other, self[2]+other)
    __radd__ = __add__

    def __iadd__(self, other):
        try:
            self[0] += other[0]
            self[1] += other[1]
            self[2] += other[2]
        except TypeError:
            self[0] += other
            self[1] += other
            self[2] += other
        return self
    
    def __sub__(self, other):
        try:
            return Vector3(self[0]-other[0], self[1]-other[1], self[2]-other[2])
        except TypeError:
            return Vector3(self[0]-other, self[1]-other, self[2]-other)
    
    def __rsub__(self, other):
        try:
            return Vector3(other[0]-self[0], other[1]-self[1], other[2]-self[2])
        except TypeError:
            return Vector3(other-self[0], other-self[1], other-self[2])
    
    def __isub__(self, other):
        try:
            self[0] -= other[0]
            self[1] -= other[1]
            self[2] -= other[2]
        except TypeError:
            self[0] -= other
            self[1] -= other
            self[2] -= other
        return self

    def __mul__(self, other):
        try:
            return Vector3(self[0]*other[0], self[1]*other[1], self[2]*other[2])
        except TypeError:
            return Vector3(self[0]*other, self[1]*other, self[2]*other)
    __rmul__ = __mul__
    
    def __imul__(self, other):
        try:
            self[0] *= other[0]
            self[1] *= other[1]
            self[2] *= other[2]
        except TypeError:
            self[0] *= other
            self[1] *= other
            self[2] *= other
        return self
    
    def __div__(self, other):
        try:
            return Vector3(operator.div(self[0], other[0]), 
                           operator.div(self[1], other[1]),
                           operator.div(self[2], other[2]))
        except TypeError:
            return Vector3(operator.div(self[0], other), 
                           operator.div(self[1], other),
                           operator.div(self[2], other))

    def __rdiv__(self, other):
        try:
            return Vector3(operator.div(other[0], self[0]), 
                           operator.div(other[1], self[1]),
                           operator.div(other[2], self[2]))
        except TypeError:
            return Vector3(operator.div(other, self[0]), 
                           operator.div(other, self[1]),
                           operator.div(other, self[2]))

    def __floordiv__(self, other):
        try:
            return Vector3(operator.floordiv(self[0], other[0]), 
                           operator.floordiv(self[1], other[1]),
                           operator.floordiv(self[2], other[2]))
        except TypeError:
            return Vector3(operator.floordiv(self[0], other), 
                           operator.floordiv(self[1], other),
                           operator.floordiv(self[2], other))

    def __rfloordiv__(self, other):
        try:
            return Vector3(operator.floordiv(other[0], self[0]), 
                           operator.floordiv(other[1], self[1]),
                           operator.floordiv(other[2], self[2]))
        except TypeError:
            return Vector3(operator.floordiv(other, self[0]), 
                           operator.floordiv(other, self[1]),
                           operator.floordiv(other, self[2]))

    def __truediv__(self, other):
        try:
            return Vector3(operator.truediv(self[0], other[0]), 
                           operator.truediv(self[1], other[1]),
                           operator.truediv(self[2], other[2]))
        except TypeError:
            return Vector3(operator.truediv(self[0], other), 
                           operator.truediv(self[1], other),
                           operator.truediv(self[2], other))

    def __rtruediv__(self, other):
        try:
            return Vector3(operator.truediv(other[0], self[0]), 
                           operator.truediv(other[1], self[1]),
                           operator.truediv(other[2], self[2]))
        except TypeError:
            return Vector3(operator.truediv(other, self[0]), 
                           operator.truediv(other, self[1]),
                           operator.truediv(other, self[2]))

    __pos__ = __copy__

    def __neg__(self):
        return Vector3(-self[0], -self[1], -self[2])

    def __abs__(self):
        return math.sqrt(self[0]**2 + self[1]**2 + self[2]**2)
    magnitude = __abs__

    def magnitude_squared(self):
        return self[0]**2 + self[1]**2 + self[2]**2

    def normalize(self):
        m = self.magnitude()
        if m:
            self[0] /= m
            self[1] /= m
            self[2] /= m
        return self
    
    def normalized(self):
        v = self.copy()
        v.normalize()
        return v

    def dot(self, other):
        return self[0]*other[0] + self[1]*other[1] + self[2]*other[2]

    def cross(self):
        return Vector3( self[1]*other[2] - self[2]*other[1],
                       -self[0]*other[2] + self[2]*other[0],
                        self[0]*other[1] - self[1]*other[0])

    def reflect(self, normal):
        d = 2*(self[0]*normal[0] + self[1]*normal[1] + self[2]*normal[2])
        return Vector3(self[0] - d*normal[0],
                       self[1] - d*normal[1],
                       self[2] - d*normal[2])

    def angle(self, other):
        return math.acos(self.dot(other)/(self.magnitude()*other.magnitude()))

    def project(self, other):
        n = other.normalized()
        return self.dot(n)*n