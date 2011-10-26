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
Interface classes for pyglet's text manipulation components.
'''

import pyglet
from batma.node import BatmaNode

class TextElement(BatmaNode):
    """
    Base class for all cocos text

    Provides the CocosNode interfase and a pyglet Batch to store parts
    Functionality other that the one common to all cococsnodes, except 'opacity', is
    provided by the member 'element' , which is the underlying pyglet object.
    """
    def __init__(self, text=u'', position=(0,0), **kwargs):
        super(TextElement, self).__init__()
        self.position = position
        self.args = []
        self.kwargs = kwargs
        kwargs['text']=text
        self.element = self.klass(**self.kwargs)

    def draw(self):
        pyglet.gl.glPushMatrix()
        self.transform()
        self.element.draw()
        pyglet.gl.glPopMatrix()


class Label(TextElement):
    klass = pyglet.text.Label

    def __init__(self, text='', position=(0, 0), color=(255, 255, 255), **kwargs):
        if len(color) == 3:
            color = color+(255,)
        kwargs['text'] = text
        kwargs['color'] = color
        kwargs['position'] = position
        kwargs['font_name'] = kwargs.get('font_name', 'Times New Roman')
        kwargs['font_size'] = kwargs.get('font_size', 36)
        kwargs['anchor_x'] = kwargs.get('anchor_x', 'center')
        kwargs['anchor_y'] = kwargs.get('anchor_y', 'center')

        super(Label, self).__init__(**kwargs)


class HTMLLabel(TextElement):
    klass = pyglet.text.HTMLLabel

    def __init__(self, text='', position=(0, 0), **kwargs):
        kwargs['text'] = text
        kwargs['position'] = position
        kwargs['anchor_x'] = kwargs.get('anchor_x', 'center')
        kwargs['anchor_y'] = kwargs.get('anchor_y', 'center')

        super(HTMLLabel, self).__init__(**kwargs)
