``batma.Color``
===============

:file: ``batma/graphics/colors.py``

.. class:: batma.Color

   Inherits and extends the `pygame.Color`_ class.


Class Properties
----------------

.. data:: Random

   Return a randomized :class:`Color` object.


Variables
---------

.. data:: color.r
   
   Gets or sets the red value of the color.


.. data:: color.g

   Gets or sets the green value of the color.


.. data:: color.b

   Gets or sets the blue value of the color.


.. data:: color.a

   Gets or sets the alpha value of the color.


.. data:: color.cmy

   Gets or sets the CMY representation of the color. The ``CMY`` components are
   in the ranges ``C = [0, 1]``, ``M = [0, 1]``, ``Y = [0, 1]``.


.. data:: color.hsva

   Gets or sets the HSVA representation of the color. The HSVA components are 
   in the ranges ``H = [0, 360]``, ``S = [0, 100]``, ``V = [0, 100]``, 
   ``A = [0, 100]``.


.. data:: color.hsla

   Gets or sets the HSLA representation of the color. The HSLA components are 
   in the ranges ``H = [0, 360]``, ``S = [0, 100]``, ``L = [0, 100]``, 
   ``A = [0, 100]``.


.. data:: color.i1i2i3

   Gets or sets the I1I2I3 representation of the color. The I1I2I3 components 
   are in the ranges ``I1 = [0, 1]``, ``I2 = [-0.5, 0.5]``, 
   ``I3 = [-0.5, 0.5]``. 


Methods
-------

.. function:: color.__init__(r, g, b, a)

   Create a new color with the RGBA value.


.. function:: color.normalize()

   Returns the normalized RGBA values of the color as floating point values.

   :return: 4-tuple (R, G, B, A)


.. function:: color.correct_gamma(gamma)

   Applies a certain gamma value to the color and returns a new :class:`Color` 
   with the adjusted RGBA values.

   :param gamma: Gamma value.
   :return: :class:`Color`.


.. function:: color.set_length(len)

   The default Color length is 4. Colors can have lengths 1,2,3 or 4. This is 
   useful if you want to unpack to r,g,b and not r,g,b,a. If you want to get 
   the length of a Color do len(acolor).

   :param len: length.


.. _`pygame.Color`: http://www.pygame.org/docs/ref/color.html
