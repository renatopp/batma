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

'''Batma's main module.

Batma 2D game engine provides an intuitive structure for game development and 
other graphical applications.

Main features:

  - Automatic import regular (equally spaced) images atlas in a list of images;
  - Animated sprites creation from image atlas or gifs;
  - Easy-to-use pyglet components, e.g. sprites, texts and resource location;
  - Input state for for keyboard and mouse (similar to XNA);
  - Primitives drawning: opengl defaults, circle, rectangle;
  - 2D cameras handling
  - Scenes based games
'''

__version__ = "0.1"
__author__ = "Renato de Pontes Pereira"
version = __version__

from batma.engine import *
from batma.camera import *
from batma.scene import *
from batma.resource import *
from batma.sprite import *
from batma.text import *
from batma.node import *
from batma.algebra import *
from batma import draw
from batma import colors
from pyglet import gl
import pyglet.window.key as keys
import pyglet.window.mouse as buttons

def run():
    '''Starts the game.

    It's the same of ``pyglet.app.run()``
    '''
    pyglet.app.run()