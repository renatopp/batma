import pyglet
from batma.algebra import Vector2

class BatmaNode(object):
    def __init__(self):
        self.children = []
        self.parent = None

        self._x = 0
        self._y = 0
        self._scale = 1.0
        self._rotation = 0.0
        self.transform_anchor_x = 0
        self.transform_anchor_y = 0
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        diff = x - self._x
        for c in self.children: c.x += diff
        self._x = x
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        diff = y - self._y
        for c in self.children: c.y += diff
        self._y = y
    
    @property
    def position(self):
        return Vector2(self.x, self.y)
    
    @position.setter
    def position(self, pos):
        self.x, self.y = pos

    @property
    def scale(self):
        return self._scale
    
    @scale.setter
    def scale(self, factor):
        diff = factor - self._scale
        for c in self.children: c.scale += diff
        self._scale = factor

    @property
    def rotation(self):
        return self._rotation
    
    @rotation.setter
    def rotation(self, angle):
        diff = angle - self._rotation
        for c in self.children: c.rotation += diff
        self._rotation = angle

    @property
    def transform_anchor(self):
        return Vector2(self.transform_anchor_x, self.transform_anchor_y)
    
    @transform_anchor.setter
    def transform_anchor(self, pos):
        self.transform_anchor_x, self.transform_anchor_y = pos

    def add(self, child):
        child.parent = self
        self.children.append(child)

    def remove(self, child):
        child.parent = None
        self.children.remove(child)

    def transform(self):
        """
        Apply ModelView transformations

        you will most likely want to wrap calls to this function with
        glPushMatrix/glPopMatrix
        """

        pyglet.gl.glTranslatef(self.position[0], self.position[1], 0)
        pyglet.gl.glTranslatef(self.transform_anchor_x, self.transform_anchor_y, 0)


        if self.rotation != 0.0:
            pyglet.gl.glRotatef(-self._rotation, 0, 0, 1)

        if self.scale != 1.0:
            pyglet.gl.glScalef(self._scale, self._scale, 1)

        if self.transform_anchor != (0, 0):
            pyglet.gl.glTranslatef(
                -self.transform_anchor_x,
                -self.transform_anchor_y,
                0) 