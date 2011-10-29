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
Contains the main classes for game flow control.

A game that inherits the Game class have the following flow:

    1. initialize
    2. load_content
    3. repeat:

       1. update
       2. draw

Usage::

    class MyBatmaGame(batma.Game):
        def initialize(self):
            pass
        
        def load_content(self):
            pass
        
        def update(self):
            pass
        
        def draw(self):
            pass
    
    game = MyBatmaGame()
    batma.run()
'''

__docformat__ = 'restructuredtext'

import pyglet
import batma
from batma.input import KeyboardState
from batma.input import MouseState
from batma.util import singleton
from batma.algebra import Vector2
from batma import colors

@singleton
class Batch(pyglet.graphics.Batch):
    def __init__(self):
        pyglet.graphics.Batch.__init__(self)

        self.base_group = pyglet.graphics.OrderedGroup(2)
        self.fringe_group = pyglet.graphics.OrderedGroup(4)
        self.object_group = pyglet.graphics.OrderedGroup(8)
        self.text_group = pyglet.graphics.OrderedGroup(16)

class Game(pyglet.window.Window):
    '''
    Game flow control.

    This class inherits a ``pyglet.window.Window`` to create a graphical 
    application, every method related to pyglet window can be applied here.

    **Important!** Do not overrid ``__init__`` or ``on_draw``.

    :Ivariables:
        keyboard : `KeyboardState`
            A `KeyboardState` object that handle keyboard input.
        mouse : `MouseState`
            A `MouseState` object that handle mouse input.
    '''

    def __init__(self, *args, **kwargs):
        '''Create a Game window instance.

        All parameters are sent to ``pyglet.window.Window`` and they are 
        optional.

        Consult pyglet's documentation for better understand.

        :Parameters:
            width : int
                Width of the window, in pixels.  Defaults to 640, or the
                screen width if ``fullscreen`` is True.
            height : int
                Height of the window, in pixels.  Defaults to 480, or the
                screen height if ``fullscreen`` is True.
            caption : str or unicode
                Initial caption (title) of the window.  Defaults to "A Batma 
                Game".
            resizable` : bool
                If True, the window will be resizable.  Defaults to False.
            style : int
                One of the ``WINDOW_STYLE_*`` constants specifying the
                border style of the window.
            fullscreen : bool
                If True, the window will cover the entire screen rather
                than floating.  Defaults to False.
            visible : bool
                Determines if the window is visible immediately after
                creation.  Defaults to True.  Set this to False if you
                would like to change attributes of the window before
                having it appear to the user.
            vsync : bool
                If True, buffer flips are synchronised to the primary screen's
                vertical retrace, eliminating flicker.
            display : ``Display``
                The display device to use.  Useful only under X11.
            screen : ``Screen``
                The screen to use, if in fullscreen.
            config : ``pyglet.gl.Config``
                Either a template from which to create a complete config,
                or a complete config.
            context : ``pyglet.gl.Context``
                The context to attach to this window.  The context must
                not already be attached to another window.
            mode : ``ScreenMode``
                The screen will be switched to this mode if ``fullscreen`` is
                True.  If None, an appropriate mode is selected to accomodate
                ``width`` and ``height``.
        '''
        if len(args) < 3 and 'caption' not in kwargs:
            kwargs['caption'] = 'A Batma Game'

        super(Game, self).__init__(*args, **kwargs)

        self.batch = Batch()
        self.background_color = colors.BLACK

        # Input
        self.keyboard = KeyboardState()
        self.mouse = MouseState()
        self.push_handlers(self.keyboard)
        self.push_handlers(self.mouse)

        self.set_mouse_visible(True)
        self.set_exclusive_mouse(False)

        # Callbacks
        pyglet.clock.schedule(self.update)

        # Resources
        pyglet.resource.path = []
        batma.add_resource_path('.')

        # Calls
        self.initialize()
        pyglet.resource.reindex()
        self.load_content()

    @property
    def size(self):
        return Vector2(self.width, self.height)
    
    @size.setter
    def size(self, value):
        self.set_size(value[0], value[1])

    @property
    def center(self):
        return Vector2(self.width/2.0, self.height/2.0) 

    def on_draw(self):
        '''
        The window contents must be redrawn. Inherited from 
        ``pyglet.window.Window``.
        '''
        self.clear()
        pyglet.gl.glClearColor(*(self.background_color+(1,)))
        self.draw()

    def initialize(self):
        '''
        Initialize method. Override Me =]

        This is the first method called on Game instantiation, you can set game
        properties overriding it, e.g., screen and pyglet configurations.
        '''
        pass

    def load_content(self):
        '''
        Load Content method. Override Me =]

        Called after `initialize`, the goal of this method is to loads every 
        game asset such images, animation, sounds, fonts, etc.
        '''
        pass

    def update(self, tick):
        '''
        Update method. Override Me =]

        Called every frame **BEFORE** `draw`. This is the best method for game 
        logic.
        '''
        pass

    def draw(self):
        '''
        Draw method. Override Me =]

        Called every frame **AFTER** `update`. This method is the place to draw
        every object in screen.
        '''
        pass

