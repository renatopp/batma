
import pyglet
from pyglet import gl

import batma
from batma import colors
from batma.util import singleton
from batma.input import MouseState
from batma.input import KeyboardState
from batma.algebra import Vector2

@singleton
class Engine(object):
    def __init__(self):
        self.game = None
        self.window = None
        self.local_batch = None

        pyglet.resource.path = []
        batma.add_resource_path('.')

    def config(self, game, window):
        self.game = game
        self.window = window
        self.window.engine = self

        self.game.initialize()
        pyglet.resource.reindex()
        self.game.load_content()

    def start(self):
        pyglet.app.run()

    def stop(self):
        self.game._unload_content()
    
    def update(self, tick):
        self.game._update(tick)
    
    def draw(self):
        self.game._draw()


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        if len(args) < 3 and 'caption' not in kwargs:
            kwargs['caption'] = 'A Batma Game'

        super(Window, self).__init__(*args, **kwargs)
        
        self.engine = None
        self.keyboard = KeyboardState()
        self.mouse = MouseState()
        self.push_handlers(self.keyboard)
        self.push_handlers(self.mouse)

        self._background_color = (0, 0, 0, 0)        
        self._virtual_width = self.width
        self._virtual_height = self.height
        self._offset_x = 0
        self._offset_y = 0
        self._usable_width = self.width
        self._usable_height = self.height
        self._set_alpha_blending()

        pyglet.clock.schedule(self.on_update)
        self.background_color = colors.LAVANDERBLUE

    def _get_virtual_size(self):
        '''Get virtual width and height'''
        return Vector2(self._virtual_width, self._virtual_height)

    def _set_projection(self):
        '''Set 3D porjection'''

        vw, vh = self._get_virtual_size()
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

    def _set_alpha_blending(self, on=True):
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

    def _set_depth_test(sefl, on=True):
        '''Enables z test. On by default
        '''
        if on:
            gl.glClearDepth(1.0)
            gl.glEnable(GL_DEPTH_TEST)
            gl.glDepthFunc(GL_LEQUAL)
            gl.glHint(gl.GL_PERSPECTIVE_CORRECTION_HINT, gl.GL_NICEST)
        else:
            gl.glDisable(gl.GL_DEPTH_TEST)


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
        gl.glClearColor(*self._background_color)
    background_color = property(get_background_color, set_background_color)


    def on_resize(self, width, height):
        pw, ph = width, height
        vw, vh = self._get_virtual_size()
        v_aratio = vw/float(vh)
        uw = int(min(pw, ph*v_aratio))
        uh = int(min(ph, pw/v_aratio))
        ox = (pw-uw)//2
        oy = (ph-uh)//2
        self._offset_x = ox
        self._offset_y = oy
        self._usable_width = uw
        self._usable_height = uh
        self._set_projection()

    def on_update(self, tick):
        '''Update callback'''
        self.engine.update(tick)

    def on_draw(self):
        self.engine.draw()
        # self.clear()
        # gl.glColor3f(1, 1, 0)
        # pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
        #     [0, 1, 2, 0, 2, 3],
        #     ('v2i', (100, 100,
        #              150, 100,
        #              150, 150,
        #              100, 150))
        # )

    def on_close(self):
        self.engine.stop()
        super(Window, self).on_close()

# class Batch(pyglet.graphics.Batch): pass
