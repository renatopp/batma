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

__all__ = ['Scene']

import pygame

class Scene(object):
    popup = True

    def __init__(self, *args, **kwargs):
        self.__scenes = []
        self.__main_scene = None
        self.__arguments = (args, kwargs)

    def add_scene(self, scene):
        if scene.popup:
            self.__scenes.append(scene)
        else:
            if self.__main_scene is not None:
                self.remove_scene(self.__main_scene)
            self.__main_scene = scene
            self.__scenes.insert(0, scene)

        scene._initialize()
        scene._load_content()

    def remove_scene(self, scene=None):
        if scene is None:
            for s in self.__scenes:
                s._unload_content()
            self.__scenes = []
        else:
            self.__scenes.remove(scene)
            scene._unload_content()

    def _initialize(self):
        args, kwargs = self.__arguments
        self.initialize(*args, **kwargs)

    def _load_content(self):
        self.load_content()

    def _unload_content(self):
        self.unload_content()
        for scene in self.__scenes:
            scene._unload_content()

    def _update(self, tick):
        self.update(tick)
        for scene in self.__scenes:
            scene._update(tick)

    def _draw(self):
        self.draw()
        for scene in self.__scenes:
            scene._draw()

    def initialize(self, *args, **kwargs):
        pass

    def load_content(self):
        pass

    def unload_content(self):
        pass

    def update(self, tick):
        pass

    def draw(self):
        pass
