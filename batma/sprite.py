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

'''
Module for sprites handling.

Batma sprites are divided into two categories: `Sprite` and `AnimatedSprite`. 
The main difference is AnimatedSprite must be manually animated via 
``update_frame`` method.

There are some ways to create sprites:

    - **Static sprites**:
        
        - Passing a ``pyglet.image.Image`` to `Sprite`.
        - Passing a string with filename of image source to `Sprite`.

    - **Animated sprites**:

        - Passing a ``pyglet.image.Animation`` to `Sprite` (aumatically 
          animated).
        - Passing a list of ``pyglet.image.Texture`` to `AnimatedSprite` 
          (manually animated).
        - Passing a string with filename of atlas image source and parameter to 
          `AnimatedSprite` (manually animated).

'''

__docformat__ = 'restructuredtext'

import pyglet
from batma.node import BatmaNode
from batma.resource import load_image
from batma.resource import load_atlas
from batma.resource import _anchor_image
from batma.resource import _anchor_animation

class Sprite(BatmaNode, pyglet.sprite.Sprite):
    '''
    Sprite class for static and automatically animated sprites.
    '''

    def __init__(self, image, position=(0, 0), rotation=0, 
                                               scale=1, 
                                               opacity=255, 
                                               color=(255, 255, 255), 
                                               anchor=None,
                                               batch=None,
                                               group=None):
        '''
        Create a sprite.

        :Parameters:
            image : string or image
                Name of the image resource or a pyglet image.
            position : tuple
                Position of the anchor. Defaults to (0,0).
            rotation : float
                The rotation (degrees). Defaults to 0.
            scale : float
                The zoom factor. Defaults to 1.
            opacity : int
                The opacity (0=transparent, 255=opaque). Defaults to 255.
            color : tuple
                The color to colorize the child (RGB 3-tuple). Defaults to 
                (255,255,255).
            anchor : (float, float)
                (x,y)-point from where the image will be positions, rotated and 
                scaled in pixels. For example (image.width/2, image.height/2) 
                is the center (default).
        '''
        if isinstance(image, basestring):
            image = load_image(image)

        BatmaNode.__init__(self)
        pyglet.sprite.Sprite.__init__(self, image, batch=batch, group=group)

        anchor = anchor or "center"

        if isinstance(self.image, (pyglet.image.Animation, list, tuple)):
            _anchor_animation(self.image, anchor)
        else:
            _anchor_image(self.image, anchor)

        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.opacity = opacity
        self.color = color

        self.__must_update = True


    def get_x(self):
        return self._x
    def set_x(self, x):
        BatmaNode.set_x(self, x)
        self.__must_update = True
    x = property(get_x, set_x)       
    

    def get_y(self):
        return self._y
    def set_y(self, y):
        BatmaNode.set_y(self, y)
        self.__must_update = True
    y = property(get_y, set_y)


    def get_scale(self):
        return self._scale
    def set_scale(self, factor):
        BatmaNode.set_scale(self, factor)
        self.__must_update = True
    scale = property(get_scale, set_scale)


    def get_rotation(self):
        return self._rotation
    def set_rotation(self, angle):
        BatmaNode.set_rotation(self, angle)
        self.__must_update = True
    rotation = property(get_rotation, set_rotation)


    def draw(self):
        if self.__must_update: 
            self._update_position()
            self.__must_update = False

        pyglet.gl.glPushMatrix()
        for rotation, position, anchor in self._parent_rotations.values():
            pyglet.gl.glTranslatef(position[0]+anchor[0], position[1]+anchor[1], 0)
            pyglet.gl.glRotatef(-rotation, 0, 0, 1)
            pyglet.gl.glTranslatef(-(position[0]+anchor[0]), -(position[1]+anchor[1]), 0)
        
        pyglet.sprite.Sprite.draw(self)
        
        pyglet.gl.glPopMatrix()

    
class AnimatedSprite(pyglet.sprite.Sprite):
    '''
    Sprite class for manually animated sprites.
    '''

    def __init__(self, image, rows=None, cols=None, initial_frame=0, 
                                                    total_frames=None, 
                                                    position=(0, 0), 
                                                    rotation=0, 
                                                    scale=1, 
                                                    opacity=255, 
                                                    color=(255, 255, 255), 
                                                    anchor=None,
                                                    batch=None,
                                                    group=None):
        '''
        Create an animated sprite.

        :Parameters:
            image : string or image
                Name of the atlas image resource or a list of images.
            rows : int
                Row number of atlas image. Ignore this if image is an 
                animation.
            cols : int
                Column number of atlas image. Ignore this if image is an 
                animation.
            initial_frame : int
                Initial frame of animation. Ignore this if image is an 
                animation.
            total_frames : int
                How much frames starting from ``initial_frame`` the animation 
                will have. If None, will use until end of atlas. Ignore this if
                image is an animation.
            position : tuple
                Position of the anchor. Defaults to (0,0).
            rotation : float
                The rotation (degrees). Defaults to 0.
            scale : float
                The zoom factor. Defaults to 1.
            opacity : int
                The opacity (0=transparent, 255=opaque). Defaults to 255.
            color : tuple
                The color to colorize the child (RGB 3-tuple). Defaults to 
                (255,255,255).
            anchor : (float, float)
                (x,y)-point from where the image will be positions, rotated and 
                scaled in pixels. For example (image.width/2, image.height/2) 
                is the center (default).
        '''
        if isinstance(image, basestring):
            atlas = load_atlas(image, rows, cols)
        else:
            atlas = image
        
        self.frames = atlas
        self._initial_frame = initial_frame
        if not total_frames:
            self._total_frames = len(atlas) - initial_frame
            
        self._frame_index = initial_frame
        
        super(AnimatedSprite, self).__init__(self.frames[initial_frame],
                                             batch=batch,
                                             group=group)
        anchor = anchor or "center"
        _anchor_animation(self.frames, anchor)

        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.opacity = opacity
        self.color = color
    
    def update_frame(self):
        """
        Update the image sequence, setting the next image of animation.
        """
        self._frame_index += 1
        if self._frame_index >= self._initial_frame+self._total_frames:
            self._frame_index = self._initial_frame

        self.image = self.frames[self._frame_index]