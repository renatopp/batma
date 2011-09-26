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
This module provides an interface to pyglet resources.
'''

__docformat__ = 'restructuredtext'

import pyglet

def add_resource_path(*path):
    '''
    Registers a resource path in pyglet resources.
    
    **Important!** This function doesn't call ``pyglet.resource.reindex``, if 
    you are using standalone you must call it manually.

    :Parameters:
        path : str
            One or more strings with dir name of resource location
    '''
    pyglet.resource.path.extend(path)

def load_image(file_name, flip_x=False, flip_y=False, rotate=0, anchor=(0, 0)):
    '''
    Loads an image from resource locations. The file must be in some of 
    registred resources path.

    :Parameters:
        file_name : str
            Filename of the image source to load.
        flip_x : bool
            If True, the returned image will be flipped horizontally.
        flip_y : bool
            If True, the returned image will be flipped vertically.
        rotate : int
            The returned image will be rotated clockwise by the given number of 
            degrees (a mulitple of 90).
        anchor : "center" or a tuple (anchor_x, anchor_y)
            Image's anchor.

    :rtype: ``pyglet.image.Texture``
    :return: A ``pyglet.image.Texture`` object
    '''
    image = pyglet.resource.image(file_name, flip_x, flip_y, rotate)
    return _anchor_image(image, anchor)

def load_atlas(file_name, rows, cols):
    '''
    Loads a regular atlas image. 

    With the image loaded, it will be divided by ``pyglet.image.ImageGrid`` in 
    ``rows*cols`` pieces of same size. The atlas regions must have the **same 
    size**.

    An atlas image with 2 rows and 3 cols will be ordered as follows::

        +---+---+---+
        | 1 | 2 | 3 |
        +---+---+---+
        | 4 | 5 | 6 |
        +---+---+---+
    
    where the number are the list position, e.g., ``[1, 2, 3, 4, 5, 6]``
    
    :Parameters:
        file_name : str
            Filename of the image source to load.
        rows : int
            Row number of atlas image.
        cols : int
            Column number of atlas image.

    :rtype: list of ``pyglet.image.Texture``
    :return: A list with textures images.
    '''
    image = pyglet.resource.image(file_name)
    atlas = pyglet.image.ImageGrid(image, rows, cols)
    sequence = atlas.get_texture_sequence()

    total = rows*cols
    temp = []
    for i in xrange(total):
        j = total-cols*(i/cols+1)+i%cols
        temp.append(sequence.items[j])
    
    return temp

def load_animation(file_name, flip_x=False, flip_y=False, rotate=0, 
                                                          anchor=(0, 0)):
    '''
    Loads an animation, e.g, a gif file.

    :Parameters:
        file_name : str
            Filename of the image source to load.
        flip_x : bool
            If True, the returned image will be flipped horizontally.
        flip_y : bool
            If True, the returned image will be flipped vertically.
        rotate : int
            The returned image will be rotated clockwise by the given number of 
            degrees (a mulitple of 90).
        anchor : "center" or a tuple (anchor_x, anchor_y)
            Image's anchor. Applied to all frames.

    :rtype: ``pyglet.image.Animation``
    :return: A ``pyglet.image.Animation`` object.
    '''
    animation = pyglet.resource.animation(file_name)
    return _anchor_animation(animation, anchor)

def load_atlas_animation(file_name, rows, cols, initial_frame=0, 
                                                total_frames=None, 
                                                duration=0.0166, 
                                                anchor=(0, 0)):
    '''
    Create an animation from an atlas image.

    :Parameters:
        file_name : str
            Filename of the image source to load.
        rows : int
            Row number of atlas image.
        cols : int
            Column number of atlas image.
        initial_frame : int
            Initial frame of animation.
        total_frames : int
            How much frames starting from ``initial_frame`` the animation will
            have. If None, will use until end of atlas.
        duration : float
            Duration in seconds of each frame, default = ``1/60.0``
        anchor : "center" or a tuple (anchor_x, anchor_y)
            Image's anchor. Applied to all frames.

    :rtype: ``pyglet.image.Animation``
    :return: A ``pyglet.image.Animation`` object.
    '''
    total_frames = total_frames or (rows*cols - 1)
    atlas = load_atlas(file_name, rows, cols)
    sequence = atlas[initial_frame:initial_frame+total_frames+1]
    animation = pyglet.image.Animation.from_image_sequence(sequence, duration)

    return _anchor_animation(animation, anchor)


def _anchor_image(image, anchor):
    '''
    Internal function to apply an anchor in a given image.

    :Parameters:
        image : ``pyglet.image.Texture`` or other image
            A ``pyglet.image.Texture`` object.
        anchor : "center" or a tuple (anchor_x, anchor_y)
            Image's anchor.
    
    :rtype: ``pyglet.image.Texture`` or other image
    :return: A ``pyglet.image.Texture`` object.
    '''
    if anchor == 'center':
        anchor = image.width/2, image.height/2

    image.anchor_x, image.anchor_y = anchor
    return image

def _anchor_animation(animation, anchor):
    '''
    Internal function to apply an anchor in every frame of an animation.

    :Parameters:
        animation : list of images or ``pyglet.image.Animation``
            A ``pyglet.image.Animation`` object.
        anchor : "center" or a tuple (anchor_x, anchor_y)
            Image's anchor. Appplied to all frames

    :rtype: ``pyglet.image.Animation``
    :return: A ``pyglet.image.Animation`` object.
    '''
    try:
        if anchor == 'center':
            anchor = animation.get_max_width()/2, animation.get_max_height()/2

        for frame in animation.frames:
            frame.image.anchor_x, frame.image.anchor_y = anchor
    except:
        if anchor == 'center':
            anchor = animation[0].width/2, animation[0].height/2
        
        for image in animation:
            image.anchor_x, image.anchor_y = anchor

    return animation

