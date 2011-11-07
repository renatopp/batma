import pyglet
from batma.algebra import Vector2

class BatmaNode(object):
    def __init__(self, position=(0, 0), rotation=0.0, scale=1.0):
        self.children = []
        self.parent = None

        self._x = position[0]
        self._y = position[1]
        self._rotation = rotation
        self._scale = scale
        self.anchor_x = 0
        self.anchor_y = 0
        
        self._parent_rotations = {} #"parent: [rotation, (anchor_x, anchor_y)]"
    

    def get_x(self):
        return self._x
    def set_x(self, x):
        diff = x - self._x
        for c in self.children: c.x += diff
        self._x = x
    x = property(get_x, set_x)
    

    def get_y(self):
        return self._y
    def set_y(self, y):
        diff = y - self._y
        for c in self.children: c.y += diff
        self._y = y
    y = property(get_y, set_y)
    

    def get_position(self):
        return Vector2(self.x, self.y)
    def set_position(self, pos):
        self.x, self.y = pos
    position = property(get_position, set_position)


    def get_scale(self):
        return self._scale
    def set_scale(self, factor):
        diff = factor - self._scale
        for c in self.children: c.scale += diff
        self._scale = factor
    scale = property(get_scale, set_scale)


    def get_rotation(self):
        return self._rotation
    def set_rotation(self, angle):
        self._rotation = angle
        
        for c in self.children:
            c.set_parent_rotation(self)
    rotation = property(get_rotation, set_rotation)


    def get_anchor(self):
        return Vector2(self.anchor_x, self.anchor_y)
    def set_anchor(self, pos):
        self.anchor_x, self.anchor_y = pos
    anchor = property(get_anchor, set_anchor)


    def set_parent_rotation(self, parent):
        self._parent_rotations[parent] = (parent.rotation, parent.position, 
                                                           parent.anchor)

        for c in self.children:
            c.set_parent_rotation(parent)

    def add(self, child):
        child.parent = self
        self.children.append(child)

    def remove(self, child):
        child.parent = None
        self.children.remove(child)

    def transform(self):
        pyglet.gl.glTranslatef(self.position[0], self.position[1], 0)
        pyglet.gl.glTranslatef(self.anchor_x, self.anchor_y, 0)

        if self.rotation != 0.0:
            pyglet.gl.glRotatef(-self._rotation, 0, 0, 1)

        if self.scale != 1.0:
            pyglet.gl.glScalef(self._scale, self._scale, 1)

        if self.anchor != (0, 0):
            pyglet.gl.glTranslatef(-self.anchor_x, -self.anchor_y, 0)

        # for rotation, position, anchor in self._parent_rotations.values():
        #     pyglet.gl.glTranslatef(position[0]+anchor[0], position[1]+anchor[1], 0)
        #     pyglet.gl.glRotatef(-rotation, 0, 0, 1)
        #     pyglet.gl.glTranslatef(-(position[0]+anchor[0]), -(position[1]+anchor[1]), 0)        
        #     