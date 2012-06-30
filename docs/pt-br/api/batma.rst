``batma`` --- Batma
===================

.. module:: batma
   :synopsis: Batma's main module.

:file: ``batma/__init__.py``

Batma's main module.


Classes
-------

.. toctree::
   :maxdepth: 1
 
   batma/Camera
   batma/Clock
   batma/Color
   batma/Display
   batma/Engine
   batma/GameObject
   batma/Interpolation
   batma/KeyboardState
   batma/MouseState
   batma/Scene
   batma/Sprite
   batma/Text
   batma/Timer
   batma/Vector2
   batma/Vector3

Functions
---------

.. function:: run(*args, **kwargs):

   Set up the :data:`engine` and starts de game.


Globals
-------

.. data:: camera

   A instance of :class:`Camera`. This variable is just available after setting
   up the engine. This camera is initialized with position centralized on the
   screen and anchor in the center.


.. data:: clock

   A singleton instance of :class:`Clock` used as to the control of the game 
   clock.


.. data:: display

   A singleton instance of :class:`Display`, which stores all informations 
   about the screen and game window.


.. data:: engine

   A singleton instance of :class:`Engine`, which control the main loop and
   the initial settings of the game.


.. data:: game

   The user defined Game object, passed as argument to :func:`batma.run()`. 
   This variable is just available after setting up the engine. It is an 
   instance of :class:`Scene`.


.. data:: keyboard

   A singleton instance of :class:`KeyboardState`.


.. data:: mouse

   A singleton instance of :class:`MouseState`.


.. data:: timer

   A singleton instance of :class:`Timer`, used for scheduling of user defined 
   functions.

