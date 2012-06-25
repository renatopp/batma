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

__all__ = ['GameObject']

import weakref
from batma.maths.algebra import Vector2

class GameObject(object):
    __ID = 1

    @classmethod
    def new_id(cls):
        id = cls.__ID
        cls.__ID += 1
        return id

    def __init__(self, position=(0, 0), rotation=0.0, scale=1.0):
        self.id = GameObject.new_id()

        self.__x = None
        self.__y = None
        self.__rotation = None
        self.__scale = None
        self.__anchor_x = None
        self.__anchor_y = None
        self.__anchor_name_x = None
        self.__anchor_name_y = None

        self.__children = []
        self.__parent = None

        self.enabled = True
        self.static = False
        self.visible = True
        self.tag = ''

    # PARENTING ===============================================================
    def add(self, child, cascade=True):
        if cascade: child.set_parent(self, False)
        self.__children.append(weakref.ref(child))

    def remove(self, child, cascade=True):
        if cascade: child.set_parent(None, False)
        self.__children.remove(weakref.ref(child))

    def get_children(self):
        result = []
        for i in reversed(xrange(len(self.__children))):
            c = self.__children[i]()
            if c is None:
                del self.__children[i]
            else:
                result.insert(0, c)

        return result
    children = property(get_children)

    def get_parent(self):
        if self.__parent is None: 
            return None
        return self.__parent()
    def set_parent(self, value, cascade=True):
        if cascade:
            if self.parent is not None : 
                self.parent.remove(self, False)
            if value is not None:
                value.add(self, False)

        if value is not None:
            self.__parent = weakref.ref(value)
        else:
            self.__parent = value
    parent = property(get_parent, set_parent)

    def __contains__(self, child):
        return child in self.get_children()
    # =========================================================================


    # SPATIAL =================================================================
    def get_x(self):
        return self.__x
    def set_x(self, value):
        self.__x = value
    x = property(get_x, set_x)

    def get_y(self):
        return self.__y
    def set_y(self, value):
        self.__y = value
    y = property(get_y, set_y)

    def get_position(self):
        return Vector2(self.__x, self.__y)
    def set_position(self, value):
        self.x = value[0]
        self.y = value[1]
    position = property(get_position, set_position)

    def get_rotation(self):
        return self.__rotation
    def set_rotation(self, value):
        self.__rotation = value%360
    rotation = property(get_rotation, set_rotation)

    def get_scale(self):
        return self.__scale
    def set_scale(self, value):
        if isinstance(value, (int, long, float)):
            value = batma.Vector2(value, value)
        self.__scale = value
    scale = property(get_scale, set_scale)

    def get_anchor_x(self):
        return self.__anchor_x
    def set_anchor_x(self, value):
        if isinstance(value, basestring):
            self.__anchor_name_x = value
        else:
            self.__anchor_x = value
            self.__anchor_name_x = 'custom'
    anchor_x = property(get_anchor_x, set_anchor_x)

    def get_anchor_y(self):
        return self.__anchor_y
    def set_anchor_y(self, value):
        if isinstance(value, basestring):
            self.__anchor_name_y = value
        else:
            self.__anchor_y = value
            self.__anchor_name_y = 'custom'
    anchor_y = property(get_anchor_y, set_anchor_y)

    def get_anchor(self):
        return Vector2(self.__anchor_x, self.__anchor_y)
    def set_anchor(self, value):
        if isinstance(value, basestring): value = [value, value]
        self.anchor_x = value[0]
        self.anchor_y = value[1]
    anchor = property(get_anchor, set_anchor)

    def get_anchor_name(self):
        return (self.anchor_name_x, self.anchor_name_y)
    anchor_name = property(get_anchor_name)
    # =========================================================================

    def __repr__(self): return '<GameObject %d>'%self.id

if __name__ == '__main__':
    a = GameObject()
    b = GameObject()

    a.add(b)

    print b in a