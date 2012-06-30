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

'''This module provides precalculated values, mathematical functions and an 
interface for the built-in math library.'''

__all__ = []

from batma.util import is_iterable
from math import *

# CONSTANTS ===================================================================
pi = pi
e = e
pi_over_2 = pi/2.0
pi_over_4 = pi/4.0
two_pi = 2*pi
log10e = log10(e)
log2e = log(e, 2)
# =============================================================================

# SHORTCUTS FUNCTIONS =========================================================
abs = abs
max = max
min = min
pow = pow
round = round
# =============================================================================

def inversesqrt(value):
    '''Returns ``1/sqrt(x)``.'''
    return 1.0/sqrt(value)

def mod(a, b):
    '''Returns ``a%b``. This is just an equivalent for the %-operator.'''
    return a%b

def sign(value):
    '''Returns -1 with a negative argument, +1 with a positive argument, and 0 
    if its argument is zero.'''
    if value == 0: return 0
    elif value > 0: return 1
    else: return -1

def step(value, threshold):
    '''Returns 0 if ``value < threshold``, otherwise 1.'''
    return 1 if value >= threshold else 0

def clamp(value, min_value, max_value):
    '''Restricts a value to be within a specified range'''
    return max(min_value, min(value, max_value))

def wrap_angle(angle):
    '''Reduces a given angle to a value between pi and -pi'''
    if angle > 0:
        result = fmod(angle+pi, two_pi) - pi;
    else:
        result = fmod(angle-pi, two_pi) + pi;

    return result

def distance(value1, value2):
    '''Calculates the absolute value of the difference of two values'''
    if not is_iterable(value1): value1 = [value1]
    if not is_iterable(value2): value2 = [value2]

    return sqrt(sum((v1-v2)**2 for v1, v2 in zip(value1, value2)))
