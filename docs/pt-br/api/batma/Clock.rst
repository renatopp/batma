``batma.Clock``
===============

:file: ``batma/time.py``

.. class:: batma.Clock

   SINGLETON. 

   Class for calculating and limiting framerate. This class is used by 
   :data:`batma.engine` to track and control the game time.

   All times here are represented in milliseconds (1/1000 seconds).
   

Variables
---------

.. data:: clock.time

   READONLY.

   Return the milliseconds since the last call to :func:`tick`.


.. data:: clock.rawtime
   
   READONLY.

   Return the milliseconds since the last call to :func:`tick` without 
   include the delayed time used to limit the framerate.


.. data:: clock.fps

   READONLY.

   Return the game's framerate (in frames per second).


.. data:: clock.ticks
   
   READONLY.

   Return the time passed since the game init.


Methods
-------

.. function:: clock.tick(framerate=0)

   Update the clock. 

   This method is called once per frame by :data:`batma.engine`. It computes 
   how milliseconds have passed since the previous call. If ``framerate`` is
   bigger than ``0``, this method will limit the runtime speed of the game to 
   approximately ``framerate`` frames per second.

   :param framerate: frame limit of the game, 0 to unlimited frames. Default to 0.
   :return: milliseconds since the previous call.


.. function:: clock.tick_busy_loop(framerate=0)

   Update the clock.

   It computes how many milliseconds have passed since the previous call. If 
   ``framerate`` is bigger than ``0``, this method will limit the runtime speed 
   of the game to approximately ``framerate`` frames per second. 

   This method uses lots of cpu in a busy loop to make sure that timing is more
   acurate.

   :param framerate: frame limit of the game, 0 to unlimited frames. Default to 0.
   :return: milliseconds since the previous call.
