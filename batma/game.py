import pyglet
from batma.engine import Engine
from batma.engine import Window
from batma.scene import Scene

class Game(Scene):
    def __init__(self, *args, **kwargs):
        self.engine = Engine()
        super(Game, self).__init__()

        self._fps_display = pyglet.clock.ClockDisplay()
        self.auto_clear = True
        self.show_fps = False

        self.window = Window(*args, **kwargs)
        self.window.push_handlers(self)
        self.engine.config(self, self.window)
    
    def _init(self, *args, **kwargs):
        pass

    def _draw(self):
        if self.auto_clear:
            self.window.clear()

        super(Game, self)._draw()

        if self.show_fps:
            self._fps_display.draw()

    def start(self):
        self.engine.start()

