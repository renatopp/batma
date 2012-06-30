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
'''

__version__ = "0.1"
__author__ = "Renato de Pontes Pereira"
version = __version__

__all__ = []

# Import from PYGAME ==========================================================
from pygame import Rect
# =============================================================================

# Import CORE =================================================================
from batma.core.engine import *
from batma.core.display import *
from batma.core.scene import *
from batma.core.camera import *
# =============================================================================

# Import GRAPHICS =============================================================
from batma.graphics.colors import *
from batma.graphics.sprite import *
from batma.graphics.text import *
from batma.graphics import colors
from batma.graphics import draw
# =============================================================================

# Import INPUTS ===============================================================
from batma.inputs.states import *
from batma.inputs import buttons
from batma.inputs import keys
# =============================================================================

# Import MATHS ================================================================
from batma.maths.algebra import *
from batma.maths.interpolation import *
from batma.maths import interpolation
from batma.maths import mathematic as math
# =============================================================================

# Import TIMES ================================================================
from batma.time import *
# =============================================================================

# Import ITER =================================================================
from batma import iter
# =============================================================================

# Import RESOURCE =============================================================
from batma import resource
# =============================================================================

# GLOBALS =====================================================================
camera = None
clock = Clock()
display = Display()
engine = Engine()
game = None
keyboard = KeyboardState()
mouse = MouseState()
# =============================================================================

def run(*args, **kwargs):
    '''Set up the engine and starts the game'''
    engine.apply_config(*args, **kwargs)
    engine.start()


