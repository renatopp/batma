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
Classes and function for input handling.
'''

__docformat__ = 'restructuredtext'

class AbstractInputState(dict):
    def __getitem__(self, key):
        return self.get(key, False)

    def is_pressed(self, key):
        '''
        Verify if a key or button is pressed.
        '''
        return self[key]

class KeyboardState(AbstractInputState):
    '''
    Keyboard input handler.

    A KeyboardState object intercepts the keyboard events and keep the pressed 
    keys. You must register a KeyboardState instance as an window handler, 
    e.g., ``game.push_handlers(keyboardstate)``.
    '''
    def on_key_press(self, symbol, modifiers):
        '''
        Key press event.
        '''
        self[symbol] = True

    def on_key_release(self, symbol, modifiers):
        '''
        Key release event.
        '''
        del self[symbol]

class MouseState(AbstractInputState):
    '''
    Mouse input handler.

    A MouseState object intercepts all mouse events and keep the pressed 
    buttons, position and scroll values. You must register a MouseState 
    instance as an window handler, e.g., ``game.push_handlers(mousestate)``.

    :Ivariables:
        x : float
            Last position of mouse cursor in axis X.
        y : float
            Last position of mouse cursor in axis Y.     
        in_screen : bool
            A flag to tell if cursor is over game screen or out of it.
        scroll_value : int
            Acumuled value os scroll whell.
    '''

    def __init__(self):
        super(MouseState, self).__init__()

        self.x = 0
        self.y = 0
        self.in_screen = False
        self.scroll_value = 0

    def on_mouse_motion(self, x, y, dx, dy):
        '''
        Mouse motion event.
        '''
        self.x, self.y = x, y

    def on_mouse_press(self, x, y, button, modifiers):
        '''
        Mouse press event.
        '''
        self[button] =  True

    def on_mouse_release(self, x, y, button, modifiers):
        '''
        Mouse release event.
        '''
        del self[button]
    
    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        '''
        Mouse drag event.
        '''
        self.x, self.y = x, y

    def on_mouse_enter(self, x, y):
        '''
        Mouse enter event.
        '''
        self.in_screen = True
    
    def on_mouse_leave(self, x, y):
        '''
        Mouse leave event.
        '''
        self.in_screen = False
    
    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        '''
        Mouse scroll event.
        '''
        self.scroll_value += scroll_y