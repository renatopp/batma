``batma.Display``
=================

:file: ``batma/core/display.py``

.. class:: batma.Display

   SINGLETON.

   Class to handle and store all informations and functions relative to screen
   and the game window.

Variables
---------

.. data:: display.background_color
.. data:: display.caption
.. data:: display.center
.. data:: display.default_color
.. data:: display.fullscreen
.. data:: display.height
.. data:: display.max_fps
.. data:: display.rect
.. data:: display.resizable
.. data:: display.screen
.. data:: display.show_cursor
.. data:: display.show_fps
.. data:: display.size
.. data:: display.width

Methods
-------

.. function:: display.__init__(caption=u'Batma Game', size=(640, 480), resizable=False, fullscreen=False, max_fps=60)
.. function:: display.init()
.. function:: display.clear(color=None)
.. function:: display.apply_config(caption=None, size=None, resizable=None, fullscreen=None, max_fps=None)
.. function:: display.draw(obj, rect)