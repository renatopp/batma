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

'''This module contains the main classes for game creation

A game that inherits the Game class have the following flow:

    1. initialize
    2. load_content
    3. repeat:

       1. update
       2. draw
'''

import pyglet
from pyglet import gl
import batma
from batma.camera import Camera
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

class WindowProxy(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(WindowProxy, self).__init__(*args, **kwargs)

        self._background_color = (0, 0, 0, 0)
        self._virtual_width = self.width
        self._virtual_height = self.height
        self._offset_x = 0
        self._offset_y = 0
        self._usable_width = self.width
        self._usable_height = self.height

        self.set_alpha_blending()

    def get_background_color(self):
        return batma.Color(int(self._background_color[0]*255),
                           int(self._background_color[1]*255),
                           int(self._background_color[2]*255),
                           int(self._background_color[3]*255))
    def set_background_color(self, value):
        alpha = value[3] if len(value) > 3 else 255
        self._background_color = (
            value[0]/255.0,
            value[1]/255.0,
            value[2]/255.0,
            alpha/255.0
        )
    background_color = property(get_background_color, set_background_color)

    @property
    def size(self):
        return Vector2(self.width, self.height)
    
    @size.setter
    def size(self, value):
        self.set_size(value[0], value[1])

    @property
    def center(self):
        return Vector2(self.width/2.0, self.height/2.0)

    def clear(self):
        super(WindowProxy, self).clear()
        pyglet.gl.glClearColor(*self._background_color)

    def on_resize(self, width, height):
        pw, ph = width, height
        vw, vh = self.get_virtual_size()
        v_aratio = vw/float(vh)
        uw = int(min(pw, ph*v_aratio))
        uh = int(min(ph, pw/v_aratio))
        ox = (pw-uw)//2
        oy = (ph-uh)//2
        self._offset_x = ox
        self._offset_y = oy
        self._usable_width = uw
        self._usable_height = uh
        self.set_projection()

    def get_virtual_size(self):
        return Vector2(self._virtual_width, self._virtual_height)

    def set_projection(self):
        '''Set 3D porjection'''

        vw, vh = self.get_virtual_size()
        aratio = self._usable_width/float(self._usable_height)

        gl.glViewport(self._offset_x, self._offset_y, self._usable_width, self._usable_height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.gluPerspective(60, aratio, 0.1, 3000.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        gl.gluLookAt(
            vw/2.0, vh/2.0, vh/1.1566,   # eye
            vw/2.0, vh/2.0, 0,           # center
            0.0, 1.0, 0.0                # up vector
        )

    def set_alpha_blending(self, on=True):
        """
        Enables/Disables alpha blending in OpenGL
        using the GL_ONE_MINUS_SRC_ALPHA algorithm.
        On by default.
        """
        if on:
            gl.glEnable(gl.GL_BLEND)
            gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        else:
            gl.glDisable(gl.GL_BLEND)

    def set_depth_test(sefl, on=True):
        '''Enables z test. On by default
        '''
        if on:
            gl.glClearDepth(1.0)
            gl.glEnable(GL_DEPTH_TEST)
            gl.glDepthFunc(GL_LEQUAL)
            gl.glHint(gl.GL_PERSPECTIVE_CORRECTION_HINT, gl.GL_NICEST)
        else:
            gl.glDisable(gl.GL_DEPTH_TEST)


class Game(WindowProxy):
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
        self.background_color = batma.colors.LAVANDERBLUE
        
        # TESTES
        self._main_scene = None
        self._scenes = []
        self._fps_display = pyglet.clock.ClockDisplay()

        self.camera = Camera(self.center)
        self.auto_clear = True
        self.show_fps = False

        # Input
        self.keyboard = KeyboardState()
        self.mouse = MouseState()
        self.push_handlers(self.keyboard)
        self.push_handlers(self.mouse)

        self.set_mouse_visible(True)
        self.set_exclusive_mouse(False)

        # Callbacks
        pyglet.clock.schedule(self.on_update)

        # Resources
        pyglet.resource.path = []
        batma.add_resource_path('.')

        # Calls
        self.initialize()
        pyglet.resource.reindex()
        self.load_content()
        
    def on_update(self, tick):
        for scene in self._scenes:
            scene.update(tick)

        self.update(tick)
        self.camera.update(tick)

    def on_draw(self):
        '''
        The window contents must be redrawn. Inherited from 
        ``pyglet.window.Window``.
        '''
        if self.auto_clear:
            self.clear()
            
        pyglet.gl.glPushMatrix()
        self.camera.reset(self.center)

        self.draw()

        for scene in self._scenes:
            scene.draw()

        self.camera.apply(self.center)
        pyglet.gl.glPopMatrix()

        if self.show_fps:
            self._fps_display.draw()


    def add_scene(self, scene):
        scene.game = self
        scene.load_content()
        if not scene.popup:
            if self._main_scene:
                self.remove_scene(self._main_scene)
            self._main_scene = scene
            self._scenes.insert(0, scene)
        else:
            self._scenes.append(scene)
    
    def remove_scene(self, scene):
        self._scenes.remove(scene)


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

