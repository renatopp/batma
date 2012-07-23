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

'''Utility functions'''

import random
import weakref
import batma

def frange(start, stop=None, step=1):
    '''A range function, that does accept float increments'''
    return [x for x in xfrange(start, stop, step)]

def xfrange(start, stop=None, step=1):
    '''A xrange function, that does accept float increments.'''
    step = float(step)
    if stop is None:
        start, stop = 0, start

    i = start
    while i < stop:
        yield i
        i += step

def is_iterable(value):
    '''Verify if a ``value`` is an iterable'''
    try:
        iter(value)
    except TypeError:
        return False

    return True

def random_position(offset_x=0, offset_y=0):
    return batma.Vector2(
        random.randint(offset_x, batma.display.width-offset_x),
        random.randint(offset_y, batma.display.height-offset_y),
    )

def singleton(cls):
    '''Singleton decorator'''
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

class classproperty(property):
    '''Decorator for class property'''
    def __get__(self, cls, owner):
        return self.fget.__get__(None, owner)()


class WeakList(object):
    def __init__(self, *args):
        self.__items = []
        for a in args:
            self.append(a)

    def append(self, obj):
        self.__items.append(weakref.ref(obj))

    def remove(self, obj):
        self.__items.remove(weakref.ref(obj))

    def clear(self):
        self.__items = []

    def to_list(self):
        result = []
        for i in reversed(xrange(len(self.__items))):
            item = self.__items[i]()
            if item is None:
                del self.__items[i]
            else:
                result.insert(0, item)

        return result

    def iter(self):
        for i in reversed(xrange(len(self.__items))):
            item = self.__items[i]()
            if item is None:
                del self.__items[i]
            else:
                yield item   
