import pyglet
from batma.algebra import Vector2

class Camera(object):
    def __init__(self, position=(0, 0), rotation=0.0, scale=1.0, following=None):
        self.x, self.y = position
        self.following = following
        self.rotation = rotation
        self.scale = scale
    
    @property
    def position(self): return Vector2(self.x, self.y)
    @position.setter
    def position(self, pos): self.x, self.y = pos

    def look_at(self, x, y):
        self.position = x, y

    def follow(self, obj):
        self.following = obj

    def update(self, tick):
        if self.following:
            self.position = self.following.position
    
    def reset(self, center):
        self.__x = self.x
        self.__y = self.y
        self.__scale = self.scale
        pyglet.gl.glTranslatef(-self.__x*self.__scale+center[0], -self.__y*self.__scale+center[1], 0)
    
        if self.rotation != 0.0:
            pyglet.gl.glTranslatef(self.__x*self.__scale, self.__y*self.__scale, 0)
            pyglet.gl.glRotatef(self.rotation, 0, 0, 1)
            pyglet.gl.glTranslatef(-self.__x*self.__scale, -self.__y*self.__scale, 0)

        if self.scale != 1.0:
            pyglet.gl.glScalef(self.scale, self.scale, 1)
        
    def apply(self, center):
        pyglet.gl.glTranslatef(self.__x*self.__scale+center[0], self.__y*self.__scale+center[1], 0)
        


