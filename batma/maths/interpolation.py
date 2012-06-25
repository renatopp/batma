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

__all__ = ['Interpolation']

from batma.util import frange, xfrange
import batma.maths.mathematic as math

CYCLE = 1
BOUNCE = 2
INVERT = 3

def lerp(value1, value2, amount):
    '''Linearly interpolates between two values'''
    return value1 + (value2-value1)*amount
linear = lerp

def smoothstep(value1, value2, amount, power=1):
    '''Interpolates between two values using a cubic equation'''
    for i in xrange(power): 
        amount = (amount*amount*(3 - 2*amount))

    return linear(value1, value2, amount)

def highpower(value1, value2, amount, power=2):
    '''Interpolates between two values using a cubic equation'''
    return linear(value1, value2, amount**power)

def ihighpower(value1, value2, amount, power=2):
    '''Inverse Highpower'''
    amount = 1 - (1-amount)**power
    return linear(value1, value2, amount)

def sin(value1, value2, amount):
    '''Performs a sin interpolation'''
    amount = math.sin(amount*math.pi_over_2)
    return linear(value1, value2, amount)

def isin(value1, value2, amount):
    '''Performs an inverse sin interpolation'''
    amount = 1 - math.sin((1-amount)*math.pi_over_2)
    return linear(value1, value2, amount)

def hermite(value1, tangent1, value2, tangent2, amount):
    '''Performs a Hermite spline interpolation'''
    t2 = amount * amount
    t3 = t2 * amount
    _3t2 = 3.0 * t2
    _2t3 = 2.0 * t3

    return (
          value1*(_2t3-_3t2+1) 
        + value2*(-_2t3+_3t2) 
        + tangent1*(t3-2.0*t2+amount) 
        + tangent2*(t3-t2))

def catmullrom(value1, value2, value3, value4, amount):
    '''Performs a Catmull-Rom interpolation using the specified positions'''
    return (
          amount*((2-amount)*amount - 1)   * value1
        + (amount*amount*(3*amount - 5) + 2) * value2
        + amount*((4 - 3*amount)*amount + 1) * value3
        + (amount-1)*amount*amount         * value4 ) / 2.0

class Interpolation(object):
    ''' Interpolation Helper

    Performs a given interpolation ``function`` from ``initial`` to ``final``
    in ``n`` steps.
    '''
    def __init__(self, function, initial, final, n=100, flag=None):
        self.__initial = initial
        self.__final = final
        self.__step = 1.0/n
        
        self.function = function
        self.initial = initial
        self.final = final
        self.flag = flag
        self.n = n

        self.step_amount = 0
        self.done = False

    def __call__(self):
        r = self.function(self.initial, self.final, self.step_amount)
        self.step_amount += self.__step

        if self.step_amount > 1:
            self.step_amount = 1
            self.done = True
        elif self.step_amount < 0:
            self.step_amount = 0
            self.done = True

        if self.done and self.flag is not None:
            if self.flag == CYCLE:
                self.step_amount = 0
            elif self.flag == BOUNCE:
                self.__step *= -1
            elif self.flag == INVERT:
                self.step_amount = 0
                self.initial, self.final = self.final, self.initial

            self.done = False

        return r

