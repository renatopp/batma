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

from batma.engine import Engine
from batma.algebra import Vector2

class Scene(object):
    popup = False

    def __init__(self, *args, **kwargs):
        self.engine = Engine()
        self.window = self.engine.window
        self.game = self.engine.game

        self._main_scene = None
        self._scenes = []
        self.scheduled_calls = []
        self.scheduled_interval_calls = []
        self._init(*args, **kwargs)

    def _init(self, *args, **kwargs):
        self.initialize(*args, **kwargs)
        self.load_content()

    #shortcuts
    @property
    def center(self):
        return Vector2(self.window.width/2.0, self.window.height/2.0)

    @property
    def size(self):
        return Vector2(self.window.width, self.window.height)
    
    @property
    def width(self):
        return self.window.width
    
    @property
    def height(self):
        return self.window.height
    
    @property
    def keyboard(self):
        return self.window.keyboard

    @property
    def mouse(self):
        return self.window.mouse

    def schedule_interval(self, callback, interval, *args, **kwargs):
        """
        Schedule a function to be called every `interval` seconds.

        Specifying an interval of 0 prevents the function from being
        called again (see `schedule` to call a function as often as possible).

        The callback function prototype is the same as for `schedule`.

        :Parameters:
            `callback` : function
                The function to call when the timer lapses.
            `interval` : float
                The number of seconds to wait between each call.

        This function is a wrapper to pyglet.clock.schedule_interval.
        It has the additional benefit that all calllbacks are paused and
        resumed when the node leaves or enters a scene.

        You should not have to schedule things using pyglet by yourself.
        """

        pyglet.clock.schedule_interval(callback, interval, *args, **kwargs)
        self.scheduled_interval_calls.append(
            (callback, interval, args, kwargs)
        )

    def schedule(self, callback, *args, **kwargs):
        """
        Schedule a function to be called every frame.

        The function should have a prototype that includes ``dt`` as the
        first argument, which gives the elapsed time, in seconds, since the
        last clock tick.  Any additional arguments given to this function
        are passed on to the callback::

            def callback(dt, *args, **kwargs):
                pass

        :Parameters:
            `callback` : function
                The function to call each frame.

        This function is a wrapper to pyglet.clock.schedule.
        It has the additional benefit that all calllbacks are paused and
        resumed when the node leaves or enters a scene.

        You should not have to schedule things using pyglet by yourself.
        """
        pyglet.clock.schedule(callback, *args, **kwargs)
        self.scheduled_calls.append((callback, args, kwargs))

    def unschedule(self, callback):
        """
        Remove a function from the schedule.

        If the function appears in the schedule more than once, all occurances
        are removed.  If the function was not scheduled, no error is raised.

        :Parameters:
            `callback` : function
                The function to remove from the schedule.

        This function is a wrapper to pyglet.clock.unschedule.
        It has the additional benefit that all calllbacks are paused and
        resumed when the node leaves or enters a scene.

        You should not unschedule things using pyglet that where scheduled
        by node.schedule/node.schedule_interface.
        """
        self.scheduled_calls = [
            c for c in self.scheduled_calls if c[0] != callback
        ]
        self.scheduled_interval_calls = [
            c for c in self.scheduled_interval_calls if c[0] != callback
        ]

        pyglet.clock.unschedule(callback)

    def resume_scheduler(self):
        """
        Time will continue/start passing for this node and callbacks
        will be called, worker actions will be called
        """
        for c, i, a, k in self.scheduled_interval_calls:
            pyglet.clock.schedule_interval(c, i, *a, **k)
        for c, a, k in self.scheduled_calls:
            pyglet.clock.schedule(c, *a, **k)

    def pause_scheduler(self):
        """
        Time will stop passing for this node: scheduled callbacks will
        not be called, worker actions will not be called
        """
        for f in set(
            [x[0] for x in self.scheduled_interval_calls] +
            [x[0] for x in self.scheduled_calls]
                ):
            pyglet.clock.unschedule(f)
        for arg in self.scheduled_calls:
            pyglet.clock.unschedule(arg[0])


    def add_scene(self, scene):
        self.window.push_handlers(scene)

        if not scene.popup:
            if self._main_scene:
                self.remove_scene(self._main_scene)
            self._main_scene = scene
            self._scenes.insert(0, scene)
        else:
            self._scenes.append(scene)

    def remove_scene(self, scene):
        self.window.remove_handlers(scene)
        self._scenes.remove(scene)

    def _unload_content(self):
        self.unload_content()
        for scene in self._scenes:
            scene._unload_content()

    def _update(self, tick):
        self.update(tick)
        for scene in self._scenes:
            scene._update(tick)

    def _draw(self):
        self.draw()
        for scene in self._scenes:
            scene._draw()


    def initialize(self):
        pass

    def load_content(self):
        pass

    def unload_content(self):
        pass

    def update(self, tick):
        pass

    def draw(self):
        pass
